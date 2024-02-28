
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import MeCab
import gensim
from gensim import corpora, models, similarities
import ipadic

def token(text_list,wvs):
    CHASEN_ARGS = r' -F "%m\t%f[7]\t%f[6]\t%F-[0,1,2,3]\t%f[4]\t%f[5]\n"'
    CHASEN_ARGS += r' -U "%m\t%m\t%m\t%F-[0,1,2,3]\t\t\n"'
    t = MeCab.Tagger(ipadic.MECAB_ARGS + CHASEN_ARGS)
    for text in text_list:
        pos = t.parseToNode(text)
        word_vector = []
        while pos:
            if "名詞" in pos.feature:
                if "数" not in pos.feature and "非自立" not in pos.feature and "接尾" not in pos.feature and "代名詞" not in pos.feature:
                    word_vector += [pos.surface]
            pos = pos.next
        wvs += [word_vector]
    return text_list

def get_topic(wvs):
    #print(wvs)
    # 辞書作成
    dictionary = corpora.Dictionary(wvs)
    #dictionary.filter_extremes(no_below=2, no_above=0.3)
    dictionary.save_as_text('dict.txt')
    # コーパスを作成
    corpus = [dictionary.doc2bow(text) for text in wvs]
    corpora.MmCorpus.serialize('cop.mm', corpus)
    # 辞書(dict.txt)を読み込んで、コーパス(cop.mm)を作成
    dictionary = gensim.corpora.Dictionary.load_from_text('dict.txt')
    corpus = corpora.MmCorpus('cop.mm')
    # LDAの実行
    topic_N = 6
    lda = gensim.models.ldamodel.LdaModel(corpus=corpus, num_topics=topic_N, id2word=dictionary)
    return lda, corpus


def read_file(filename):
    data = []
    stopwords = [""]
    with open(filename, 'r') as f:
      text = f.read()
    word_list = text.split()

    return word_list


def check_lda(lda, corpus):
    for topics_per_document in lda[corpus]:
        high_topic_score = 0.0
        for topic in topics_per_document:
            topic_index = topic[0]
            topic_score = topic[1]
            if topic_score > high_topic_score:
                high_topic_score = topic_score
                high_topic_index = topic_index

def word_cloud(lda, corpus):
    plt.figure(figsize=(20,20))
    for t in range(lda.num_topics):
        plt.subplot(4,3,t+1)
        x = dict(lda.show_topic(t, 50))
        fpath = "SourceHanSansJP-Normal.otfへのPATH"
        im = WordCloud(background_color="white",font_path=fpath, width=900, height=500).generate_from_frequencies(x)
        plt.imshow(im)
        plt.axis("off")
        plt.title("Topic_" + str(t))
    plt.show()


if __name__ == '__main__':
    wvs = []
    filename = '歌詞を1つにまとめたテキストファイルへのPATH'
    data = read_file(filename)
    token_jpn = token(data,wvs)
    lda, corpus = get_topic(wvs)
    check_lda(lda, corpus)
    word_cloud(lda, corpus)
