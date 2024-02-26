

file_path = '/home/neosoleil/遊び/ベロティカ/歌詞分かち書き/覚醒butterfly.txt_tokenized.txt'  # テキストファイルのパスを適切に指定してください

# ファイルを開いて中のデータを読み込む
with open(file_path, 'r') as file:
    lines = file.readlines()

cleaned_text = lines[0].replace('   ', ' ')#.replace('\n', '')
print(cleaned_text)