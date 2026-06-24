# # Medium & Advanced Python Practice Questions


# ---

# # 1. Variables, Data Types & Input Handling

# ## Q1

# Create a program that accepts:

# * employee name
# * monthly salary
# * years of experience
# Then calculate yearly salary and print:
# if experience is greater than 5 years.

# print('Enter the some information!')
# emp_name=input('Enter the Enployee Name: ')
# mon_salary=int(input('Enter the Monthly Salary: '))
# exp=int(input('Enter your Years of experience: '))

# print(f'{emp_name} yearly salary is: ',mon_salary*12)
# if exp>5:
#     print('Senior Employee')


# ---

# ## Q2

# Take a string input from the user and print:

# * total characters
# * total digits
# * total alphabets
# * total special characters

# string=input('Enter the Sentance: ')
# T_char=0
# T_digi=0
# T_alph=0
# T_spe=0

# for i in string:
#     T_char+=1
#     if i.isalpha():
#         T_alph+=1
#     elif i.isdigit():
#         T_digi+=1
#     elif not i.isalpha() and not i.isdigit():
#         T_spe+=1

# print('Total characters',T_char)
# print('Total digits',T_digi)
# print('Total alphabets',T_alph)
# print('Total special characters',T_spe)


# ---

# ## Q3

# Create a currency converter:

# * INR to USD
# * USD to INR

# Use user choice with conditional statements.

# print('Currency Converter')
# print('If INR to USD Press: 1')
# print('If USD to INR Press: 2')

# choice = int(input('Enter your choice: '))

# if choice == 1:
#     inr = float(input('Enter INR Amount: '))
#     print('Dollar Amount:', inr / 83)

# elif choice == 2:
#     usd = float(input('Enter Dollar Amount: '))
#     print('INR Amount:', usd * 83)

# else:
#     print('Invalid Choice')


# ---

# ## Q4

# Write a program that checks whether a given number is:

# * integer
# * float
# * string
# * boolean

# without manually checking the value.
# value=input('Enter Any think: ')
# for i in value.split():
#     if i=='True' or i=='False':
#         print(i,' Type Boolena')
#     elif i.isdigit():
#         print(i,' Type Integer')
#     elif '.' in i:
#         print(i," Type Float")
#     else:
#         print(i,' Type String')

# ---

# ## Q5

# Take a sentence input and print:

# * number of words
# * longest word
# * shortest word

# lw=[]
# sw=[]
# number_of_words=0

# a=input('Write a sentence: ')
# for i in a.split():
#     number_of_words+=1
#     lw.append(len(i))
#     sw.append(len(i))
# print('Number of words: ',number_of_words)
# for i in a.split():
#     if len(i)==max(lw):
#         print('longest word: ',i," len is ",max(lw))
#     elif len(i)==min(sw):
#         print('Shortest word: ',i," len is ",min(sw))


# ---

# # 2. Conditional Statements (Medium–Advanced)

# ## Q6

# Create a login system:

# * maximum 3 attempts allowed
# * if password is correct:

# User_id='root'
# password='root'
# count=0
# for i in range(3):
#     count+=1
#     en=input('Enter the User Id: ')
#     pa=input('Enter the Password: ')
#     if en==User_id and pa==password:
#         print('Login Successful!')
#         break;
#     elif count==3:
#         print('Account Locked!')
#     else:
#         print('Try Again!')
#         pass;

# ---

# ## Q7

# Write a program to classify a triangle:

# * Equilateral
# * Isosceles
# * Scalene

# based on side lengths.

# A=int(input('Enter the triangle A side lengths in CM: '))
# B=int(input('Enter the triangle B side lengths in CM: '))
# C=int(input('Enter the triangle C side lengths in CM: '))
# if A==B==C:
#     print('Equilateral triangle')
# elif A==B or B==C or A==C:
#     print('Isosceles triangle')
# else:
#     print('Scalene triangle')
# ---

# ## Q8

# Create a BMI calculator and classify:

# * Underweight
# * Normal
# * Overweight
# * Obese

# Hight=float(input('Enter the Hight: '))
# Weight=float(input('Enter the Weight: '))
# BMI=Weight/(Hight**2)
# if BMI>=30:
#     print('Obesity')
# elif BMI<29.9 and BMI>25:
#     print('Overweight')
# elif BMI <24.9 and BMI>18.5:
#     print('Normal weight')
# else:
#     print('Underweight')

# ---

# ## Q9

# Write a grading system with nested conditions:

# * distinction
# * first division
# * second division
# * fail

# Also validate marks input.
# marks=int(input('Enter the Yours Marks!: '))
# if marks>=95:
#     print('distinction')
# elif marks<94 and marks>=60:
#     print('first division')
# elif marks<59 and marks>=33:
#     print('second division')
# else:
#     print('Fail')

# ---

# ## Q10

# Build a simple ATM simulation:

# * withdraw
# * deposit
# * balance check
# * insufficient balance handling

# ---
# balance=30000
# print('Select The option: ')
# print('Withdraw Press 1')
# print('Deposit Press 2')
# print('Balance check Press 3')
# choice=int(input('Enter the Option: '))
# if choice==1:
#     amt=float(input('Enter the Amount: '))
#     if amt<=balance:
#         balance=balance-amt
#         print(' Your amount successfully withdrawal')
#         print(' Your available balance is: ',balance)
#     else:
#         print('Insufficient balance!')
# elif choice==2:
#     amt=float(input('Enter the Amount: '))
#     balance+=amt
#     print(' Your amount successfully deposit')
#     print(' Your available balance is: ',balance)
# elif choice==3:
#     print(' Your available balance is: ',balance)

# # 3. Loops & Logic Building

# ## Q11

# Print all Armstrong numbers between 1 and 1000.

# for num in range(1,1001):
#     arm=0
#     degits=len(str(num))
#     for i in str(num):
#         arm+=(int(i)**degits)
#     if arm==int(num):
#         print(arm,' is Armstrong numbers.')
#         arm=0
# ---

# ## Q12

# Create a pattern:

# ```python
# *
# **
# ***
# ****


# for i in range(5):
#     print(('*')*i)

# ```

# Then create the reverse pattern.
# for i in range(4,0,-1):
#     print(('*')*i)

# ---

# ## Q13

# Find all prime numbers within a user-defined range.

# num=int(input('Enter the Number: '))
# for i in range(1,num+1):
#     count=0
#     for j in range(1,i+1):
#         if i%j==0:
#             count+=1
#     if count==2:
#         print(i,' Is prime number.')
#         count=0

# ---

# ## Q14

# Write a program to find:

# * factorial
# * sum of digits
# * product of digits

# for a given number.
# num=int(input('Enter the Number: '))
# fac=1
# for i in range(1,num+1):
#     fac*=i
# print(fac)


# num=input('Enter the Number: ')
# sum_digits=0
# for i in num:
#     sum_digits+=int(i)
# print(sum_digits)


# num=input('Enter the number: ')
# mult=1
# for i in num:
#     mult*=int(i)
# print(mult)

# ---

# ## Q15

# Generate Fibonacci series up to `n` terms using loops.

# a=0
# b=1
# Fibonacci_series=[0,1]
# num=int(input('Enter the number: '))
# for i in range(num):
#     Fibonacci_series.append(Fibonacci_series[i]+Fibonacci_series[i+1])
# print(Fibonacci_series)
# ---

# ## Q16

# Write a program that checks whether a number is:

# * palindrome
# * Armstrong
# * perfect number


# def arm(num):
#     a = str(num)
#     result = 0
#     digits = len(str(num))
#     for i in a:
#         result += int(i) ** digits
#     if num == result:
#         return f"{num} is Armstrong Number."
#     else:
#         return f"{num} is not Armstrong Number."


# def pali(num):
#     if num == int(str(num)[::-1]):
#         return f"{num} is palindrome Number."
#     else:
#         return f"{num} is not palindrome Number."


# def per(num):
#     result = 0
#     for i in range(1, num):
#         if num % i == 0:
#             result += i

#     if result == num:
#         return f"{num} is Perfect number"
#     else:
#         return f"{num} is not Perfect number"


# num = int(input("Enter the number: "))
# print(arm(num))
# print(pali(num))
# print(per(num))
# ---

# ## Q17

# Create a multiplication table generator for numbers 1–20.
# for i in range(1,21):
#     for j in range(1,11):
#         print(i*j,'\n\t')
#     print('\n')
    
# ---

# ## Q18

# Find the frequency of each digit in a number.





# # 4. Functions (Important for Interviews)

# ## Q19

# Create a function that accepts unlimited numbers using `*args`
# and returns:
# * maximum
# * minimum
# * average
# def mult(*num):
#     return f'Minimum number is: {min(num)}\nMaximum number is: {max(num)}\nAverage number is: {sum(num)/len(num)}'
# print(mult(10,20,30,40,52,65,85,74))
# ---

# ## Q20

# Write a function that accepts a sentence and returns:

# * total vowels
# * total consonants
# * total spaces

# string=input('Enter any String: ')
# con_str=0
# vow_str=0
# spa=0
# for i in string:
#     if i.lower() in 'aeiou':
#         vow_str+=1
#     elif i.lower() in 'bcdfghjklmnpqrstvwxyz':
#         con_str+=1
#     else:
#         spa+=1
# print(f'Total vowels: {vow_str}\nTotal consonants: {con_str}\nTotal spaces: {spa}')

# ---

# ## Q21

# Create a recursive function for:

# * factorial
# * Fibonacci
# * power calculation

# import math as mt
# num=int(input('Enter any Number: '))
# fact=0
# Fibo=[0,1]
# power=0

# print(f'Factorial: {mt.factorial(num)}')
# for i in range(num-2):
#     Fibo.append(Fibo[i]+Fibo[i+1])
# print(f'Fibonacci: {Fibo}')
# print(f'power calculation: {mt.pow(num,num)}')


# ## Q22

# Write a function decorator that prints:

# def decorator(num):
#     print('Function Started')
#     Fibo=[0,1]
#     for i in range(num-2):
#         Fibo.append(Fibo[i]+Fibo[i+1])
#     print(f'Fibonacci: {Fibo}')
#     print('Function Ended')

# decorator(int(input('Enter the Number: ')))


#  Q23

# Create a function that validates email format.

def validates(Email):
    if Email.endswith('@gmail.com') or Email.endswith('@icloud.com') or Email.endswith('@outlook.com') or Email.endswith('@zoho.in'):
        print(f'{Email}: Valid Email Id')
    else: 
        print(f'{Email}: Invalid Email ID')

validates(input('Enter the Email Id: '))

# ## Q24

# Write a function that returns all duplicate elements from a list.

# ---

# ## Q25

# Create a function that flattens a nested list.

# Example:

# ```python
# [[1,2],[3,4]]
# ```

# Output:

# ```python
# [1,2,3,4]
# ```

# ---

# # 5. Exception Handling (Interview Level)

# ## Q26

# Create a division calculator using:

# * `try`
# * `except`
# * `finally`

# ---

# ## Q27

# Handle multiple exceptions:

# * ValueError
# * ZeroDivisionError
# * IndexError

# in one program.

# ---

# ## Q28

# Create a custom exception:

# ```python
# InvalidAgeError
# ```

# if age is below 18.

# ---

# ## Q29

# Write a file reader program with proper exception handling.

# ---

# ## Q30

# Create a banking system where negative withdrawal raises a custom exception.

# ---

# # 6. Lists (Very Important)

# ## Q31

# Find:

# * largest
# * second largest
# * third largest

# from a list without using sorting.

# ---

# ## Q32

# Remove duplicates from a list while maintaining order.

# ---

# ## Q33

# Rotate a list by `k` positions.

# Example:

# ```python
# [1,2,3,4,5]
# ```

# Output:

# ```python
# [4,5,1,2,3]
# ```

# ---

# ## Q34

# Find common elements between two lists without using sets.

# ---

# ## Q35

# Write a program to separate:

# * even numbers
# * odd numbers

# into different lists.

# ---

# ## Q36

# Find all pairs whose sum equals a target value.

# ---

# ## Q37

# Implement bubble sort manually.

# ---

# ## Q38

# Implement binary search manually.

# ---

# # 7. Tuples

# ## Q39

# Swap two tuples without using a temporary variable.

# ---

# ## Q40

# Find repeated elements in a tuple.

# ---

# ## Q41

# Convert a tuple into:

# * list
# * dictionary
# * set

# ---

# # 8. Dictionaries (Most Important for Data Science)

# ## Q42

# Count frequency of each word in a paragraph.

# ---

# ## Q43

# Sort a dictionary by values.

# ---

# ## Q44

# Merge multiple dictionaries into one.

# ---

# ## Q45

# Find the student with highest marks from a dictionary.

# ---

# ## Q46

# Invert a dictionary:

# ```python
# {"a":1}
# ```

# Output:

# ```python
# {1:"a"}
# ```

# ---

# ## Q47

# Create a dictionary-based inventory management system.

# Features:

# * add product
# * update stock
# * delete product
# * search product

# ---

# # 9. Sets

# ## Q48

# Find:

# * union
# * intersection
# * symmetric difference

# between two sets.

# ---

# ## Q49

# Check whether one set is subset of another.

# ---

# ## Q50

# Remove duplicates from a sentence using sets.

# ---

# # 10. List Comprehension & Dictionary Comprehension

# ## Q51

# Generate squares of even numbers using list comprehension.

# ---

# ## Q52

# Create a list of prime numbers using list comprehension.

# ---

# ## Q53

# Create a dictionary where:

# ```python
# number -> cube
# ```

# using dictionary comprehension.

# ---

# ## Q54

# Filter words longer than 5 characters using comprehension.

# ---

# # 11. Generators (MNC Important)

# ## Q55

# Create a generator for Fibonacci numbers.

# ---

# ## Q56

# Create a generator that reads a large file line by line.

# ---

# ## Q57

# Create an infinite generator for even numbers.

# ---

# ## Q58

# Compare memory usage:

# * list
# * generator

# ---

# # 12. String Problems (Very Important)

# ## Q59

# Check whether two strings are anagrams.

# ---

# ## Q60

# Find the first non-repeating character in a string.

# ---

# ## Q61

# Compress a string:

# ```python
# aaabbcc
# ```

# Output:

# ```python
# a3b2c2
# ```

# ---

# ## Q62

# Find the longest word in a sentence.

# ---

# ## Q63

# Reverse words in a sentence.

# Example:

# ```python
# I love Python
# ```

# Output:

# ```python
# Python love I
# ```

# ---

# # 13. File Handling

# ## Q64

# Count:

# * lines
# * words
# * characters

# from a text file.

# ---

# ## Q65

# Copy contents from one file to another.

# ---

# ## Q66

# Find the most frequent word in a file.

# ---

# ## Q67

# Create a CSV reader without using pandas.

# ---

# # 14. Data Science Style Questions

# ## Q68

# Given a list of salaries:

# * find average salary
# * highest salary
# * employees above average salary

# ---

# ## Q69

# Handle missing values (`None`) in a dataset list.

# ---

# ## Q70

# Create a mini student report card system using dictionaries and functions.

# ---

# # 15. Advanced Logic Questions

# ## Q71

# Find all duplicate characters in a string.

# ---

# ## Q72

# Implement linear search and binary search.

# ---

# ## Q73

# Check whether a matrix is symmetric.

# ---

# ## Q74

# Transpose a matrix manually.

# ---

# ## Q75

# Create a simple command-line quiz application.

# ---
