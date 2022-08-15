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

# ---------if statement---------
# age = int(input('How old are you?: '))
#
# if age >= 18:
#     print('You are and adult')
# elif age < 0:
#     print('you are not born yet!')
# else:
#     print('You are a child')


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

# ------while loop-----
# name = ''
#
# while len(name) == 0:
#     name = input('enter your name: ')
#
# print('Hello '+name)

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






