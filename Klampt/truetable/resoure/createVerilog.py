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

		for j in range(0,1024): #all edge
			strData = 'edge_mask['+str(j)+']='
			for i in range(0,32768): #all pix
				if  trueTable[i][j] == 1 :
					fun = bin(i)
					lenth = len(fun)
					while ( lenth < 17 ):
						fun = fun + '0'
						lenth = lenth + 1
					if ( fun[2] == '1' ):
						strData = strData + 'O '
					else :
						strData = strData + 'O` '
					if ( fun[3] == '1' ):
						strData = strData + 'N '
					else :
						strData = strData + 'N` '
					if ( fun[4] == '1' ):
						strData = strData + 'M '
					else :
						strData = strData + 'M` '
					if ( fun[5] == '1' ):
						strData = strData + 'L '
					else :
						strData = strData + 'L` '
					if ( fun[6] == '1' ):
						strData = strData + 'K '
					else :
						strData = strData + 'K` '
					if ( fun[7] == '1' ):
						strData = strData + 'J '
					else :
						strData = strData + 'J` '
					if ( fun[8] == '1' ):
						strData = strData + 'I '
					else :
						strData = strData + 'I` '
					if ( fun[9] == '1' ):
						strData = strData + 'H '
					else :
						strData = strData + 'H` '
					if ( fun[10] == '1' ):
						strData = strData + 'G '
					else :
						strData = strData + 'G` '
					if ( fun[11] == '1' ):
						strData = strData + 'F '
					else :
						strData = strData + 'F` '
					if ( fun[12] == '1' ):
						strData = strData + 'E '
					else :
						strData = strData + 'E` '
					if ( fun[13] == '1' ):
						strData = strData + 'D '
					else :
						strData = strData + 'D` '
					if ( fun[14] == '1' ):
						strData = strData + 'C '
					else :
						strData = strData + 'C` '
					if ( fun[15] == '1' ):
						strData = strData + 'B '
					else :
						strData = strData + 'B` '
					if ( fun[16] == '1' ):
						strData = strData + 'A'
					else :
						strData = strData + 'A`'

					strData = strData + '+'

			strData = strData + ';\n'
			verilogFile.write(strData)




		pass
	#print trueTable

	pass


load_trueTable()
write_verilog()
print 'done!'



