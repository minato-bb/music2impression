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

    cur.execute("SELECT name, artist FROM music WHERE name = '{}'".format(name))
    l_name = cur.fetchall()
    conn.commit()
    if len(l_name) > 1:
        for n in l_name:
            print(n)
        artist = input('アーティスト名')
        cur.execute("SELECT impression_norm.word, distance(music.danceability, music.acousticness, music.energy, music.liveness, music.loudness, music.speechiness, music.tempo, music.valence, impression_norm.danceability, impression_norm.acousticness, impression_norm.energy, impression_norm.liveness, impression_norm.loudness, impression_norm.speechiness, impression_norm.tempo, impression_norm.valence) AS score FROM music, impression_norm WHERE music.name = '{}' AND music.artist = '{}' ORDER BY score ASC;".format(name, artist))
        n = cur.fetchall()
        conn.commit()

    else:
        cur.execute("SELECT impression_norm.word, distance(music.danceability, music.acousticness, music.energy, music.liveness, music.loudness, music.speechiness, music.tempo, music.valence, impression_norm.danceability, impression_norm.acousticness, impression_norm.energy, impression_norm.liveness, impression_norm.loudness, impression_norm.speechiness, impression_norm.tempo, impression_norm.valence) AS score FROM music, impression_norm WHERE music.name = '{}' ORDER BY score ASC".format(name))
        n = cur.fetchall()
        conn.commit()
    print()
    if len(l_name) > 1:
        print(name, artist)
    else:
        print(l_name)
    for n_ in n:
        print(n_)
    print()
    cur.close()
    conn.close()

    return