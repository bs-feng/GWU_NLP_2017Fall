import re

f = open('q4text.txt')
text = f.read()
f.close()
pattern = r'''[0-9]+[,][0-9]+|[0-9]+[.][0-9]+|[0-9]+|\b[A-Z][a-z]+[.]|\b[A-Za-z]+['][a-z]+|[A-Z.]+[A-Z]|\b[A-Za-z-]+|[.]+|[.,'"!?:;]'''

word_token = re.findall(pattern, text)
token_dictionary = {}

for element in word_token:
    if element in token_dictionary:
        token_dictionary[element] += 1
    else:
        token_dictionary[element] = 1

for key in sorted(token_dictionary.keys()):
    print("{} {}".format(key, token_dictionary[key]))
print('Tokens: ' + str(len(word_token)))
print('Types: ' + str(len(token_dictionary)))
