





file_path = 'test.txt'  # テキストファイルのパスを適切に指定してください

# ファイルを開いて中のデータを読み込む
with open(file_path, 'r') as file:
    lines = file.readlines()

# 改行文字を取り除いてリストに格納
data_list = [line.strip() for line in lines]

# 結果を表示
print(data_list)


# サンプルテキストデータ
sample_text = "あいうえお\u3000This is a <p>sample</p> text. これはサンプルテキストです。\u3000<p>More text.</p>"

# \u3000と<p>を空文字列に置き換える
cleaned_text = data_list[0].replace('\u3000', '').replace('<p>', '').replace('</p>', '')

# 結果を表示
print(cleaned_text)
'''
<p><p> 2行の改行
<p>    改行
\u3000 空白全角１っこ


import MeCab


mecab = MeCab.Tagger("-Owakati")  # 分かち書きのみを出力する設定

result = mecab.parse(cleaned_text)
print(result)
'''