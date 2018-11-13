import sys
import time

import json

import time

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

	nowtime = time.localtime(time.time())

	with open('./prm_LUT.v','w') as verilogFile:

		strSyntax = '/*******************************************\n'
		strSyntax = strSyntax + '****** Wuhan university of technology ******\n'
		strSyntax = strSyntax + '****** Ruige Lee ******\n'
		strSyntax = strSyntax + 'year: ' + str(nowtime.tm_year) + '\n'
		strSyntax = strSyntax + 'month: ' + str(nowtime.tm_mon) + '\n'
		strSyntax = strSyntax + 'date: ' + str(nowtime.tm_mday) + '\n'
		strSyntax = strSyntax + 'hour: ' + str(nowtime.tm_hour) + '\n'
		strSyntax = strSyntax + 'minutes: ' + str(nowtime.tm_min) + '\n'
		strSyntax = strSyntax + 'second: ' + str(nowtime.tm_sec) + '\n'
		strSyntax = strSyntax + '********************************************/\n\n'



		strSyntax = strSyntax +'module prm_LUT_chk(\n'
		strSyntax = strSyntax + '	input [4:0] X,\n'
		strSyntax = strSyntax + '	input [5:0] Y,\n'
		strSyntax = strSyntax + '	input [5:0] Z,\n'
		strSyntax = strSyntax + '	output [1033:0] edge_mask\n'
		strSyntax = strSyntax + ');\n\n'
		strSyntax = strSyntax + '	reg [1033:0] edge_mask_reg;\n'
		strSyntax = strSyntax + '	assign edge_mask = edge_mask_reg;\n\n'
		strSyntax = strSyntax + 'always @( *) begin\n' 


		verilogFile.write(strSyntax);
		for j in range(0,1034): #all edge
			strData = '    case({X,Y,Z})\n'
			
			for i in range(0,16384): #all pix
				if (trueTable[i][j] == 1):
					strData = strData + '		14\'b' + bin(i)[2:16] +',\n'
			strData = strData[0:-2]
			strData = strData + ': edge_mask_reg[' + str(j) + '] <= 1\'b1;\n '
			strData = strData + '		default: edge_mask_reg[' + str(j) + '] <= 1\'b0;\n '
			strData = strData + '	endcase\n\n'
			verilogFile.write(strData)

		strSyntax =  'end\n'
		strSyntax = strSyntax + 'endmodule\n\n'

		verilogFile.write(strSyntax) 

	pass


load_trueTable()
write_verilog()
print 'done!'



