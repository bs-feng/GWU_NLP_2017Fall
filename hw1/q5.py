import re

a_series_of_num = input("Enter the number: ")
num = re.findall(r'\b\d+', a_series_of_num)
tokens = len(num)

num_dictionary = {}

for element in num:
    if int(element) in num_dictionary:
        num_dictionary[int(element)] += 1
    else:
        num_dictionary[int(element)] = 1


for key in sorted(num_dictionary.keys()):
    print("{} {}".format(key, num_dictionary[key]))
print('Tokens: ' + str(tokens))
print('Types: ' + str(len(num_dictionary)))
