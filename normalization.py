import psycopg2
import pandas as pd
from sqlalchemy import create_engine
from sklearn.preprocessing import MinMaxScaler

def normal():
    conn = psycopg2.connect("host=" + "localhost" +
                        " dbname=" + "fc" +
                        " user=" + "babaminato" +
                        " password=" + "")
    cur = conn.cursor()
    df = pd.read_sql(sql='SELECT * FROM music', con=conn)

    df_value = df.drop(["name", "artist"], axis = 1)
    df_name = df.drop(["danceability", "acousticness", "energy", "liveness" ,"loudness", "speechiness", "tempo", "valence"], axis = 1)

    # df_ = (df_value - df_value.mean()) / df_value.std()
    scaler = MinMaxScaler()
    df_value.loc[:,['loudness', 'tempo']] = scaler.fit_transform(df_value[['loudness', 'tempo']]) # loudness, tempoを正規化
    df_normal = pd.concat([df_name, df_value], axis = 1)

    engine=create_engine("postgresql://babaminato@localhost:5432/fc")
    df_normal.to_sql("music_normalization", engine, if_exists = "replace", index = False)

    conn.commit()
    cur.close()
    conn.close()
    return
normal()