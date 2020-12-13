# Create three strings using three different methods. Save your result to result_string_1, result_string_2,
# result_string_3 variables

result_string_1 = 'My first string'
result_string_2 = "My second string"
result_string_3 = '''My third string'''
print(result_string_1)
print(result_string_2)
print(result_string_3)
print('______________')

# Enter your first and  last name. Join them together with a space in
# between. Save a result in a variable result_full_name and
# save the length of the whole name in result_full_name_length variable.

first_name = input('Enter first name: ')
last_name = input('Enter last name: ')
result_full_name = first_name + ' ' + last_name
result_full_name_length = len(result_full_name)
print(result_full_name)
print(result_full_name_length)
print('______________')

# Enter the capital city of California State in lower case. Change the case to title case.
# Save the result in result_ca_capital variable

ca_capital = 'sacramento'
result_ca_capital = ca_capital.title()
print(result_ca_capital)
print('______________')

# Enter the name of our planet. Change the case to upper case. Save the result in
# result_planet variable

our_planet = 'Earth'
result_planet = our_planet.upper()
print(result_planet)
