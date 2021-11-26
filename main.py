from Movie2impression import movie2imp, movie_frame
from Word2vec import word2vec
from Impression2music import main_norm

# #動画をフレーム毎に分けて保存
# movie_frame.split_frames()

#動画から印象語を選定
word = movie2imp.movie2impression()

#Word2vec
impression = word2vec.vector(word)

#印象語から音楽を推薦
main_norm.music_impression(impression)