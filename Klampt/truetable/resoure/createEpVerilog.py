import sys
import time

for k in range(0,1024):
with open('./singleVerilog/singleV','w') as vFile:

		with open('./single/result/singleRes'+str(k),'r') as epressFile:
			vFile.write('casez(edge_mask['+str(k)+'])\n')
			vFile.write(epressFile.readlines()[3:-1])

			#vFile.write(data)
