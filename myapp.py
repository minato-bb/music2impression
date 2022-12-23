#FLASK_APP=myapp.py FLASK_ENV=development flask run
from flask import Flask, render_template, request
import psycopg2
import main
import update
import pandas as pd

app = Flask(__name__, static_folder='templates/images')

@app.route("/")
def hello_world():
    # return render_template("index.html")
    return render_template("index2.html")


@app.route("/serch_music", methods=["POST"])
def img2music():
    imp = ["威厳のある", "悲しい", "哀愁のある", "落ち着いた", "優美な", "楽しい", "興奮する", "活発な"]
    # imp_e = ["dignified, sad, sentimental, calm, graceful, happy, exciting, vigorous"]
    conn = psycopg2.connect("host=" + "localhost" +
                        " dbname=" + "fc" +
                        " user=" + "babaminato" +
                        " password=" + "")
    cur = conn.cursor()

    name = [request.form["music_name_dignified"], request.form["music_name_sad"], request.form["music_name_sentimental"], request.form["music_name_calm"], request.form["music_name_graceful"], request.form["music_name_happy"], request.form["music_name_exciting"], request.form["music_name_vigorous"]]
    artist = [request.form["artist_name_dignified"], request.form["artist_name_sad"], request.form["artist_name_sentimental"], request.form["artist_name_calm"], request.form["artist_name_graceful"], request.form["artist_name_happy"], request.form["artist_name_exciting"], request.form["artist_name_vigorous"]]

    for name_, artist_ in zip( name, artist):
        cur.execute("INSERT INTO impression_norm_test(danceability, acousticness, energy, liveness ,loudness, speechiness, tempo, valence) SELECT danceability, acousticness, energy, liveness ,loudness, speechiness, tempo, valence FROM music WHERE  music.name = '{}' AND music.artist = '{}'".format(name_, artist_))
        conn.commit()

    cur.close()
    conn.close()

    data = []
    for imp, name, artist in zip(imp, name, artist):
        data.append([imp, name, artist])
    return render_template("img2music.html", data = data)


@app.route("/result", methods=["POST"])
def result():
    music = main.main()
    return render_template("result.html", music = music)


@app.route("/update", methods=["POST"])
def update():
    word = request.form["imp_word"]
    m_name = request.form["name"]
    m_artist = request.form["artist"]

    conn = psycopg2.connect("host=" + "localhost" +
                            " dbname=" + "fc" +
                            " user=" + "babaminato" +
                            " password=" + "")
    cur = conn.cursor()
    query = 'SELECT * FROM impression_norm'
    df_sql = pd.read_sql(query, index_col="word", con=conn)
    
    cur = conn.cursor()
    cur.execute("SELECT * FROM music where name = '{}' and artist ='{}'".format(m_name, m_artist))
    m = cur.fetchall()
    conn.commit()

    target = []
    fig = df_sql.loc[word]
    for i in m:
        for data in i:
            target.append(data)
    
    data =target[2:]
    update = (data + fig)/2


    #ここを変更
    cur.execute("update test_7 set danceability={}, acousticness={}, energy={}, liveness={}, loudness={}, speechiness={}, tempo={}, valence={} where word='{}'".format(update[0], update[1], update[2], update[3], update[4], update[5], update[6], update[7], word))
    conn.commit()
    cur.close()
    conn.close()
    return render_template("update.html")


@app.route("/back")
def back():
    conn = psycopg2.connect("host=" + "localhost" +
                    " dbname=" + "fc" +
                    " user=" + "babaminato" +
                    " password=" + "")
    cur = conn.cursor()
    cur.execute("delete from impression_norm_test")
    conn.commit()
    cur.close()
    conn.close()
    return render_template("back.html")