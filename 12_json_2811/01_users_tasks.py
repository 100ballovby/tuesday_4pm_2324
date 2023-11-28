import requests as req

url = 'https://jsonplaceholder.typicode.com/'
todos = req.get(url + 'todos').json()
users = req.get(url + 'users').json()

users_list = {}
for user in users:
    users_list[user['id']] = {'name': user['name']}  # создаем новую пару ключ-значение

print(users_list)

quantity = 0
for todo in todos:
    if todo['userId'] == 5 and todo['completed']:
        quantity += 1

print(f'User {users_list[5]["name"]} has completed {quantity} todos')
# TODO: создать словарь, где ключом будет id пользователя, которому
#  назначили задачу, а значением количество выполненных задач
users_tasks = {}
for task in todos:
    if task['completed']:  # сначала проверяем, выполнена ли задача
        if task['userId'] not in users_tasks:  # проверяем наличие пользователя в списке
            users_tasks[task['userId']] = 1  # добавляем нового пользователя и ставим количество выполненных
        else:
            users_tasks[task['userId']] += 1  # увеличиваем количество выполненных задач

print(users_tasks)

for user in users_list:
    pers = users_list[user]
    pers['completed'] = 0
    pers['not_completed'] = 0
    for todo in todos:
        if todo['userId'] == user:
            if todo['completed']:
                pers['completed'] += 1
            else:
                pers['not_completed'] += 1
print(users_list)
