users ={
    'id':1 ,
    'name': 'Leonardo Da Vinci',
    'username': 'Leonardo',
    'email' : 'Davinci@agust.biz',
    'address' : {
        'street' : 'Paris',
        'suite'  : 'apt.664',
        'city'   : 'Gweentloud',
        'zipcode': '231333232-43244233',
    }

}
print(users)
print(users['id'])
print(users['name'])
print(users['username'])
print(users['email'])
print(users['address'])

print('\nubah Dict Ke Json')
import json
result = json.dumps(users)
print(result)
print(type(result))

print('\nubah dict ke Json tapi menggunakan kan dump')
with open('result.json' ,'w') as file:
    json.dump(users,file)
print('\n dengan ini file json akan tebuat di file baru dan sudah berbentuk json')