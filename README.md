## 機能
* 印象を入力することでその印象に合った楽曲の提示
* 楽曲名を入力することでその曲の印象を提示


## 必要ライブラリ
* pandas
* spotipy       (Spotify APIを取り扱う)
* spycopg2      (pythonでpostgresqlを取り扱う)


## 実行方法
1. Spotify APIの登録をする
1. sqlファイルを3つ実行する
2. spotifyから楽曲情報を取得する
```
python add_table.py add_table -i 'id'
```

4. ターミナルで以下の文を実行(印象語から検索するときは上、楽曲の印象を調べたいときは下)
```
python main_norm.py music_impression -i '印象語'
```
```
python main_norm.py music_impression -i '楽曲名'
```
### 印象語の候補
* cool
* sad
* excited
* relax
* fierce
