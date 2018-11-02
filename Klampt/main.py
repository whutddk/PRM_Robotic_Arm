from klampt import *
from klampt.model.collide import *
import sys
import time
from klampt.sim import *
from klampt import vis


def make_testing_mesh(world):
	"""automatically create a mesh test grid
	"""

	for z in range(0,31):
		for y in range (0,31):
			for x in range (0,31):
				grid = Geometry3D()

				grid.loadFile("terrains/cube.off")

				grid.transform([0.032,0,0,0,0.032,0,0,0,0.032],[0.032*x - 0.512,0.032*y- 0.512,0.032*z])
					

	
				

				Mesh = world.makeTerrain("Grid" + str(x) + "," + str(y) + "," + str(z))

				Mesh.geometry().set(grid)
				Mesh.appearance().setColor(0.3,0.1,0.1,0.5)
	return 




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
	sim = Simulator(world)
	robot = world.robot(0)

	collisionTest = WorldCollider(world)
	
	robotPose = RobotPoser(robot)
	
	#print robotPose.get()
	
	for i in range(0,100):
		#vis.shown()

		robotPose.set([0,-0.0157*i,-0.0157*i,-0.0157*i,-0.0157*i,-0.0157*i,0])
		collisionTest = WorldCollider(world)

		cnt = 0;
		for i,j in collisionTest.robotTerrainCollisions(0):
			#print j.getName()
			cnt = cnt + 1;
		print "cnt in this frame"
		print cnt

			#pass
			

