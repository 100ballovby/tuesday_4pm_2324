with open('test.txt', 'w') as f:  # записать в файл новую строку (перезаписав его содержимое)
	f.write('Hello, world! This is my first file writing operation!')

with open('test.txt', 'a') as f:  # добавить что-то в файл
	f.write('There is a new line of text!')
