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
2. sqlファイルを2つ実行する
3. spotifyから楽曲情報を取得する(idはURLの末尾)
```
python add_table.py add_table -i 'id'
```
4. 画像ファイルをData/Img/frameに保存
5. ターミナルで以下の文を実行
```
python main.py
```
## 処理内容
1. 画像から色情報を取得する
2. 配色イメージスケールを参考に画像の色情報と合致する印象語(画像印象語)を選定する
3. 画像印象語と、8つの楽曲印象語のWord2vecによりその画像の楽曲特徴量を算出する
4. ３の楽曲特徴と最も距離が近い特徴を持つ楽曲を推薦、プレイリスト化
