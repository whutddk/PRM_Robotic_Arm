from klampt import *
from klampt.model.collide import *
import sys
import time
from klampt.sim import *
from klampt import vis

if __name__ == "__main__":
	if len(sys.argv)<=1:
		print "USAGE: visualize_world.py [world_file]"
		exit()
	world = WorldModel()
	for fn in sys.argv[1:]:
		res = world.readFile(fn)
		if not res:
			raise RuntimeError("Unable to load model "+fn) 
	vis.add("world",world)
	sim = Simulator(world)
	robot = world.robot(0)
	#endeffectors = [robot.numLinks()-1]
	collisionTest = WorldCollider(world)
	#controller = sim.getController(0)
	
	robotPose = RobotPoser(robot)
	print robotPose.get()
	

	
	
	#sim.reset()
	#sim.getStatus()
	#base = sim.body(world.robotLink(0,0))
	#shoulder = sim.body(world.robotLink(0,1))
	#arm = sim.body(world.robotLink(0,2))
	#elbow = sim.body(world.robotLink(0,3))
	#wrist = sim.body(world.robotLink(0,4))
	#finger = sim.body(world.robotLink(0,5))
	#tool = sim.body(world.robotLink(0,6))
	#body = sim.body(world.rigidObject(1))
	#body.applyForceAtPoint ([0,2000,200],[0,0,0])

	#print base.getVelocity()
	#print shoulder.getVelocity()
	#print arm.getVelocity()
	#print elbow.getVelocity()
	#print wrist.getVelocity()
	#print finger.getVelocity()
	#print tool.getVelocity()
	
	vis.show()

	#shoulder.enableDynamics(False)
	#arm.enableDynamics(False)
	#elbow.enableDynamics(False)
	#wrist.enableDynamics(False)
	#finger.enableDynamics(False)
	#tool.enableDynamics(False)
	
	#shoulder.setVelocity((1,0,0),(0,0,0))
	#arm.setVelocity((0,0,0),(0,0,0))
	#elbow.setVelocity((0,0,0),(0,0,0))
	#wrist.setVelocity((0,0,0),(0,0,0))
	#finger.setVelocity((0,0,0),(0,0,0))
	#tool.setVelocity((0,0,0),(0,0,0))


	#t0 = time.time()
	for i in range(0,100):
		vis.shown()
		#sim.simulate(0.01)
		robotPose.set([0,0.0157*i,-0.0157*i,-0.0157*i,0,0,0])
		collisionTest = WorldCollider(world)
		#for i,j in  collisionTest.robotTerrainCollisions(0):
		for i,j in collisionTest.robotTerrainCollisions(0):
			print j.getName()
			
		
		#t1 = time.time()
	#update your code here	       
		time.sleep(0.1)
		#t0 = t1
