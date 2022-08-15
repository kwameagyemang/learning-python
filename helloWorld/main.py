import time
# slicing = create a substring by extracting elements from another string
# indexing[] or slice()
# [start:stop:step]

# indexing[]
# ---------------------------------------------
# name = 'Kwame Agyemang'
#
# first_name = name[0:5]         # name[:5]    # name[:5]
# last_name = name[6:14]         # name[6:]    # name[6:end]
# funky_name = name[0:14:2]      # name[::2]   # name[0:end:2]
# reversed_name = name[::-1]  # name[::-1]  # name[0:end:-1]
#
# print(reversed_name)

# slicing()
# ------------------------------------------------------

# website1 = 'http://google.com'
# website2 = 'http://wikipedia.com'
#
# slice = slice(7,-4)
#
#
# print(website1[slice])

# -------------------------------------------------------------------------------
# ---------if statement---------
# age = int(input('How old are you?: '))
#
# if age >= 18:
#     print('You are and adult')
# elif age < 0:
#     print('you are not born yet!')
# else:
#     print('You are a child')

# -------------------------------------------------------------------------------
# ----logical operators (and,or,not) = used to check if two or more conditional statement is true
# not---when both conditions are true
# or--when one condition is true
# not---change true to false or false to true
# temp = int(input('What is the temperature outside?: '))
#
# if not(temp >= 0 and temp <= 30):
#     print('the temperature is  bad today')
#     print('stay  inside!')
# elif not(temp < 0 or temp > 30):
#     print('the temperature is good today')
#     print('go outside!')

# -------------------------------------------------------------------------------
# ------while loop-----
# name = ''
#
# while len(name) == 0:
#     name = input('enter your name: ')
#
# print('Hello '+name)

# -------------------------------------------------------------------------------

# -----For Loop-----

# for i in range(10):
#     print(i+1)

# for i in range(50,100+1,5):
#     print(i)

# for i in "kwame agyemang":
#     print(i)

# for seconds in range(10,0,-1):
#     print(seconds)
#     time.sleep(2)
# print('happy new year!')

# -------------------------------------------------------------------------------
# -----nested loop-----a loop inside another loop, 'inner loop' will finish iteration before finishing 'outer loop'

# rows = int(input('How many rows?: '))
# columns = int(input('How many columns?: '))
# symbol = input('Enter a symbol to use: ')
#
# for i in range(rows):
#     for j in range(columns):
#         print(symbol, end="")
#     print()

#
# for i in range(4):
#     for j in range(10):
#         print(j, end='')
#     print()

# row = int(input('how many rows?: '))
# column = int(input('How many columns?: '))
# symbol = input('What symbol?: ')
#
# for i in range(row):
#     for j in range(column):
#         print(symbol, end='')
#     print()

# -------------------------------------------------------------------------------

# ----loop control statement = change a loops execution from its normal sequence---

# break = used to terminate a loop entirely
# continue = skips to the next iteration of the loop
# pass = does nothing, acts like a placeholder

# while True:
#     name = input('Enter your name: ')
#     if name !="":
#         break

# phone_number = '123-456-7890'
#
# for i in phone_number:
#     if i == "-":
#         continue
#     print(i, end='')


# for i in range(1,21):
#     if i == 10:
#         pass
#     else:
#         print(i, end='')

# -------------------------------------------------------------------------------

# -----list = used to store multiple items in a single variable----

# food = ['pizza','hamburger','hotdog','cookies','pudding']
#
# food[0] = 'sushi'
# food.pop()
# food.remove('hotdog')
# food.sort()---arranges items in alphabetical order
# food.insert(0,'cake')
# food.append('ice cream')
# food.clear()
#
# for i in food:
#     print(i)

# -------------------------------------------------------------------------------

# 2d list or multidimensional list  = list of separate list

# drinks = ['coffee','soda','tea']
# dinner = ['pizza','hamburger','hotdog']
# dessert = ['cake','ice cream']
#
# food =[drinks,dinner,dessert]
# print(food[2][1])

# ----------------------------------------------------------
# tuple = collection which is ordered and unchangeable
# used to group together related data
# uses () unlike list which uses []

# student = ('kwame',32,'male')
#
# print(student.index('male'))
# print(student.count('kwame'))
#
# for i in student:
#     print(i)
#
# if 'kwame' in student:
#     print('kwame is here!')

# ------------------------------------------------------------------------






