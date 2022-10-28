#FLASK_APP=myapp.py FLASK_ENV=development flask run
from flask import Flask, render_template, request
import psycopg2
import main

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")


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


@app.route("/result")
def result():
    music = main.main()
    return render_template("result.html", music = music)


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