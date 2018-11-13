import sys
import time


for k in range(0,1024):
	with open ('./logicVerilog/logicV'+str(k)+'.v','w') as vFile:
		vFile.write('module prm_oblgc_chk'+str(k)+'\n(\ninput A,\ninput B,\ninput C,\ninput D,\ninput E,\ninput F,\ninput G,\ninput H,\ninput I,\ninput J,\ninput K,\ninput L,\ninput M,\ninput N,\ninput O,\noutput edge_mask\n);\n')
		vFile.write('assign edge_mask = (')
		with open('./singleVerilog/singleV'+str(k),'r') as epressFile:
			
			lines = epressFile.readlines()
			strData = ''
			for data in lines:

				if ( data[0] == '-' ):
					pass
				elif ( data[0] == '1' ):
					strData = strData + 'O&'
				else :
					strData = strData + '!O&'
				if ( data[1] == '-' ):
					pass
				elif ( data[1] == '1' ):
					strData = strData + 'N&'
				else :
					strData = strData + '!N&'
				if ( data[2] == '-' ):
					pass
				elif ( data[2] == '1' ):
					strData = strData + 'M&'
				else :
					strData = strData + '!M&'
				if ( data[3] == '-' ):
					pass
				elif ( data[3] == '1' ):
					strData = strData + 'L&'
				else :
					strData = strData + '!L&'
				if ( data[4] == '-' ):
					pass
				elif ( data[4] == '1' ):
					strData = strData + 'K&'
				else :
					strData = strData + '!K&'
				if ( data[5] == '-' ):
					pass
				elif ( data[5] == '1' ):
					strData = strData + 'J&'
				else :
					strData = strData + '!J&'
				if ( data[6] == '-' ):
					pass
				elif ( data[6] == '1' ):
					strData = strData + 'I&'
				else :
					strData = strData + '!I&'
				if ( data[7] == '-' ):
					pass
				elif ( data[7] == '1' ):
					strData = strData + 'H&'
				else :
					strData = strData + '!H&'
				if ( data[8] == '-' ):
					pass
				elif ( data[8] == '1' ):
					strData = strData + 'G&'
				else :
					strData = strData + '!G&'
				if ( data[9] == '-' ):
					pass
				elif ( data[9] == '1' ):
					strData = strData + 'F&'
				else :
					strData = strData + '!F&'
				if ( data[10] == '-' ):
					pass
				elif ( data[10] == '1' ):
					strData = strData + 'E&'
				else :
					strData = strData + '!E&'
				if ( data[11] == '-' ):
					pass
				elif ( data[11] == '1' ):
					strData = strData + 'D&'
				else :
					strData = strData + '!D&'
				if ( data[12] == '-' ):
					pass
				elif ( data[12] == '1' ):
					strData = strData + 'C&'
				else :
					strData = strData + '!C&'
				if ( data[13] == '-' ):
					pass
				elif ( data[13] == '1' ):
					strData = strData + 'B&'
				else :
					strData = strData + '!B&'
				if ( data[14] == '-' ):
					pass
				elif ( data[14] == '1' ):
					strData = strData + 'A&'
				else :
					strData = strData + '!A&'


				strData = strData[0:-1] + ')|('

			strData = strData[0:-2] + ';\n'

			vFile.write(strData)
			vFile.write('endmodule')


			

				#vFile.write(data)
