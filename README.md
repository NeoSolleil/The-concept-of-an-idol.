# The-concept-of-an-idol.

今まで気になっていたことを色々試してみたのですが、どこにも見せる場がないので、ここに記そうと思います。  
詳しくはQiitaに書きました  
https://qiita.com/NeoSoleil/items/23589d83900266b1f824

# 以下はコードの説明です

# linkco_kasi_toridasi.py
歌詞をネットから取得するためのスクレイピングのコードです。  
  
  56行目の  
```site_url='https://linkco.re/t667vaEg/songs/2472069/lyrics'```  
の部分を適宜変えてください。  
このコードでは、「超NEW WORLD」という曲の歌詞を取得するコードになっています。  

# wakati_sudachi.py
linkco_kasi_toridasi.pyで取得した歌詞を分かち書きするためのコードです。  
  
30，31行目の  
```input_folder_path = 'linkco_kasi_toridasi.pyで生成したテキストファイルが入っているフォルダのPATH'```  
```output_folder_path = '分かち書きをしたテキストファイルを保存するフォルダのPATH'```  
の部分を適宜変えてください。  

# kuhaku_3wo1.py
wakati_sudachi.pyで分かち書きしたテキストファイルの中で半角の空白が3つ付く部分があるので、それを半角1つの空白に置き換えるコードです。  
  
3行目の  
```file_path = 'wakati_sudachi.pyで分かち書きしたテキストへのPATH'  # テキストファイルのパスを適切に指定してください```  
の部分を適宜変えてください。  


# word_cloud.py
LDAを用いてトピックモデルを生成し、ワードクラウドを生成するコードです。  
  
67行目の  
```fpath = "SourceHanSansJP-Normal.otfへのPATH"```  
「SourceHanSansJP-Normal.otf」は同じディレクトリに置いてあります。  
77行目の  
```filename = '歌詞を1つにまとめたテキストファイルへのPATH'```  
の部分を適宜変えてください。  
  
トピック数を変更したい場合は37行目の  
```topic_N = 6```  
の部分を変えてください。  

# 
