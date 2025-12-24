import re 


def isPhoneNumber(text):
    if len(text) != 12:
        return False
    
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    
    if text[3] != '-':
        return False
    
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    
    if text[7] != '-':
        return False
    
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    
    return True


print('415-555-4242 is a phone number:')
print(isPhoneNumber('415-555-4242'))

print('Moshi moshi is a phone number:')
print(isPhoneNumber('Moshi moshi'))


message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'

# print(len(message))
listOne = []
for i in range(len(message)):
    chunk = message[i : i+12]
    if isPhoneNumber(chunk):
        listOne.append(chunk)

print(' , '.join(listOne))   
    


regix_Object = re.compile(r'\d{3}-\d{3}-\d{4}')

match_object = regix_Object.findall('My number is 415-555-4242 my brother number is 415-653-4242 and my pakistani number is 03337132996')

print(match_object)


# so there is more to learn about the regex in python  and the next one is groups in regex we 
# can create groups in our pattern too 
print("_________________________________-")
another_Regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')

matchObject = another_Regex.search("My number is 4715-234-42426 my brother number is  and my pakistani number is 03337132996")
print(matchObject.group(0))
print(matchObject.group(1))
print(matchObject.group(2))
print(matchObject.groups())

# here we have a problem to fix just remeber we will hit this part later
# and the problem is even though the string is not matching here but still the match object has the first match object here
# which is very wierd and its giving me the substring we are goona fix that later 
# print(matchObject)


dateRegixObject = re.compile(r'(\d\d\d\d)-(\d\d)-(\d\d)')
dateMatch = dateRegixObject.search('Date: 2025-11-19')
print(dateMatch.groups())
year , month , day = dateMatch.groups()
print(f'{day}-{month}-{year}')




