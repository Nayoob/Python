
from doctest import debug
from pickle import DICT

from pyparsing import dict_of


def decorator(func):
    def wrapper():
        print("before func call")
        func()
        print("after func call")
    return wrapper
    

def hello():
    print("hello jabbara !!!")

hello()
print(id(hello))

print("_______________________________")

hello = decorator(hello)

hello()
print(id(hello))

# the upper part is manual decoration right 


person = {
    'name':"sufyan",
    "age" : 23
}

print(person.items())


students = [
    ("Ali", 85, True),
    ("Ahmed", 72, True),
    ("Sara", 90, True),
    ("Zain", 88, False)
]


newlist = [tup[0] for tup in students if tup[2] == True and tup[1] > 80]

print(newlist)


lis = ['even' if num % 2 == 0 else 'odd' for num in range(11)]
print(lis)



