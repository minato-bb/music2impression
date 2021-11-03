## 機能
* 印象を入力することでその印象に合った楽曲の提示
* 楽曲名を入力することでその印象を提示


## 必要ライブラリ
* pandas
* spotipy       (Spotify APIを取り扱う)
* spycopg2      (pythonでpostgresqlを取り扱う)


## 実行方法
* ターミナルで以下の文を実行(印象語から検索)
```
python main_norm.py music_impression -i '印象語'
```
* ターミナルで以下の文を実行(楽曲の印象検索)
```
python main_norm.py music_impression -i '楽曲名'
```
### 印象語の候補
* cool
* sad
* excited
* relax
* fierce
