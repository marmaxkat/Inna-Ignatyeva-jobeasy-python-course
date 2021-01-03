# FUNCTIONS

# Difference
# Write a function, which will calculate the difference of these two numbers

num_1 = int(input('First number: '))
num_2 = int(input('Second number: '))

def difference(num_1, num_2):
    difference = abs(num_1 - num_2)
    return difference

print(difference(num_1, num_2))

# Division
# Write a function, which will divide these two numbers

def division(num_1, num_2):
    if not num_2:
        return 'Can\'t divide by zero'
    division = num_1 / num_2
    return division

print(division(num_1, num_2))

# Function gets random number. If this number is more than ten, return the difference between 100 and this number,
# otherwise return this number multiplied by 10

# from random import random
#
# def function_1(number):
#     if number > 10:
#         result = 100 * number
#     else:
#         result = number * 10
#     return result
#
# number = random()
# print(number)

import random

def function_1(number: int):
    if number > 10:
        result = 100 - number
    else:
        result = number * 10
    return result

number = random.randint(0, 1000)
print(number)
print(function_1(number))


# Your function temerature_convertor gets the temperature in Fahrenheit, convert it to Celsius and return.
# Formula (32°F − 32) × 5/9 = 0°C

temperature_fahrenheit = int(input('Enter the temperature in Fahrenheit: '))

def temerature_convertor(fahrenheit_degree):
    celsius_degree = (fahrenheit_degree - 32) * 5 / 9
    result_temperature = round(celsius_degree)
    return result_temperature

print(f'{temerature_convertor(temperature_fahrenheit)} C')


# Taxi Fare
# In a particular jurisdiction, taxi fares consist of a base fare of $4.00, plus $0.25 for every 140 meters travelled.
# Write a function that takes the distance travelled (in kilometers) as its only parameter and returns the total fare
# as its only result rounded by 2 digits. Write a program that demonstrates the function.

distace = int(input('Enter your distance in km: '))
base_fare = 4.00
def taxi_fare(distance):
    result_fare = round(base_fare + distance / 0.14 * 0.25, 2)
    return result_fare

print(f'Taxi fare for {distace} km is ${taxi_fare(distace)}')


# examples of usage:
# taxi_fare(10) #21.86
