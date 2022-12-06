from gensim.models import word2vec
import pandas as pd
import numpy as np
import psycopg2

def vector(word):   
    conn = psycopg2.connect("host=" + "localhost" +
                            " dbname=" + "fc" +
                            " user=" + "babaminato" +
                            " password=" + "")
    cur = conn.cursor()
    # query = 'SELECT * FROM impression_norm_test'
    query = 'SELECT * FROM impression_norm'
    df_sql = pd.read_sql(query, con=conn)
    # a = df_sql.values
    a = df_sql.values
    cur.close()
    conn.close()

    #追加
    a = a[:, 1:]

    
    df = pd.read_csv("/Users/babaminato/fc/color_image_rgb.csv")
    color_imp = []
    for i in df["Unnamed: 0"]:
        color_imp.append(i)

    #music_wordの説明
    music_imp = ["威厳のある", "悲しい", "哀愁のある", "落ち着いた", "優美な", "楽しい", "興奮する", "活発な"]

    sentence = [color_imp, music_imp]
    model_music = word2vec.Word2Vec(sentence, vector_size=20,min_count=1)

    weight = np.array([])
    for i in music_imp:
        weight = np.append(weight, (model_music.wv.similarity(word, i)))

    print(weight)

    b = np.dot(a.T, weight)

    if b[0] < 0:
        return  -b
    else:
        return b

# [(0.04467906740307809, 0.14242708527045247, 0.1345008647814393, 0.08660954502969981, -3.7936308509148655, 0.0391709207765758, 46.130823979165406, 0.08325808453187347)]
# [(0.1155834000146352, 0.07876717341495679, 0.24518633176672827, 0.07037606541262939, -2.624249384018492, 0.03513276758582145, 43.48652869001342, 0.13688834313264492)]

# [(0.30171701587364075, 0.06492145093617105, 0.48132356189191344, 0.18904566356912256, -4.33552010248974, 0.038917834040895105, 84.5349576842524, 0.32893616304174067)]
# [(0.3408668379007876, 0.16227822059748692, 0.4907496361532286, 0.14360814248728754, -4.301975006203319, 0.050890390936892474, 84.73431106293819, 0.31547497991915424)]
