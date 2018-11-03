from klampt import *
from klampt.model.collide import *
import sys
import time
from klampt.sim import *
from klampt import vis


import random



Pose = [[0,0,0,0,0,0]]



def make_testing_mesh(world):
	"""automatically create a mesh test grid
	"""

	for z in range(0,31):
		for y in range (0,31):
			for x in range (0,31):
				grid = Geometry3D()

				grid.loadFile("terrains/cube.off")

				grid.transform([0.032,0,0,0,0.032,0,0,0,0.032],[0.032*x - 0.512,0.032*y- 0.512,0.032*z])
					

	
				

				Mesh = world.makeTerrain("Grid," + "%3d"%x + "," + "%3d"%y + "," + "%3d"%z)

				Mesh.geometry().set(grid)
				Mesh.appearance().setColor(0.3,0.1,0.1,0.1)
	return 

def create_Pose():
	for i in range(0,31):
		shoulderConfig = random.uniform(-270 , 90)
		armConfig = random.uniform(0 , 180)
		elbowConfig = random.uniform(0 , 180)
		wristConfig = random.uniform(-180 , 180)
		fingerConfig = random.uniform(-90 , 90)
		toolConfig = random.uniform(-180 , 180)

		#print shoulderConfig
		#print armConfig
		#print elbowConfig
		#print wristConfig
		#print fingerConfig
		#print toolConfig

		Pose.append([shoulderConfig,armConfig,elbowConfig,wristConfig,fingerConfig,toolConfig])
	#print Pose
	#print Pose[0]
	#pass

def create_Edge():
	for i in range(1,31):
		for j in range (0,i-1):
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

			for k in range (0,100):
				time.sleep(0.01)
				robotPose.set([0,shoulderStart + shoulderDis*k,- (armStart + armDis*k),-(elbowStart + elbowDis*k),- (wristStart + wristDis*k),-(fingerStart + fingerDis*k),toolStart + toolDis*k])
				collisionTest = WorldCollider(world)

				cnt = 0;
				for p,q in collisionTest.robotTerrainCollisions(0):
					#print q.getName()
					cnt = cnt + 1;
				#print "cnt in this frame"
				#print cnt
			pass
	pass

def create_truetable():
	pass







if __name__ == "__main__":
	if len(sys.argv)<=1:
		print "USAGE: visualize_world.py [world_file]"
		exit()
	world = WorldModel()
	for fn in sys.argv[1:]:
		res = world.readFile(fn)
		if not res:
			raise RuntimeError("Unable to load model "+fn) 
			
			
	make_testing_mesh(world)
			
			
	vis.add("world",world)
	#sim = Simulator(world)
	robot = world.robot(0)
	vis.show()
	collisionTest = WorldCollider(world)
	
	robotPose = RobotPoser(robot)
	
	#print robotPose.get()
	
	create_Pose()
	#create_Edge()
	for i in range(0,100):
		#vis.shown()

		robotPose.set([0,-0.0157*i,-0.0157*i,-0.0157*i,-0.0157*i,-0.0157*i,0])
		collisionTest = WorldCollider(world)

		cnt = 0;
		for k,j in collisionTest.robotTerrainCollisions(0):
			result = j.getName()
			print result[5:8] + result [9:12] + result[13:16]
			cnt = cnt + 1;
		print "cnt in this frame"
		print cnt
		
		time.sleep(0.1)
			#pass
			

