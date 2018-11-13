import sys
import time
import os

for i in range(0,1024):
	os.system('./espresso ./epressoTable'+str(i)+' >> ./result/singleRes'+str(i))
	print i
print 'done!'