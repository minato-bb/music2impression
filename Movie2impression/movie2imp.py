import numpy as np
import pandas as pd
from pandas import plotting
from scipy.spatial import distance
import os
import cv2
from tqdm import tqdm

def movie2impression():
    color_image_scale = pd.read_csv("Data/csv/color_image_rgb.csv", index_col="Unnamed: 0")
    color_ = pd.read_csv('Data/csv/color.csv', index_col='Hue/Tone')
    color = color_.drop(["color","h", "s", "v", "L", "a", "b"], axis =1)

    image_path = "templates/images/"
    dir_name = os.listdir(image_path)

    target_dir ='templates/images/'
    v = os.listdir(target_dir)
    
    movie_image = []#フレーム毎に最も割合の多い3色

    num1 = 0
    num2 = 0
    num3 = 0

    f1 = []
    f2 = []
    f3 = []

    #ターゲット画像
    target_file = os.listdir(target_dir)
    target_img_path = target_dir + target_file[0]

    #画像読み込み
    img_ = cv2.imread(target_img_path)

    
    #resize
    def scale_to_width(img, width):
        h, w = img.shape[:2]
        height = round(h * (width / w))
        dst = cv2.resize(img, dsize=(width, height))

        return dst
    img = scale_to_width(img_, 200)

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
    a = df.values
    b = color.values

    ia, ib = np.meshgrid(np.arange(a.shape[0]), np.arange(b.shape[0]))
    distance = np.linalg.norm(a[ia]-b[ib], axis=2)

    pixel = np.argmin(distance, axis=0)


    #130色のうち最も近い色に置換
    for num, i in tqdm(enumerate(pixel)):
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

    #画像の中で最も割合の多い3色
    most_img_color = []
    for i in rgb_list:
        most_img_color.append(i)


    #カラーイメージスケールの印象を選定
    n = 9999
    for num in range(len(color_image_scale)):
        norm = np.linalg.norm(most_img_color - color_image_scale.values.reshape(1170, 3, 3)[num])
        if norm < n:
            n = norm
            list_num = num
                
    #動画の印象抽出
    movie_impression = color_image_scale.index[list_num]

    return movie_impression