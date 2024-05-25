import os
import random
from datetime import datetime

now_date = str(datetime.now().date())
now_time = str(datetime.now().time())
f_name = 'folder_' + now_date + '_' + now_time
os.mkdir(f_name)

for i in range(10):
	with open(os.path.join(f_name, f'file_{i}.txt'), 'w') as f:
		num = str(random.randint(-100, 100))
		f.write(num)
