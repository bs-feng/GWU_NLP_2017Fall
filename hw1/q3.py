def add_up_number(number):
    number_string = str(number)
    sum = 0
    for index in range(len(number_string)):
        sum += int(number_string[index])
    return sum


number = input("Enter the number:")

print("The result which adds up all the digits of the number is: {}".format(add_up_number(number)))
