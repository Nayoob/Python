import pyperclip

name = input("Enter your name: ")
bloodgroup = input("Enter your blood group: ")
city = input("Enter your city: ")

data = f"Donor name is {name}, blood group is {bloodgroup}, and lives in {city}."

pyperclip.copy(data)

print("\n✅ Data has been copied to clipboard! You can paste it anywhere (Ctrl + V).")
