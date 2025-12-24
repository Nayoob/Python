print(2+2)
print(2/10)
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
    'firstname':'Asabeneh', 
    'lastname':'Yetayeh', 
    'country':'Finland',
    'city':'Helsinki',
     'skills' : skills
    }
person_info['firstname'] = "sufyan"
print('Person information: ', person_info.get("firstname"))
print("skills" , person_info.get('skills'))