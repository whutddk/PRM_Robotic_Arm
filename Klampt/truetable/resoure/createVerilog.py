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

	with open('./PRMM.v','w') as verilogFile:

		# for i in range(0,32768):	#all case all pix
		# 	#strSyntax =  '15\'d'+ str(i) + ': edgeMask <= 1034\'b'
		# 	strData = ''
		# 	for j in range(0,1024): # all edge
		# 		strData = strData + str(trueTable[i][j]) + ','
		# 	#strSyntax = strSyntax + strData + ';\n'
		# 	strData = strData +'\n'
		# 	verilogFile.write(strData)
		# 	#print strSyntax

		for j in range(0,1024): # all edge
			strSyntax = 'always @(*) begin\n case({A,B,C,D,E,F,G,H,I,J,K,L,M,N,O})\n'
			for i in range(0,32768):	#all case all pix
				if ( trueTable[i][j] == 1 ):
					strSyntax = strSyntax + bin(i) + ',\n'
			strSyntax = strSyntax + ':edge_mask_reg[' + str(j) +'] <= 1\'b1;\ndefault:edge_mask_reg[' + str(j) +'] <= 1\'b0;\n endcase \n end\n\n'
			verilogFile.write(strSyntax)



		pass
	#print trueTable

	pass


load_trueTable()
write_verilog()
print 'done!'



