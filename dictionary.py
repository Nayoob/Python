# spam = ['cats', 'dogs', 'moose']
# bacon = ['dogs', 'moose', 'cats']
# print(spam == bacon)   # False

# eggs = {
#     'name': 'Zophie',
#     'species': 'cat',
#     'age': '8'
# }
# ham = {
#     'species': 'cat',
#     'age': '8',
#     'name': 'Zophie'
# }
# print(eggs == ham)     # True


# birthdays = {'Alice': 'Apr 1',
#              'Bob': 'Dec 12',
#              'Carol': 'Mar 4'
# }

# listOne = birthdays.keys()
# print(listOne)
# print(birthdays.values())
# print(birthdays.items())

# print(birthdays)
# while True:
#     print("Enter your Name (Enter to Quite)")
#     name = input()
#     if name == '':
#         break
#     if name in birthdays.keys():
#         print(f'{name} birthday is {birthdays[name]}')
#     else:
#         print(f'i dont have birthdayInfo for this name what his birthday?')
#         bday = input()
#         birthdays[name] = bday
#         print("db updated.....")

# print(birthdays)


# spam = {'color': 'red'}
# items_view = spam.items()
# print(items_view)

# pair = list(items_view)[]  # ['color', 'red']
# print(pair)

# # pair[0][0] = 'age'    

# print(spam)
# print(pair)

khayal = {
    "name": "Khayal Naseeb",
    "age": 22,
    "location": "Quetta, Pakistan",
    "profession": "Web & App Developer",
    "interests": ["AI", "Machine Learning", "Blockchain", "Web Development"],

    # nested dictionary
    "education": {
        "degree": "BS Computer Science",
        "university": "University of Baluchistan",
        "year": "Ongoing",
        "courses": ["Web Development", "Data Structures", "Databases", "AI Fundamentals"]
    },

    # list of skills
    "skills": [
        "HTML", "CSS", "Bootstrap", "Tailwind", "JavaScript",
        "React", "Node.js", "Express.js", "MongoDB", "Python", "Django"
    ],

    "github": "https://github.com/khayalnaseeb",
    "goal": "To become a skilled AI & Blockchain Engineer"
}

# lets say we want to display the key value pair by using the for loop on the dictionary 

itemss = khayal.items()
# print(itemss)
updated_items = list(khayal.items())
# print(updated_items)

for i in updated_items:
    print(i)
for v, k in updated_items:
    print(f'key is {v} : value is {k}')
# print(khayal.keys()) 

# keys = khayal.keys()
# print(keys)
# print("_________________________________________________")
# values = khayal.values()
# print(values)

# for keys in khayal.keys():
#     print(keys)

# for values in khayal.values():
#     print(values)

# listt = list(khayal.keys())
# print(listt)
# for key in listt:
#     khayal[key] = 'sufyan'

# print(khayal.keys())    
    

# print(khayal)


# dictiory chapter challenge 

def createObj(addedItems):
    newInventory = {}
    for item in addedItems:
        newInventory[item] = newInventory.get(item , 0) + 1
    return newInventory     

def addToInventory(inventory, addedItems):
    newLootData = createObj(addedItems)
    for item , count  in newLootData.items():
        inventory[item] = inventory.get(item , 0) + count
    return inventory

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
print(inv)




