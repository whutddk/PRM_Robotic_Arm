import sys
import time

import json

trueTable = []

def create_empty_trueTable():
	global trueTable

	output = [ 0 for k in xrange(0,1034) ]
	
	#print output
	for i in xrange(0,32768):
		trueTable.append(output)
	#print trueTable
	
	data = json.dumps(trueTable)
	with open('./trueTable.json','w') as poseFile:
		poseFile.write(data)

	pass


create_empty_trueTable()



