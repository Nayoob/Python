import re
# the pip usage matching multiple groups with pip 

regexObject = re.compile(r"sufyan|khan")
matchObject = regexObject.search("i am khan sufyan the great")
print(matchObject.group())


regexObjectOne = re.compile(r'bat(man|mobile|women)')
matchObjectOne = regexObjectOne.findall("the batwomen is cooked batmobile")
print(matchObjectOne)



# pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
# match = pattern.search("My number is 1011")
# print(match.group(3))
# print(match.group(1))
# print(match.group(2))


pattern = re.compile(r'jabbar(apple|orange|banana)-(\d+)')
mathcobject = pattern.search('i am the jabbarorange-333 and the banana-33432')
print(mathcobject.group())

patternOne = re.compile(r'(apple|orange|banana)-(\d+)')
mathcobjectOne = patternOne.findall('i am the orange-333 and the banana-33432')
print(mathcobjectOne)


# charcterclass of regex 
regex = re.compile('\d+\s\w+')
chMatchObject = regex.findall('12 drummers_232, 11\tpipers, 10lords, 9\nladies, 8 maids, 7swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
# print(chMatchObject)

for n in chMatchObject:
    if n.startswith('11') or n.startswith('9'):
        print(n)


# the carrot and dollor sign character how does that work 
# the carot sign in sqare brakcet work as negation  tool 
# but the carot sign wihtout square bracket mean the string start with this word 

startWith = re.compile(r'^hello\s\sufyan$')
startWithMatch = startWith.search('hello sufyan its saturday')
print(startWithMatch)

# matching stuff with .*

objecct = re.compile(r'First Name: (.*) Last Name: (.*)')
matchObj = objecct.search("First Name:  Last Name: jan")
print(matchObj.group(1))
print(matchObj.group())


subObject = re.compile(r'Agent \w+')
subMatch = subObject.sub('censord' , 'Agent Alice gave the secret documents to Agent Bob.')
print(subMatch)