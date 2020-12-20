print('______________')
# Slice string string_5 from the first to the last character, save only every forth character and
# save the result to variable result_6

string_5 = 'Python is a programming language that lets you work quickly and integrate systems more effectively'
result_6 = string_5[0::4]
print(result_6)

print('______________')
# Slice string string_6 from the first to 14th (including 14th) character, save only every third character and save
# the result to variable result_7

string_6 = 'Python is a programming language that lets you work quickly and integrate systems more effectively'
result_7 = string_6[0:14:3]
print(result_7)

print('______________')
# Save to variable result_8 string value from string_7 variable, written in reverse order, using slicing.

string_7 = 'Python'
result_8 = string_7[::-1]
print(result_8)

print('______________')
# Create a range of numbers from 0 to 10 (excluding 10) and save it to result_9 variable

numbers = [3, 6, 8, 9, 1]
result_9 = numbers[0:]
print(result_9)
