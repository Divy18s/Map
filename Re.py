import requests

r=requests.get('http://127.0.0.1:5000/Todo3')

print(r.content)