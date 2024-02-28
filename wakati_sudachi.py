import os
from sudachipy import tokenizer, dictionary

def tokenize_text(text):
    tokenizer_obj = dictionary.Dictionary().create()
    tokens = tokenizer_obj.tokenize(text)
    result = ' '.join([m.surface() for m in tokens])
    return result

def tokenize_files_in_folder(folder_path, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    tokenizer_obj = dictionary.Dictionary().create()

    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            output_path = os.path.join(output_folder, f"{filename}_tokenized.txt")

            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()

            tokens = tokenize_text(content)

            with open(output_path, 'w', encoding='utf-8') as output_file:
                output_file.write(tokens)

# 使用例
input_folder_path = 'linkco_kasi_toridasi.pyで生成したテキストファイルが入っているフォルダのPATH'
output_folder_path = '分かち書きをしたテキストファイルを保存するフォルダのPATH'

tokenize_files_in_folder(input_folder_path, output_folder_path)
