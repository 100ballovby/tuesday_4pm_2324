import requests as r

url = 'https://jsonplaceholder.typicode.com/todos'
response = r.get(url).json()  # обратиться по ссылке и получить json

for todo in response:
    if not todo["completed"]:
        print(todo)
