import random as rs

messages = ['It is certain',
'It is decidedly so',
'Yes definitely',
'Reply hazy try again',
'Ask again later',
'Concentrate and ask again',
'My reply is no',
'Outlook not so good',
'Very doubtful']

def random():
    randomNumber = rs.randint(0 , len(messages)-1)
    return f'{messages[randomNumber]} , {randomNumber}'
    
for i in range(5):
    
    print(random())


name = 'sufyan khan yousufzai'
newName = name[0:6] + " the " +  name[12:-1]

print(newName)

myNameTuppel = tuple("sufyan")


print(myNameTuppel)
# myNameTuppel[2] = 34

spam = ['apples', 'bananas', 'tofu', 'cats']
def getlist(lisst):
    
    return str(lisst)

print(getlist(spam))
print(type(getlist(spam)))