
import os
import re
import bs4
import time
import requests
import pprint

def load(url):
    res = requests.get(url)
    res.raise_for_status()

    return res.text

def pickup_tag(html, find_tag):
    soup = bs4.BeautifulSoup(str(html), 'html.parser')
    paragraphs = soup.find_all(find_tag)

    return paragraphs

def parse(html):
    soup = bs4.BeautifulSoup(str(html), 'html.parser')
    # htmlタグの排除
    kashi_row = soup.getText()
    kashi_row = kashi_row.replace('\n', '')
    kashi_row = kashi_row.replace('　', '')

    # 英数字の排除
    kashi_row = re.sub(r'[a-zA-Z0-9]', '', kashi_row)
    # 記号の排除
    kashi_row = re.sub(r'[ ＜＞♪`‘’“”・…_！？!-/:-@[-`{-~]', '', kashi_row)
    # 注意書きの排除
    kashi = re.sub(r'注意：.+', '', kashi_row)

    return kashi


def extract_text_from_string(text, start_string, end_string):
    start_index = text.find(start_string)
    if start_index == -1:
        print(f"指定された開始文字列 '{start_string}' が見つかりませんでした。")
        return None

    end_index = text.find(end_string, start_index)
    if end_index == -1:
        print(f"指定された終了文字列 '{end_string}' が見つかりませんでした。")
        return None

    extracted_text = text[start_index + len(start_string):end_index]
    return extracted_text

start_string = '<div class="lyric_text"><p>'
end_string = '</p></p></p>'


site_url='https://linkco.re/t667vaEg/songs/2472069/lyrics'

# 曲のurlを格納
musics_url = []
musics_url.append(site_url)



""" 歌詞の取得 """
for i, page in enumerate(musics_url):

    html = load(page)
    for div in pickup_tag(html, 'div'):

        div = str(div)
        result = extract_text_from_string(div, start_string, end_string)
        if result is not None:
            #print(result)
            #print('')
            cleaned_text = result.replace('\u3000', ' ').replace('<p><p>', ' ').replace('<p>', ' ')
            #cleaned_text = result.replace('\u3000', ' ').replace('<p>', ' ').replace('<p><p>', ' ')
            print(cleaned_text)
            break







