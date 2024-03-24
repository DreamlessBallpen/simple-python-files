# The challenge is to have the user input their birthday in a number format, like 19891201, and 
# the function keeps adding the numbers until only a single digit remains. The computed digit is considered to be the
# 'digit of life'


def digit_of_life() -> int:
    string_date = input('Please enter your birthday in number form: ')
    string_to_sum = string_date
    while True:
        total = 0
        for elem in string_to_sum:
            total += int(elem)
        if len(str(total)) > 1:
            string_to_sum = str(total)
            continue
        else:
            break
    return total

print(digit_of_life())
