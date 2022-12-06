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
    query = 'SELECT * FROM impression_norm_test'
    df_sql = pd.read_sql(query, con=conn)
    a = df_sql.values
    print(a)
    cur.close()
    conn.close()

    
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

    # a = np.array([[0.398357, 0.655872, 0.42245, 0.160421, -12.044429, 0.066843, 107.533857, 0.3091],
    #                 [0.541389, 0.447167, 0.522511, 0.139822, -8.4815, 0.037811, 105.3725, 0.428417],
    #                 [0.493318, 0.404653, 0.534103, 0.189091, -7.749, 0.042405, 119.049182, 0.421559],
    #                 [0.547235, 0.429712, 0.470189, 0.155441, -9.610176, 0.048106, 116.012, 0.353512],
    #                 [0.414444, 0.522503, 0.43275, 0.1449, -11.775444, 0.040639, 111.909889, 0.3145],
    #                 [0.527143, 0.096779, 0.853857, 0.202486, -4.543429, 0.088233, 137.614333, 0.619476],
    #                 [0.44515, 0.100985, 0.84105, 0.24179, -4.9374, 0.08188, 136.87695, 0.492995],
    #                 [0.538909, 0.091223, 0.875727, 0.255255, -4.031773, 0.081364, 134.460545, 0.5379]])

    b = np.dot(a.T, weight)

    if b[0] < 0:
        return  -b
    else:
        return b

# [(0.04467906740307809, 0.14242708527045247, 0.1345008647814393, 0.08660954502969981, -3.7936308509148655, 0.0391709207765758, 46.130823979165406, 0.08325808453187347)]
# [(0.1155834000146352, 0.07876717341495679, 0.24518633176672827, 0.07037606541262939, -2.624249384018492, 0.03513276758582145, 43.48652869001342, 0.13688834313264492)]

# [(0.30171701587364075, 0.06492145093617105, 0.48132356189191344, 0.18904566356912256, -4.33552010248974, 0.038917834040895105, 84.5349576842524, 0.32893616304174067)]
# [(0.3408668379007876, 0.16227822059748692, 0.4907496361532286, 0.14360814248728754, -4.301975006203319, 0.050890390936892474, 84.73431106293819, 0.31547497991915424)]
