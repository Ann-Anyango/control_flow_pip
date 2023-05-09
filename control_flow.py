# Write a Python program that takes a 
# list of strings as input and outputs the 
# number of times each string appears in the list, using 
# # a dictionary
strings = ['apple', 'banana', 'orange', 'apple', 'banana', 'pear', 'apple']
start = {}
for string in strings:
    if string in start:
        start[string] += 1
    else:
        start[string] = 1
for string, start in start.items():
    print(string, start)

# Write a Python program that takes a 
# list of numbers as input and outputs the median of the numbers 
def lists_number(number):
    sorted_list=sorted(number)
    lists_lenghth=len(number)
    mid_index = lists_lenghth// 2
    if lists_lenghth % 2 == 0:
        return (sorted_list[mid_index-1] + sorted_list[mid_index]) / 2
    else:
        return sorted_list[mid_index]

input_list = [3, 5, 1, 7, 2, 8, 4]
output = lists_number(input_list)
print(output)
# Write a Python program that takes a list of numbers
#  as input and outputs the second largest number in 
# the list using conditional statements and a for loop.
def list_of_numbers(numbers):
    count_1= numbers[0]
    count_2=numbers[0]
    for num in numbers:
        if num > count_1:
            count_2 = count_1
            count_1 = num
        elif num > count_2 and num != count_1:
            count_2 = num
    return count_2
input_list = [3, 5, 1, 7, 2, 8, 4]
output = list_of_numbers(input_list)
print(output)
# Write a Python program that takes a year as 
# input and determines if it is a leap year.
def leap_year(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False

input_year = 2023
output = leap_year(input_year)
print(output)

# Write a Python program that takes a 
# string as input and checks if it is a palindrome 
# (reads the same forwards
#  and backwards), ignoring spaces and punctuation.
# def string_check_palindriome(string):

#   return cleaned_string == cleaned_string[::-1]
