# what is type hinting in python 
# type hinting is used to enhance the readibility of code it doesnt affect our python code 
# but act as a meta data for variables 
# but the fun fact is it doesnt affect the code i mean if i pass the string instead of int in third parameter 
# of create__user func it wont affect the functionailty 

def create__user(name: str, last_name: str , age: int) -> dict :

    email = f'{name.lower()}_{last_name.lower()}@gmail.com'

    return {
        "name" : name,
        "lastName" : last_name,
        "age" : age,
        "email" : email
    }
    # def print_details():
    #     print(name , last_name , age , email)

    # return print_details


user1: dict= create__user("sufyan",'Khan', 23)

print(user1)
# print(user1.__closure__)

