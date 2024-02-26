

file_path = ''  # テキストファイルのパスを適切に指定してください

# ファイルを開いて中のデータを読み込む
with open(file_path, 'r') as file:
    lines = file.readlines()

cleaned_text = lines[0].replace('   ', ' ')#.replace('\n', '')
print(cleaned_text)
