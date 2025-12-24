import pyperclip as py
accounts = {
    "facebook": "sufyan-khan2002",
    "password": "P@ssw0rd!23",     # example only — don't store real passwords like this
    "whatsapp": "+923337123456",
    "gmail": "sufyan.khan@gmail.com",
    "instagram": "sufyan_insta",
    "coursera": "sufyan_coursera"
}
def getPassword():
    platform_name = input("Enter App Name ").strip().upper()
    found = False
    for app in accounts.keys():
        if app.upper() == platform_name:
            found = True
            py.copy(accounts[app])
            print("Password printed to clipboard. Press Ctrl+V to access!")
            break
    if not found:
        print(f"{platform_name.lower()} password doesn't Exist")
while True:
    getPassword()
    print('Do you want to check again(y/n)')   
    check = input().strip().lower()
    if check == 'y':
        continue
    elif check == 'n':
        break
