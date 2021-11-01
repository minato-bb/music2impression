import psycopg2
#テーブル作成
def create_music_table():
    conn = psycopg2.connect("host=" + "localhost" +
                           " dbname=" + "fc" +
                           " user=" + "babaminato" +
                           " password=" + "")
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS music (name TEXT NOT NULL, artist TEXT NOT NULL, danceability FLOAT8 NOT NULL,acousticness FLOAT8 NOT NULL,energy FLOAT8 NOT NULL,liveness FLOAT8 NOT NULL,loudness FLOAT8 NOT NULL,speechiness FLOAT8 NOT NULL,tempo FLOAT8 NOT NULL,valence FLOAT8 NOT NULL);')
    cur.execute('CREATE TABLE IF NOT EXISTS music_normalization (name TEXT NOT NULL, artist TEXT NOT NULL, danceability FLOAT8 NOT NULL,acousticness FLOAT8 NOT NULL,energy FLOAT8 NOT NULL,liveness FLOAT8 NOT NULL,loudness FLOAT8 NOT NULL,speechiness FLOAT8 NOT NULL,tempo FLOAT8 NOT NULL,valence FLOAT8 NOT NULL);')
    conn.commit()
    cur.close()
    conn.close()
    return 