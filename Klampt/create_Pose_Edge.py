from klampt import *
from klampt.model.collide import *
import sys
import time
from klampt.sim import *
from klampt import vis

import json

import random

Pose = [[0,0,0,0,0,0]]
edgeIndex = []

def create_Pose_Edge():
	poseCnt = 0;
	edgeCnt = 0;
	while(edgeCnt < 1034):
		shoulderConfig = random.uniform(-180 , 0)
		armConfig = random.uniform(0 , 180)
		elbowConfig = random.uniform(0 , 180)
		wristConfig = random.uniform(-90 , 90)
		fingerConfig = random.uniform(-90 , 90)
		toolConfig = random.uniform(-90 , 90)

		# print shoulderConfig
		# print armConfig
		# print elbowConfig
		# print wristConfig
		# print fingerConfig
		# print toolConfig

		Pose.append([shoulderConfig,armConfig,elbowConfig,wristConfig,fingerConfig,toolConfig])
		poseCnt = poseCnt + 1

		for i in range(0,poseCnt):
			#print Pose[i][0]
			#print Pose[poseCnt][0]
			shoulderDis = abs( Pose[i][0] - Pose[poseCnt][0] )
			armDis = abs( Pose[i][1] - Pose[poseCnt][1] )
			elbowDis = abs( Pose[i][2] - Pose[poseCnt][2] )
			# wristDis = abs( Pose[i][3] - Pose[poseCnt][3] )
			# fingerDis = abs( Pose[i][4] - Pose[poseCnt][4] )
			# toolDis = abs( Pose[i][5] - Pose[poseCnt][5] )

			if ( ( shoulderDis + armDis + elbowDis  ) < 180 ):
				edgeIndex.append([i,poseCnt])
				edgeCnt = edgeCnt + 1




create_Pose_Edge()

print Pose
data = json.dumps(Pose)

with open('./pose.json','w') as poseFile:
	poseFile.write(data)

print edgeIndex
data = json.dumps(edgeIndex)
with open('./edgeIndex.json','w') as edgeIndexFile:
	edgeIndexFile.write(data)



