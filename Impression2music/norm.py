import psycopg2

def distance(b):
    conn = psycopg2.connect("host=" + "localhost" +
                            " dbname=" + "fc" +
                            " user=" + "babaminato" +
                            " password=" + "")
    cur = conn.cursor()

    cur.execute("drop table target")
    conn.commit()
    cur.execute("CREATE TABLE target (danceability float, acousticness float, energy float, liveness float, loudness float, speechiness float, tempo float, valence float)")
    conn.commit()

    cur.execute("SELECT * FROM music")
    m = cur.fetchall()
    conn.commit()
    print("The number of music is ", len(m))
    conn.commit()

    cur.execute("INSERT INTO target (danceability, acousticness, energy, liveness, loudness, speechiness, tempo, valence) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", [b[0], b[1], b[2], b[3], b[4], b[5], b[6], b[7]])
    conn.commit()

    cur.execute("SELECT * FROM target")
    l = cur.fetchall()
    conn.commit()
    print(l)

    cur.execute("SELECT music.name, music.artist, distance(music.danceability, music.acousticness, music.energy, music.liveness, music.loudness, music.speechiness, music.tempo, music.valence, target.danceability, target.acousticness, target.energy, target.liveness, target.loudness, target.speechiness, target.tempo, target.valence) AS score FROM music, target ORDER BY score ASC FETCH FIRST 10 ROWS ONLY")
    n = cur.fetchall()
    conn.commit()
    print()
    for i in n:
        print(i)

    cur.close()
    conn.close()

    return