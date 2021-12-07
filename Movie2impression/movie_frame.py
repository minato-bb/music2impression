import cv2
import os
from tqdm import tqdm

#動画から画像を取得
def split_frames():
    TARGET_DIR ='/Data/Movie'
    dir_name = os.listdir(TARGET_DIR)

    for i in dir_name:
        target_movie = TARGET_DIR + "/" + i
        if i == '.DS_Store':
            continue
        else:
            cap = cv2.VideoCapture(target_movie)

    if not cap.isOpened():#動画の読み込み判定
        return

    basename="img"
    NEW_DIR='/Data/Img/frame'
    os.makedirs(NEW_DIR, exist_ok=True)
    base_path = os.path.join(NEW_DIR, basename)
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    n_ = 0
    ext='jpg'
    print("フレーム分割")
    for n in tqdm(range(0, int(cap.get(cv2.CAP_PROP_FRAME_COUNT)), round(fps/10))):
        cap.set(cv2.CAP_PROP_POS_FRAMES, n)
        ret, frame = cap.read()
        if ret:
            cv2.imwrite('{}_{}.{}'.format(base_path, n_, ext), frame)
            n_+=1
        else:
            return