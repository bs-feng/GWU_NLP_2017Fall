from nltk.tokenize import sent_tokenize, word_tokenize
import nltk
import math


def single_word_count(text):
    word_dict = {}
    for item in text:
        if item in word_dict:
            word_dict[item] += 1
        else:
            word_dict[item] = 1
    return word_dict


def bigram_word_count(text):
    word_list = []
    i = 0
    for i in range(len(text) - 1):
        word_list.append((text[i], text[i + 1]))

    word_dict = {}
    for item in word_list:
        if item in word_dict:
            word_dict[item] += 1
        else:
            word_dict[item] = 1
    return word_dict


# single sentence probability
def cal_sent_pro(sent, single, bigram):
    word_test = word_tokenize(sent)
    word_bigram_test = []
    i = 0
    for i in range(len(word_test) - 1):
        word_bigram_test.append((word_test[i], word_test[i + 1]))

    v = len(single)

    p = 1
    for item in word_bigram_test:
        if item[0] not in single:
            p = p * (1 / v)
        else:
            if item not in bigram:
                p = p * (1 / (single[item[0]] + v))
            else:
                p = p * ((bigram[item] + 1) / (single[item[0]] + v))
    return p

# test sentences probability


def cal_pro(test, single, bigram):
    sent = sent_tokenize(test)
    pro = 0
    for item in sent:
        pro += cal_sent_pro(item, single, bigram)
    return pro

# read and lowercase the file
f = open('HW2english.txt', encoding="utf-8")
eng_text = f.read().lower()
f.close()


f = open('HW2french.txt', encoding="utf-8")
french_text = f.read().lower()
f.close()

f = open('HW2german.txt', encoding="utf-8")
german_text = f.read().lower()
f.close()

test_text = []
with open('LangID.test.txt', encoding="utf-8") as f:
    for line in f:
        test_text.append(line.lstrip('0123456789. ').lower())

# tokenize words by nltk
en = word_tokenize(eng_text)
fr = word_tokenize(french_text)
gr = word_tokenize(german_text)

en_single_word = single_word_count(en)
fr_single_word = single_word_count(fr)
gr_single_word = single_word_count(gr)


# bigram
en_bigram_word = bigram_word_count(en)
fr_bigram_word = bigram_word_count(fr)
gr_bigram_word = bigram_word_count(gr)

# idendify language
with open('BigramWordLangId-AO.out', 'w') as f:
    f.write('ID LANG\n')

h_en = 0
h_fr = 0
h_gr = 0

with open('BigramWordLangId-AO.out', 'a') as f:
    for i in range(len(test_text)):
        test_en_pro = cal_pro(test_text[i], en_single_word, en_bigram_word)
        test_fr_pro = cal_pro(test_text[i], fr_single_word, fr_bigram_word)
        test_gr_pro = cal_pro(test_text[i], gr_single_word, gr_bigram_word)

        if test_en_pro != 0:
            h_en += -1 * test_en_pro * math.log(test_en_pro, 2)
        if test_fr_pro != 0:
            h_fr += -1 * test_fr_pro * math.log(test_fr_pro, 2)
        if test_gr_pro != 0:
            h_gr += -1 * test_gr_pro * math.log(test_gr_pro, 2)

        if(test_en_pro > test_fr_pro and test_en_pro > test_gr_pro):
            f.write(str(i + 1) + " EN\n")
        elif(test_fr_pro > test_en_pro and test_fr_pro > test_gr_pro):
            f.write(str(i + 1) + " FR\n")
        elif(test_gr_pro > test_en_pro and test_gr_pro > test_fr_pro):
            f.write(str(i + 1) + " GR\n")
        else:
            f.write(str(i + 1) + " ERROR\n")


pp_en = 2**h_en
pp_fr = 2**h_fr
pp_gr = 2**h_gr


