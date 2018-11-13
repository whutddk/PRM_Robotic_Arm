from klampt import *
from klampt.model.collide import *
import sys
import time
from klampt.sim import *
from klampt import vis

import json

import random

Pose = []
edge = []
edgeIndex = []

trueTable = []

def make_testing_mesh(world):
	"""automatically create a mesh test grid
	"""

	for z in range(0,32):
		for y in range (0,32):
			for x in range (0,16):
				grid = Geometry3D()

				grid.loadFile("terrains/cube.off")

				grid.transform([0.032,0,0,0,0.032,0,0,0,0.032],[0.032*y - 0.512,0.032*x-0.512,0.032*z])			

				Mesh = world.makeTerrain("Grid," + "%3d"%x + "," + "%3d"%y + "," + "%3d"%z)

				Mesh.geometry().set(grid)
				Mesh.appearance().setColor(0.3,0.1,0.1,0.1)
	return 

def load_Pose():
	global Pose
	global edgeIndex
	global edge

	with open('./pose.json','r') as poseFile:
		data = poseFile.read()
		Pose = json.loads(data)
		print Pose
	pass

def load_edge():
	global Pose
	global edgeIndex
	global edge

	with open('./edge.json','r') as edgeFile:
		data = edgeFile.read()
		edge = json.loads(data)
		#print edge

def load_Index():

	global Pose
	global edgeIndex
	global edge

	with open('./edgeIndex.json','r') as edgeIndexFile:
		data = edgeIndexFile.read()
		edgeIndex = json.loads(data)
		
		print edgeIndex

def store_Edge():
	global Pose
	global edgeIndex
	global edge

	with open('./edge.json','w') as edgeFile:
		data = json.dumps(edge)
		edgeFile.write(data)
	pass



def create_Edge(Index):

	global Pose
	global edgeIndex
	global edge

	print "now Create Edge:"
	print Index
	print edgeIndex[Index]

	i = edgeIndex[Index][0]
	j = edgeIndex[Index][1]

	shoulderStart = Pose[j][0] / 180 * 3.14159
	armStart = Pose[j][1] / 180 * 3.14159
	elbowStart = Pose[j][2] / 180 * 3.14159
	wristStart = Pose[j][3] / 180 * 3.14159
	fingerStart = Pose[j][4] / 180 * 3.14159
	toolStart = Pose[j][5] / 180 * 3.14159

	shoulderEnd = Pose[i][0] / 180 * 3.14159
	armEnd = Pose[i][1] / 180 * 3.14159
	elbowEnd = Pose[i][2] / 180 * 3.14159
	wristEnd = Pose[i][3] / 180 * 3.14159
	fingerEnd = Pose[i][4] / 180 * 3.14159
	toolEnd = Pose[i][5] / 180 * 3.14159

	shoulderDis = (shoulderEnd - shoulderStart) / 100
	armDis = (armEnd - armStart) / 100
	elbowDis = ( elbowEnd - elbowStart ) / 100
	wristDis = ( wristEnd - wristStart ) / 100
	fingerDis = ( fingerEnd - fingerStart ) / 100
	toolDis = ( toolEnd - toolStart ) / 100

	oneEdge = [0 for m in xrange(0,16384)]

	for k in range (0,101):
		time.sleep(0.01)
		robotPose.set([0,shoulderStart + shoulderDis*k,- (armStart + armDis*k),-(elbowStart + elbowDis*k),- (wristStart + wristDis*k),-(fingerStart + fingerDis*k),toolStart + toolDis*k])
		collisionTest = WorldCollider(world)

		cnt = 0;
		for p,q in collisionTest.robotTerrainCollisions(0):
			result = q.getName()
			
			#print q.getName()
			x = int(result[5:8])
			y = int(result [9:12])
			z = int(result[13:16])
			oneEdge[1024*x+32*y+z] = 1
			cnt = cnt + 1;
		print "cnt in this frame"
		print cnt
	edge.append(oneEdge)
	store_Edge()
	pass

if __name__ == "__main__":
	
	world = WorldModel()

	res = world.readFile('./anno_check.xml')
	if not res:
		raise RuntimeError("Unable to load model ") 
			
	load_Pose()
	load_Index()
	load_edge()

	make_testing_mesh(world)
				
	#vis.add("world",world)
	#sim = Simulator(world)
	robot = world.robot(0)
	#vis.show()
	collisionTest = WorldCollider(world)
	
	robotPose = RobotPoser(robot)
	
	#print robotPose.get()
	while(len(edge) < 1034):
		create_Edge(len(edge))




	#while(1):
		#time.sleep(0.1)
		#vis.shown()
		#pass

			#pass
			

