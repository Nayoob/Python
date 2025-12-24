# name = "i am sufyan's brother"
# updateName = 'i am \"sufyan" big brother'
# print(name)
# print(updateName)


# slice = name[2:]
# print(slice)

# print('hello' not in name)

# print('hello'.isalpha())
# print('hello2'.isalpha())
# print('iamsufyan'.isalpha())


# print('iam334sufyan'.isalnum())

# print('234232'.isdecimal())

# print('\n '.isspace())

# print('Thisissufyan'.istitle())

# print('hell3223o'.isalnum())


# while True:
#     print('Enter you password')
#     takePassword = input()
#     if takePassword.isalnum():
#         print(takePassword)
#         break
#     print('Enter password again')

print('hello world'.endswith('rld'))

print('Thisistitlecase'.istitle())


arr = ['sufyan' , 'jabbar', 343 ]

newarr = ''.join(str(i) for i in arr)
print(newarr)

string = 'my-name-is-jabbar'.split('-')
print(string)

stringtwo = '--'.join(str(i) for i in arr)
print(stringtwo)


string3 = 'my name, is jabbar, the greate!'.split(',')
print(string3)


# rjust and l just and center 

stringfour = 'sufyankhan'.rjust(20,'*')
print(stringfour)


def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))


picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)
