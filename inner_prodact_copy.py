import psycopg2

def inner_product(name):
    conn = psycopg2.connect("host=" + "localhost" +
                            " dbname=" + "fc" +
                            " user=" + "babaminato" +
                            " password=" + "")
    cur = conn.cursor()
    cur.execute("SELECT * FROM music_normalization")
    m = cur.fetchall()
    conn.commit()
    print("The number of music is ", len(m))
    conn.commit()
    cur.execute("SELECT music_normalization.name, music_normalization.artist, inner_product(music_normalization.danceability, music_normalization.acousticness, music_normalization.energy, music_normalization.liveness, music_normalization.loudness, music_normalization.speechiness, music_normalization.tempo, music_normalization.valence, impression.danceability, impression.acousticness, impression.energy, impression.liveness, impression.loudness, impression.speechiness, impression.tempo, impression.valence) AS score FROM music_normalization, impression WHERE impression.word = '{}' ORDER BY score DESC FETCH FIRST 10 ROWS ONLY".format(name))
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