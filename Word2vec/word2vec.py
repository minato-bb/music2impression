from gensim.models import word2vec
import pandas as pd

def vector(word):
    df = pd.read_csv("/Users/babaminato/music2impression/color_img_scale.csv")
    color_imp = []
    for i in df["Unnamed: 0"]:
        color_imp.append(i)

    music_imp = ["威厳", "悲しい", "哀愁", "冷静", "優雅", "幸福", "興奮", "活発"]
    sentence = [color_imp, music_imp]
    model_music = word2vec.Word2Vec(sentence,vector_size=400,min_count=1)

    value = -1.0
    for i in music_imp:
        if model_music.wv.similarity(word, i) > value:
            value = model_music.wv.similarity(word, i)
            name = i

    return name