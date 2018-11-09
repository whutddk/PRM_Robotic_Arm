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

	with open('./CMemoryTable.c','w') as CFile:

		# for i in range(0,32768):	#all case all pix
		# 	#strSyntax =  '15\'d'+ str(i) + ': edgeMask <= 1034\'b'
		# 	strData = ''
		# 	for j in range(0,1024): # all edge
		# 		strData = strData + str(trueTable[i][j]) + ','
		# 	#strSyntax = strSyntax + strData + ';\n'
		# 	strData = strData +'\n'
		# 	verilogFile.write(strData)
		# 	#print strSyntax
		strSyntax = 'lookUpTrueTable[1048577] = {'
		CFile.write(strSyntax)
		for i in range(0,32768):	#all case all pix			
			for j in range(0,32): # all edge
				result = ''
				for k in range(0,32):
					result = result + str(trueTable[i][j*32+k])
				hexTable = hex(int(result,2)) + ','
				CFile.write(hexTable)
			strSyntax = '\n'
			CFile.write(strSyntax)
		strSyntax = '};\n'
		CFile.write(strSyntax)
				#print hexTable
			




		pass
	#print trueTable

	pass


load_trueTable()
write_verilog()
print 'done!'



