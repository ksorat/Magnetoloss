import sys
import numpy as np
import datetime
from visit import *
from visit_utils import *
from visit_utils.common import lsearch #lsearch(dir(),"blah")
import pyVisit as pyv

Quiet = False
Nt = 200
Base = "~/Work/magnetoloss/"
EqDir = Base + "eqSlc" #eqSlc database
Src0 = EqDir + "/eqSlc.*.vti database"
dbs = [Src0]

Nr = 4
Np = 2
Rad = [6,9.5]
r = np.linspace(Rad[0],Rad[1],Nr)
phi = np.linspace(0,2*np.pi,Np)
phi = np.linspace(-np.pi/2,np.pi/2,Np)


x = [];y=[];z=[]
for j in range(Np):
	for i in range(Nr):
	
		xij = r[i]*np.cos(phi[j])
		yij = r[i]*np.sin(phi[j])
		x.append(xij)
		y.append(yij)
		z.append(0)
#dBz
abBz = 25;
dBzBds = [-abBz,abBz]

if (Quiet):
        LaunchNowin()
else:
        Launch()

#Do some defaults
#pyv.setAtts() #Some defaults
pyv.lfmExprs()

#Open databases
OpenDatabase(dbs[0])

#Field stuff
pyv.lfmPCol(dbs[0],"dBz",vBds=dBzBds,pcOpac=0.7,Inv=True)

#Pathline plot
#Do streams
pyv.lfmStream(dbs[0],"V2D",x,y,z,cMap="Cool",dx=0.005,bothDir=False)

SetTimeSliderState(Nt)

#Show
DrawPlots()