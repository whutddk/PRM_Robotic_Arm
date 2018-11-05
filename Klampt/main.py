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

trueTable = []
edgeCnt = 0

def make_testing_mesh(world):
	"""automatically create a mesh test grid
	"""

	for z in range(0,32):
		for y in range (0,32):
			for x in range (0,32):
				grid = Geometry3D()

				grid.loadFile("terrains/cube.off")

				grid.transform([0.032,0,0,0,0.032,0,0,0,0.032],[0.032*x - 0.512,0.032*y- 0.512,0.032*z])
					

	
				

				Mesh = world.makeTerrain("Grid," + "%3d"%x + "," + "%3d"%y + "," + "%3d"%z)

				Mesh.geometry().set(grid)
				Mesh.appearance().setColor(0.3,0.1,0.1,0.1)
	return 

def load_Pose():
	with open('./pose.json','r') as poseFile:
		data = poseFile.read()
		Pose = json.loads(data)
		#print Pose[1]
	pass

def load_edge():
	with open('./edge.json','r') as edgeFile:
		data = edgeFile.read()
		edge = json.loads(data)
		print edge


edgeIndex = []
def creat_Index():
	cnt = 0
	for i in xrange(0,50):
		for j in xrange(0,i):
			edgeIndex.append([i,j])
			cnt = cnt + 1
	#print edgeIndex
	#print cnt
	pass

def store_Edge():
	with open('./edge.json','w') as edgeFile:
		data = json.dumps(edge)
		edgeFile.write(data)
	pass



def create_Edge(Index):

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

	oneEdge = []
	
	for k in range (0,101):
		#time.sleep(0.01)
		robotPose.set([0,shoulderStart + shoulderDis*k,- (armStart + armDis*k),-(elbowStart + elbowDis*k),- (wristStart + wristDis*k),-(fingerStart + fingerDis*k),toolStart + toolDis*k])
		collisionTest = WorldCollider(world)

		cnt = 0;
		for p,q in collisionTest.robotTerrainCollisions(0):
			result = q.getName()
			#create_truetable(edgeCnt,int(result[5:8]),int(result [9:12]),int(result[13:16]))
			#print q.getName()
			cnt = cnt + 1;
		print "cnt in this frame"
		print cnt
	edgeCnt = edgeCnt +1
	print "EDGE="
	print edgeCnt
	pass

	pass

def trueTable_init():
	for i in xrange(0,32768):
		trueTable.append([0 for j in range(0,1024)])
	pass

def create_truetable(edge,x,y,z):
	trueTable[1024*x+32*y+z][edge] = 1
	pass

checkWorld = WorldModel()
def check_edge(x,y,z):
	#if (z == 2):
	grid = Geometry3D()
	grid.loadFile("terrains/cube.off")
	grid.transform([0.032,0,0,0,0.032,0,0,0,0.032],[0.032*x - 0.512,0.032*y- 0.512,0.032*z])

	
	Mesh = checkWorld.makeTerrain("Grid," + "%3d"%x + "," + "%3d"%y + "," + "%3d"%z)

	Mesh.geometry().set(grid)
	Mesh.appearance().setColor(0.1,0.1,0.3,0.1)
	pass
	



if __name__ == "__main__":
	
	world = WorldModel()

	res = world.readFile('./anno_check.xml')
	if not res:
		raise RuntimeError("Unable to load model ") 
			
	load_Pose()
	creat_Index()
	load_edge()

	trueTable_init()	
	make_testing_mesh(world)
			
			
	#vis.add("world",world)
	#sim = Simulator(world)
	robot = world.robot(0)
	#vis.show()
	collisionTest = WorldCollider(world)
	
	robotPose = RobotPoser(robot)
	
	#print robotPose.get()
	
	create_Edge()



	#for i in range(0,100):
		#vis.shown()

		#robotPose.set([0,-0.0157*i,-0.0157*i,-0.0157*i,-0.0157*i,-0.0157*i,0])
		#collisionTest = WorldCollider(world)

		#cnt = 0;
		#for k,j in collisionTest.robotTerrainCollisions(0):
			#result = j.getName()
			#print result
			#print result[5:8] + result [9:12] + result[13:16]
			
			#cnt = cnt + 1;
			#check_edge(int(result[5:8]),int(result [9:12]),int(result[13:16]))
		#print "cnt in this frame"
		#print cnt
		
		#time.sleep(0.1)
	#vis.add("world",checkWorld)
	#vis.show()
	#while(1):
		#time.sleep(0.1)
		#vis.shown()
		#pass

			#pass
			

