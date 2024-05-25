with open('test.txt', 'w') as f:
	for i in range(1, 11):
		f.write(i * "* " + '\n')
