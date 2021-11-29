import numpy as np
import pandas as pd
from pandas import plotting
from scipy.spatial import distance
import os
import cv2

def movie2impression():
    color_image_scale = pd.read_csv("Data/csv/color_img_scale.csv", index_col="Unnamed: 0")
    color_ = pd.read_csv('Data/csv/color.csv', index_col='Hue/Tone')
    color = color_.drop(["color","h", "s", "v", "L", "a", "b"], axis =1)

    image_path = "Data/Img/"
    dir_name = os.listdir(image_path)

    target_dir ='Data/Img/frame/'
    v = os.listdir(target_dir)

    movie_image = []#フレーム毎に最も割合の多い3色

    for n in range(len(v)-1):
        num1 = 0
        num2 = 0
        num3 = 0

        f1 = []
        f2 = []
        f3 = []

        #ターゲット画像
        target_file = "img_{}.jpg".format(n)
        target_img_path = target_dir + target_file

        #画像読み込み
        img_ = cv2.imread(target_img_path)

        
        #resize
        def scale_to_width(img, width):
            h, w = img.shape[:2]
            height = round(h * (width / w))
            dst = cv2.resize(img, dsize=(width, height))

            return dst
        img = scale_to_width(img_, 70)

        #RGB値化
        target_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        h, w, c = target_img.shape
        reshaped_rgb_array = target_img.reshape(h * w, 3)
        unique_rgb_array = np.unique(reshaped_rgb_array, axis = 0)
        rgb = reshaped_rgb_array.tolist()


        #ピクセルRGB値をdf化
        pixel_dic = []
        for i in rgb:
            f = {"R":i[0], "G":i[1], "B":i[2]}
            pixel_dic.append(f)
        df = pd.DataFrame(pixel_dic)


        #130色から最も近い色を算出
        pixel = []
        for i in range(0, len(df)):
            pixel_dict = {n : np.linalg.norm(df.iloc[i] - color.iloc[n]) for n in range(0, len(color))}
            pixel.append(min(pixel_dict, key=pixel_dict.get))


        #130色のうち最も近い色に置換
        for num, i in enumerate(pixel):
            df.iloc[num] = color.iloc[i]

        #置換後のdf設定
        unique_rgb_array = np.unique(df, axis = 0)
        rgb = df.values.tolist()#全ピクセルRGB値
        rgb_u = unique_rgb_array.tolist()#重複なしRGB値

        #割合の多い3色を決定
        for i in rgb_u:
            c = rgb.count(i)
            if c >= num1 >= num2 >= num3:
                f3 = f2
                f2 = f1
                f1 = i
                num3 = num2
                num2 = num1
                num1 = c
            elif num1 >= c >= num2 >= num3:
                f3 = f2
                f2 = i
                f1 = f1
                num3 = num2
                num2 = c
                num1 = num1
            elif num1 >= num2 >= c >= num3:
                f3 = i
                f2 = f2
                f1 = f1
                num3 = c
                num2 = num2
                num1 = num1
            else:
                continue

        rgb_list = [f1, f2, f3]
        movie_image.append(rgb_list)

        seen = []                
        rgb_u =  [x for x in movie_image if x not in seen and not seen.append(x)]
        rgb = movie_image

        #動画の中で最も割合の多い3色
        most_movie_color = []

        #割合の多い3色を決定
        for i in rgb_u:
            c = rgb.count(i)
            if c >= num1 >= num2 >= num3:
                f3 = f2
                f2 = f1
                f1 = i
                num3 = num2
                num2 = num1
                num1 = c
            elif num1 >= c >= num2 >= num3:
                f3 = f2
                f2 = i
                f1 = f1
                num3 = num2
                num2 = c
                num1 = num1
            elif num1 >= num2 >= c >= num3:
                f3 = i
                f2 = f2
                f1 = f1
                num3 = c
                num2 = num2
                num1 = num1
            else:
                continue

        rgb_list = [f1, f2, f3]
        for i in rgb_list:
            most_movie_color.append(i)
        
    #Hue/Toneを参考にカラーイメージスケールの印象を選定
    movie_HT = []
    flatten = lambda x: [z for y in x for z in (flatten(y) if hasattr(y, '__iter__') and not isinstance(y, str) else (y,))]

    for rgb in most_movie_color:
        color_item = color[(color['R'] == rgb[0]) & (color['G'] == rgb[1]) & (color["B"] == rgb[2])]
        movie_HT.append(color_item.index.tolist())
        
    movie_HueTone = flatten(movie_HT)
    color_item = color_image_scale[(color_image_scale[movie_HueTone[0]] == 1) & (color_image_scale[movie_HueTone[1]] == 1) & (color_image_scale[movie_HueTone[2]] == 1)]

    #動画の印象抽出
    movie_impression = color_item.index.tolist()
    return movie_impression