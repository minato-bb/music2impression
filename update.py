import pandas as pd
import psycopg2

def update(im_word, m_name, m_artist):
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
    fig = df_sql.loc[im_word]
    for i in m:
        for data in i:
            target.append(data)
    
    data =target[2:]
    update = (data + fig)/2

    cur.execute("update test_update set danceability={}, acousticness={}, energy={}, liveness={}, loudness={}, speechiness={}, tempo={}, valence={} where word='{}'".format(update[0], update[1], update[2], update[3], update[4], update[5], update[6], update[7], imp_word))
    conn.commit()
    cur.close()
    conn.close()
    
    return