from klampt import *
from klampt.model.collide import *
import sys
import time
from klampt.sim import *
from klampt import vis

import json

import random

Pose = [[0,0,0,0,0,0]]

def create_Pose():
	for i in xrange(0,50):
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

create_Pose()

data = json.dumps(Pose)
#print json.loads(data)[1][3]

with open('./pose.json','w') as poseFile:
		poseFile.write(data)



