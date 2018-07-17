import re
import math


def bigram_letter_count(text):
    bigram_letter = re.findall(r'(?=(\w{2}))', text)
    bigram_letter_count = {}
    for item in bigram_letter:
        if item in bigram_letter_count:
            bigram_letter_count[item] += 1
        else:
            bigram_letter_count[item] = 1
    return bigram_letter_count


def single_letter_count(text):
    single_letter = re.findall(r'\w', text)
    single_letter_count = {}
    for item in single_letter:
        if item in single_letter_count:
            single_letter_count[item] += 1
        else:
            single_letter_count[item] = 1
    return single_letter_count


def cal_probability(test, bigram, single):
    p = 1
    for item in test:
        if(item[0] not in single and re.compile(r'[^0-9]').match(item[0])):
            return 0

        if(item in bigram):
            p = p * bigram[item] / single[item[0]]
    return p


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

# bigram letter count and single letter count
eng_bigram_letter = bigram_letter_count(eng_text)
eng_single_letter = single_letter_count(eng_text)

french_bigram_letter = bigram_letter_count(french_text)
french_single_letter = single_letter_count(french_text)

german_bigram_letter = bigram_letter_count(german_text)
german_single_letter = single_letter_count(german_text)

with open('BigramLetterLangId.out', 'w') as f:
    f.write('ID LANG\n')

h_en = 0
h_fr = 0
h_gr = 0

with open('BigramLetterLangId.out', 'a') as f:
    for i in range(len(test_text)):
        test_bigram = re.findall(r'(?=(\w{2}))', test_text[i])
        test_eng_pro = cal_probability(
            test_bigram, eng_bigram_letter, eng_single_letter)
        test_french_pro = cal_probability(
            test_bigram, french_bigram_letter, french_single_letter)
        test_german_pro = cal_probability(
            test_bigram, german_bigram_letter, german_single_letter)

        if test_eng_pro != 0:
            h_en += -1 * test_eng_pro * math.log2(test_eng_pro)
        if test_french_pro != 0:
            h_fr += -1 * test_french_pro * math.log(test_french_pro, 2)
        if test_german_pro != 0:
            h_gr += -1 * test_german_pro * math.log(test_german_pro, 2)

        if(test_eng_pro > test_french_pro and test_eng_pro > test_german_pro):
            f.write(str(i + 1) + " EN\n")
        elif(test_french_pro > test_eng_pro and test_french_pro > test_german_pro):
            f.write(str(i + 1) + " FR\n")
        elif(test_german_pro > test_eng_pro and test_german_pro > test_french_pro):
            f.write(str(i + 1) + " GR\n")
        else:
            f.write(str(i + 1) + " ERROR\n")


pp_en = 2**h_en
pp_fr = 2**h_fr
pp_gr = 2**h_gr

