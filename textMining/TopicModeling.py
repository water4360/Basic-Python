import myTextMining as tm
from konlpy.tag import Okt
import gensim
import gensim.corpora as corpora


def getNounsList(input_list):
    noun_list = []
    okt = Okt()

    for sent in input_list:
        noun_list.append(okt.nouns(sent))
    return noun_list


def prepareData(filename, field, keyword):
    target_list = tm.loadSavedData_JSON(filename, field)
    clean_list = tm.cleanInputData(target_list)
    # noun_list = tm.getMostFreqNouns(clean_list, tm.const_wordFreqRange, keyword)
    noun_list = getNounsList(clean_list)
    return noun_list


def genModel_LDA(input_noun_list):
    dictionary = corpora.Dictionary(input_noun_list)
    corpus = [dictionary.doc2bow(word) for word in input_noun_list]
    k = 3
    lda_model = gensim.models.ldamulticore.LdaMulticore(corpus, iterations=12, num_topics=k, id2word=dictionary, passes=1, workers=10)
    return lda_model, dictionary, corpus




import pyLDAvis.gensim

def main():
    filename = '블루베리_news.json'
    # keyword = filename.split("_")[0]
    # 데이터 준비
    input_noun_list = prepareData(filename, 'description', '블루베리')
    # 모델 구축
    # corpus = genModel_LDA(input_noun_list)
    # 모델 학습
    lda_model, dictionary, corpus = genModel_LDA(input_noun_list)
    result = lda_model.print_topics(num_topics=3, num_words=10)
    for cluster in result:
        print(cluster)
    # 학습모델로 분석
    pass
    # 시각화
    lda_vis = pyLDAvis.gensim.prepare(lda_model, corpus, dictionary)
    pyLDAvis.display(lda_vis)


if __name__ == '__main__':
    main()