# lets start error handling in python 

# the errro handling is a bit simple in python then other concepts 
# it basically means that when ever we get a clue that yeah this is the code where error can arise
# we put that snippet in the try block so we can cannot ruin the user exp for example 

from warnings import catch_warnings


def divideBy(dividend :int , divisor: int) -> float:
    try:
        # print(k)
        ans = dividend / divisor
        return ans
    except NameError:
        print("k kidaar hay jo to print karwa raha hay ")
        return 0.0
    except ZeroDivisionError:
        print('zero division erro hay bahi .....')
        return 0.0
    except Exception as e:
        print(e)
        print("Cant do invalid ops....")
        return 0.0
        
    
print(divideBy(10 , 0))


# there is one more thing that is i guess a bit important to diccuss and its else 
# for example if we want to check weather we are connected to db or not or we want to get data from backend 
# through some api call we will first check if backend services are availible 
try:
    # is db connected 
    # is backend server live?
    # Check services before api call 
    print("khan")
except Exception as e:
    print(e)
else:
    # write the code of what ever you want to do after checking if the connection is 
    # working fine weather is sending data or making api call or sending data to db
    print("send data")
finally:
    print("yei to har hal  may print hoga")



def process():
    try:
        x = int("abc")
    except ValueError:
        # We raise a new error with context
        raise ValueError("Conversion failed in process()")

def main():
    try:
        process()
    except ValueError as e:
        # Handle it gracefully instead of crashing
        print("Oops, something went wrong:", e)
    print("All done safely")

main()

# good example to understand why do we need the custom exception class 

class SecurityError(Exception):

  def __init__(self,message):
    print(message)

  def logout(self):
    print('logout')

class Google:

  def __init__(self,name,email,password,device):
    self.name = name
    self.email = email
    self.password = password
    self.device = device

  def login(self,email,password,device):
    if device != self.device:
      raise SecurityError('bhai teri to lag gayi')
    if email == self.email and password == self.password:
      print('welcome')
    else:
      print('login error')

obj = Google('nitish','nitish@gmail.com','1234','android')

try:
  obj.login('nitish@gmail.com','1234','windows')
except SecurityError as e:
  e.logout()
else:
  print(obj.name)
finally:
  print('database connection closed')
