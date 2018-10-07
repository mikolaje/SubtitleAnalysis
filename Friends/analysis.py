#coding=u8
from collections import Counter
import gensim
import io
import pandas as pd
from nltk import ngrams
import spacy
nlp = spacy.load('en', disable=['parser'])


all_word_list = []
sentences = []


def analysis_season(season):
    with io.open(r'filtered_subtitles/s%s/s%s_all.txt' % (season, season), 'r', encoding='u8') as f:
        for line in f:
            zh, en = line.split('\b0\b1\b2---')

            all_word_list.extend(en.split(' '))
            word_list = [i.lower().replace(',','').replace('.','').replace('?','').strip() for i in en.split(' ')]
            sentences.append(word_list)

    print(len(all_word_list))
    for index, word in enumerate(all_word_list):

        word = word.strip().replace(',','').replace('.','').replace('?','').lower()
        all_word_list[index] = word
        if '-' == word:
            del all_word_list[index]


lemma_list = []
def analyze_wc_season(season):

    with io.open(r'filtered_subtitles/s%s/s%s_all.txt' % (season, season), 'r', encoding='u8') as f:
        for line in f:
            zh ,en = line.split('\b0\b1\b2---')
            doc = nlp(en)
            for token in doc:
                if token.is_stop == False and token.is_punct == False and token.is_space == False:
                    lemma_list.append(token.lemma_)

    cnt = Counter(lemma_list)
    # print(cnt.most_common(100))
    return cnt


def analyze_wc_all():
    episode_list = [format(i, '02d') for i in range(1, 11)]
    cnt = Counter()
    for each in episode_list:
        cnt_each = analyze_wc_season(each)
        cnt = cnt+cnt_each
    print(cnt.most_common(100))


def analyze_ngram_season(season):
    words_list = []
    with io.open(r'filtered_subtitles/s%s/s%s_all.txt' % (season, season), 'r', encoding='u8') as f:
        for line in f:
            zh, en = line.split('\b0\b1\b2---')
            doc = nlp(en)
            for token in doc:
                if token.is_stop == True and token.is_punct == False and token.is_space == False:
                    words_list.append(token.text.lower())
    ngrams_result = ngrams(words_list, 4)
    cnt = Counter(ngrams_result)
    print('season: %s '%season)
    print(cnt.most_common(50))
    return cnt


def analyze_ngram_all():
    episode_list = [format(i, '02d') for i in range(1, 11)]
    cnt = Counter()
    for each in episode_list:
        cnt_each = analyze_ngram_season(each)
        cnt = cnt+cnt_each
    print('all season result')
    print(cnt.most_common(100))


if __name__ == '__main__':
    """
    episode_list = [format(i, '02d') for i in range(1, 10)]
    for each in episode_list:
        analysis_season(each)
    cnt = Counter(all_word_list)
    #cnt = {k:v for k,v in cnt.iteritems() if v > 5}
    print(cnt.most_common(1000))
    """

    # analyze_by_spacy('03')
    # analyze_wc_all()
    # analyze_ngram_season('01')
    analyze_ngram_all()


