import requests

url = 'http://127.0.0.1:5000/get_form'
data = {'user_name': 'alex', 'date': '19.02.2023', 'email': '123@mail.ru'}

data2 = {'user_name': 'alex', 'phone_number': '+7 989 576 98 54'}


response = requests.post(url, data=data)
response2 = requests.post(url, data=data2)

print(response.json())
print(response2.json())