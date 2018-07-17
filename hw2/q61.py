# input result from q2-q5
q2 = []
with open('BigramLetterLangId.out', encoding="utf-8") as f:
    for line in f:
        q2.append(line.lstrip('0123456789 '))

q3 = []
with open('BigramWordLangId-AO.out', encoding="utf-8") as f:
    for line in f:
        q3.append(line.lstrip('0123456789 '))

q4 = []
with open('BigramWordLangId-GT.out', encoding="utf-8") as f:
    for line in f:
        q4.append(line.lstrip('0123456789 '))

q5 = []
with open('TrigramWordLangId-KBO.out', encoding="utf-8") as f:
    for line in f:
        q5.append(line.lstrip('0123456789 '))

# input test file
test = []
with open('LangID.gold.txt', encoding="utf-8") as f:
    for line in f:
        test.append(line.lstrip('0123456789. '))

# output the accuracy
q2_correct = 0
q3_correct = 0
q4_correct = 0
q5_correct = 0

for i in range(len(test) - 1):
    if(q2[i + 1] == test[i + 1]):
        q2_correct += 1
    if(q3[i + 1] == test[i + 1]):
        q3_correct += 1
    if(q4[i + 1] == test[i + 1]):
        q4_correct += 1
    if(q5[i + 1] == test[i + 1]):
        q5_correct += 1

print("BigramLetterLandId: " + str(q2_correct / len(test) * 100) + "%")
print("BigramWordLangId-AO: " + str(q3_correct / len(test) * 100) + "%")
print("BigramWordLangId-GT: " + str(q4_correct / len(test) * 100) + "%")
print("TrigramWordLangId-KBO: " + str(q5_correct / len(test) * 100) + "%")


# confusion matrix
def confusion_matrix(input, test):
    en_fr = 0
    en_gr = 0
    fr_en = 0
    fr_gr = 0
    gr_en = 0
    gr_fr = 0

    for i in range(len(test) - 1):
        if(input[i + 1] != test[i + 1]):
            if(input[i + 1] == "EN\n" and test[i + 1] == "FR\n"):
                en_fr += 1
            elif(input[i + 1] == "EN\n" and test[i + 1] == "GR\n"):
                en_gr += 1
            elif(input[i + 1] == "FR\n" and test[i + 1] == "EN\n"):
                fr_en += 1
            elif(input[i + 1] == "FR\n" and test[i + 1] == "GR\n"):
                fr_gr += 1
            elif(input[i + 1] == "GR\n" and test[i + 1] == "EN\n"):
                gr_en += 1
            elif(input[i + 1] == "GR\n" and test[i + 1] == "FR\n"):
                gr_fr += 1
    return en_fr, en_gr, fr_en, fr_gr, gr_en, gr_fr


def percentage(a, b):
    if(a == 0 and b == 0):
        return 0
    else:
        return a / (a + b) * 100


def print_result(name, result):
    print(name)
    print("None" + " " + str(percentage(result[0], result[1])) +
          "%" + " " + str(percentage(result[1], result[0])) + "%")
    print(str(percentage(result[2], result[3])) + "%" +
          " None " + str(percentage(result[3], result[2])) + "%")
    print(str(percentage(result[4], result[5])) + "%" +
          " " + str(percentage(result[5], result[4])) + "% None")


print_result("BigramLetter", confusion_matrix(q2, test))
print_result("BigramWordLangId-AO", confusion_matrix(q3, test))
print_result("BigramWordLangId-GT", confusion_matrix(q4, test))
print_result("TrigramWordLangId-KBO", confusion_matrix(q5, test))

###
