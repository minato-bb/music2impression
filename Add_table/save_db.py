import psycopg2

#重複を避けてDBに保存
def save_df(df):
    conn = psycopg2.connect("host=" + "localhost" +
                           " dbname=" + "fc" +
                           " user=" + "babaminato" +
                           " password=" + "")
    cur = conn.cursor()
    for text in df.values:
        values = (text[0], text[1], text[2], text[3], text[4], text[5], text[6], text[7], text[8], text[9])
        
        cur.execute('SELECT * FROM music WHERE name = %s AND artist = %s', (text[0], text[1]))
        record = cur.fetchone()
        if record is not None:
            continue
        else:
            try:
                cur.execute ('INSERT INTO music (name, artist, danceability, acousticness, energy, liveness, loudness, speechiness, tempo, valence)' 'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)' ,values)
            except Exception as err:
                print("Encountered exception. {}".format(err))

        conn.commit()

    cur.execute("SELECT * FROM music")
    m = cur.fetchall()
    conn.commit()
    print("The number of music is ", len(m))
    cur.close()
    conn.close()