import sys
import time

with open ('./singleVerilog/singleV.v','w') as vFile:
	for k in range(0,1024):
		with open('./singleVerilog/singleV'+str(k),'r') as epressFile:
			vFile.write('casez({A,B,C,D,E,F,G,H,I,J,K,L,M,N,O})\n')
			lines = epressFile.readlines()
			string = ''
			for data in lines:
				string = string + '	15\'b'+data[0:15]+',\n'
			string = string[0:-2]
			vFile.write(string)
			vFile.write(': edge_mask['+str(k)+'] <= 1\'b1')
			vFile.write(';\n	default:edge_mask['+str(k)+'] <= 1\'b0;\nendcase\n\n')

				#vFile.write(data)
