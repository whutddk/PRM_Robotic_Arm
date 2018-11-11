import sys
import time

import json

trueTable = []

def load_trueTable():
	global trueTable

	with open('../trueTable.json','r') as trueTableFile:
		data = trueTableFile.read()
		trueTable = json.loads(data)
	#print trueTable

	pass


def write_verilog():
	global trueTable

	for j in range(0,1024): #all edge
		with open('./single/epressoTable'+str(j),'w') as epressFile:


		#epressFile.write('.i 15\n.o 1024\n')
			epressFile.write('.i 15\n.o 1\n')

			#for i in range(0,32768): #all pix
			for i in range(0,32768): #all pix
				logicI = bin(i)
				logicInput = ''
				inputlen = len(logicI)

				logicInput = logicI[2:inputlen]
				while(inputlen < 17 ):
					logicInput = '0'+ logicInput
					inputlen = inputlen + 1
				logicInput = logicInput +' '
				#print (logicInput)
				logicOutput = ''
				#for j in range(0,1024): #all edge
				
				logicOutput = logicOutput+str(trueTable[i][j])
				logicOutput = logicOutput +'\n'
					#strData = 'assign edge_mask['+str(j)+']=('
				pass
					
				epressFile.write(logicInput+logicOutput)


		pass
	#print trueTable

	pass


load_trueTable()
write_verilog()
print 'done!'



