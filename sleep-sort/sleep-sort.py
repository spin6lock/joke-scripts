#-*- coding:utf8 -*-

import subprocess
import random

if __name__ == '__main__':
	random_list = [int(random.random() * 30) for i in range(20)]
	for num in random_list:
		print num
	print "*" * 30
	for num in random_list:
		subprocess.Popen(['./dreamer.py', str(num)])
