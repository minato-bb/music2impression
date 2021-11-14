from gensim.models import word2vec
import pandas as pd

def vector(word):
    df = pd.read_csv("/Data/csv/color_img_scale.csv")
    color_imp = []
    for i in df["Unnamed: 0"]:
        color_imp.append(i)

    music_imp = ["強調された", "雄大な", "武骨な", "活気のある", "堅牢な", "活発な", "興奮した", "刺激的な", "勢いのある", "情熱的な", "扇情的な", "高揚した", "明るい", "陽気な", "快活な", "幸福な", "朗らかな", "楽しい", "繊細な", "空想的な", "優美な", "趣のある", "幻想的な", "穏やかな", "ゆったりとした", "叙情的な", "静かな","落ち着いた", "やわらげる", "平静な", "素敵な", "憧れ", "思慕", "暗い","憂鬱な", "悲惨な", "挫折した", "喪に服した", "哀れな", "悲しい", "悲劇的な", "荘厳な", "威厳のある", "高尚な", "神聖な", "由々しい", "謹直な", "厳粛な", "気高い"]

    sentence = [color_imp, music_imp]
    model_music = word2vec.Word2Vec(sentence,vector_size=170,min_count=1)

    value = -1.0
    for i in music_imp:
        if model_music.wv.similarity(word, i) > value:
            value = model_music.wv.similarity(word, i)
            name = i

    return name