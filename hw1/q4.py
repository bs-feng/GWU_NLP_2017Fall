import re

f = open('q4text.txt')
text = f.read()
f.close()

pattern = r'''[0-9]+[,][0-9]+|[0-9]+[.][0-9]+|[0-9]+|\b[A-Z][a-z]+[.]|\b[A-Za-z]+['][a-z]+|[A-Z.]+[A-Z]|\b[A-Za-z-]+|[.]+|[.,'"!?:;]'''

word_token = re.findall(pattern, text)
for element in word_token:
    print(element)
