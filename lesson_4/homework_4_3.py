 WHILE LOOPS EXERCISES

# Enter a random string in the variable string_1, then enter a character and save it in the variable char_1.
# Write code, which will count how many times your character is included in your string.
# Save result to result_1 variable

string_1 = 'I like Python! It\'s so cool.'
string_1_len =len(string_1)
i = 0
char_1 = 'o'
char_1_count = 0
while i < string_1_len:
    char_in_string = string_1[i]
    if char_in_string == char_1:
        char_1_count += 1
    i += 1
result_1 = char_1_count
print(result_1)


# Enter a random number and save it in variable number_1. Then create code to multiply all the digits together
# and save result in the result_2 variable.

number_1 = input('Enter a random number: ')
number_1_len = len(number_1)
result_2 = 1
i = 0
while i < number_1_len:
    result_2 *= int(number_1[i])
    i += 1
print(result_2)


# Enter a random number and save it in variable number_2. Then create code which will return
# a number with digits of number_1 in reverse order. Save it in result_3 variable

number_2 = input('Enter a random number: ')
number_2_len = len(number_2)
result_3 = ''
i = 1
while i <= number_2_len:
    result_3 += number_2[-i]
    i += 1
print(result_3)
