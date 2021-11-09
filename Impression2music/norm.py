import psycopg2

def distance(name):
    conn = psycopg2.connect("host=" + "localhost" +
                            " dbname=" + "fc" +
                            " user=" + "babaminato" +
                            " password=" + "")
    cur = conn.cursor()
    cur.execute("SELECT * FROM music")
    m = cur.fetchall()
    conn.commit()
    print("The number of music is ", len(m))
    conn.commit()
    cur.execute("SELECT music.name, music.artist, distance(music.danceability, music.acousticness, music.energy, music.liveness, music.loudness, music.speechiness, music.tempo, music.valence, impression_norm.danceability, impression_norm.acousticness, impression_norm.energy, impression_norm.liveness, impression_norm.loudness, impression_norm.speechiness, impression_norm.tempo, impression_norm.valence) AS score FROM music, impression_norm WHERE impression_norm.word = '{}' ORDER BY score ASC FETCH FIRST 1 ROWS ONLY".format(name))
    n = cur.fetchall()
    conn.commit()
    print()
    print(name)
    for n_ in n:
        print(n_)
    print()
    cur.close()
    conn.close()

    return