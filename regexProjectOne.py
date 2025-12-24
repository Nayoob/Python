import pyperclip
import re
# Step 1: create regex for phone numbers
phoneRegex = re.compile(r'''
(
    (\d{3}|\(\d{3}\))?       # area code (optional)
    (\s|-|\.)?               # separator (optional)
    (\d{3})                  # first 3 digits
    (\s|-|\.)                # separator
    (\d{4})                  # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?   # extension (optional)
)
''', re.VERBOSE)

# Step 2: create regex for emails
emailRegex = re.compile(r'''
(
    [a-zA-Z0-9._%+-]+        # username
    @                        # @ symbol
    [a-zA-Z0-9.-]+           # domain name
    (\.[a-zA-Z]{2,4})        # dot-something (.com, .net, .org, etc)
)
''', re.VERBOSE)

# step3 find all the matches in the clip borad 

text = str(pyperclip.paste())
sample_text = """Here are some contacts you might need:

John Doe: 415-555-1234, john.doe@example.com
Jane Smith: (212) 555-9876 x101,
Mike Brown: 650.555.4321, """
# print(phoneRegex.findall(sample_text))
matches = []
for groups in phoneRegex.findall(sample_text):
    phoneNumber = '-'.join([groups[1], groups[3] , groups[5]])
    matches.append(phoneNumber)
# print(emailRegex.findall(sample_text))
for email in emailRegex.findall(sample_text):
    matches.append(email[0])
# print(matches)

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print("Matches copied to clip board....")
else:
    print("No emaial and phone number is matched ....")