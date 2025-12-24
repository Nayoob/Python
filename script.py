import pyperclip as py
import sys as sy

accounts = {
    "facebook": "sufyan-khan2002",
    "password": "P@ssw0rd!23",     # example only — don't store real passwords like this
    "whatsapp": "+923337123456",
    "gmail": "sufyan.khan@gmail.com",
    "instagram": "sufyan_insta",
    "coursera": "sufyan_coursera"
}

if len(sy.argv) < 2:
    print("fuck you!")
    sy.exit()

account = sy.argv[1]

if account in accounts:
    py.copy(accounts[account])
    print("Password has been copied to clipBoard")
else:
    print('There is no account named ' + account)