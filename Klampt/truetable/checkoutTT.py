import sys
import time

import json



trueTable = []
edge = []

def load_empty_trueTable():
	global trueTable

	with open('./trueTable.json','r') as trueTableFile:
		data = trueTableFile.read()
		trueTable = json.loads(data)
	#print trueTable

	pass


def load_edge():

	global edge

	with open('../edge.json','r') as edgeFile:
		data = edgeFile.read()
		edge = json.loads(data)
		#print edge
	pass

def checkout_Truetable():

	global edge
	global trueTable

	for i in xrange(0,1034):#check all edge
		for j in xrange(0,16384):#check all pix
			trueTable[j][i] = edge[i][j]
	pass

	data = json.dumps(trueTable)
	with open('./trueTable.json','w') as ttFile:
		ttFile.write(data)

	pass



load_edge()
load_empty_trueTable()
checkout_Truetable()


