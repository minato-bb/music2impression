## 機能
* Data/Img/frameに画像を入れるとその画像の印象に合致した楽曲の推薦


## 必要ライブラリ
* pandas
* spotipy       (Spotify APIを取り扱う)
* spycopg2      (pythonでpostgresqlを取り扱う)
* gensim        (word2vecを取り扱う)
* opencv-python (画像処理を取り扱う)
* tqdm          (for文の進行度を可視化)


## 実行方法
1. Spotify APIの登録をする
1. sqlファイルを2つ実行する
2. spotifyから楽曲情報を取得する(idはURLの末尾)
```
python add_table.py add_table -i 'id'
```
3. 画像ファイルをData/Img/frameに保存
4. ターミナルで以下の文を実行
```
python main.py
```

