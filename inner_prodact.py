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

    cur.execute("SELECT name, artist FROM music_normalization WHERE name = '{}'".format(name))
    l_name = cur.fetchall()
    conn.commit()
    if len(l_name) > 1:
        for n in l_name:
            print(n)
        artist = input('アーティスト名')
        cur.execute("SELECT impression.word, inner_product(music_normalization.danceability, music_normalization.acousticness, music_normalization.energy, music_normalization.liveness, music_normalization.loudness, music_normalization.speechiness, music_normalization.tempo, music_normalization.valence, impression.danceability, impression.acousticness, impression.energy, impression.liveness, impression.loudness, impression.speechiness, impression.tempo, impression.valence) AS score FROM music_normalization, impression WHERE music_normalization.name = '{}' AND music_normalization.artist = '{}' ORDER BY score DESC;".format(name, artist))
        n = cur.fetchall()
        conn.commit()

    else:
        cur.execute("SELECT impression.word, inner_product(music_normalization.danceability, music_normalization.acousticness, music_normalization.energy, music_normalization.liveness, music_normalization.loudness, music_normalization.speechiness, music_normalization.tempo, music_normalization.valence, impression.danceability, impression.acousticness, impression.energy, impression.liveness, impression.loudness, impression.speechiness, impression.tempo, impression.valence) AS score FROM music_normalization, impression WHERE music_normalization.name = '{}' ORDER BY score DESC".format(name))
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