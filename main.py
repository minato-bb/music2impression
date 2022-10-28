from Movie2impression import movie2imp, movie_frame
from Word2vec import word2vec
from Impression2music import main_norm

def main():
    #動画から印象語を選定
    word = movie2imp.movie2impression()

    print("画像の印象語", word)

    #Word2vec
    b = word2vec.vector(word)

    return main_norm.music_impression(b) #印象語から音楽を推薦

# psql -U babaminato -A -F, -c "select music, artist from music" fc > /Users/babaminato/music2impression/Data/csv/music.csv
# COPY music (name, artist) TO '/Users/babaminato/music2impression/Data/csv/music.csv' WITH encoding 'UTF8' CSV;
# =QUERY(music!A:B,"where B='"&G3&"'",true)
# =QUERY(music!A:B,"where A='"&D3&"'",true)