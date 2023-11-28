import requests as r

url = 'https://jsonplaceholder.typicode.com/todos'
response = r.get(url).json()  # обратиться по ссылке и получить json

completed = 0
not_completed = 0
task_quantity = 0  # общее количество задач
for todo in response:
    if todo["completed"]:
        completed += 1
    else:
        not_completed += 1

task_quantity = completed + not_completed
print(f'Выполнено задач: {completed}')
print(f'Не выполнено задач: {not_completed}')
print(f'Общее количество задач: {task_quantity}')
print(f'Процент выполненных задач: {(completed / task_quantity) * 100}%')
