import sys
import time

for k in range(0,1024):
	with open('./singleVerilog/singleV'+str(k),'w') as vFile:
		with open('./single/result/singleRes'+str(k),'r') as epressFile:
			data = epressFile.readlines()[3:-1]
			for line in data:
				vFile.write(line)

			#vFile.write(data)
