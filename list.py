
import random as rand
#list in python store data and that list in it self can be considered as variable that hold the refrence to list
list = ["jabbar" , 'sufyan' , 23 , 'pishin']
# python list can contain values of different data types 

print(list[0])
print(list)

#we can lists with in list too 
list_Two = ['jabbar' , [1 , 2 , 3] , ['a' , 'b' , 'ccuuss'] , False]
name = 'sufyan'
print(name[0])
print(list_Two[0])

# getting sublist and slices from list 

sliceOne = list[0:2]
sliceTwo = list_Two[1]
result = sliceOne + sliceTwo 
print(result)

del result[0]

print(result)

# listThree = [] 

# for i in range(5):
#     print("Enter value")
#     name = input()
#     listThree[i] = name


# print(listThree)



supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
print(len(supplies))
for i in range(len(supplies)):
 print('Index ' + str(i) + ' in supplies is: ' + supplies[i])



myDecomposition = ['fat', 'average' , 'brown']

weight , height , color = myDecomposition

print(weight , height , color)


messages = ['It is certain',
'It is decidedly so',
'Yes definitely',
'Reply hazy try again',
'Ask again later',
'Concentrate and ask again',
'My reply is no',
'Outlook not so good',
'Very doubtful']