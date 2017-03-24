#Use single particle "zoom" run and static field data to generate pic of Spizer orbit

import sys
import numpy as np
import os
import datetime
from visit import *
from visit_utils import *
from visit_utils.common import lsearch #lsearch(dir(),"blah")
import pyVisit as pyv
import lfmPostproc as lfmpp
import random

#Quiet = Do silently, open up GUI
Quiet = False
doProd = True #Do high-res lines

doConfig1 = True

SrcF = "fld.vti"
#SrcF = "fldLorez.vti"

#All particles
np.random.seed(31337)
random.seed(31337)

if (doConfig1):
	#Config O+
	SrcP = "O.100keV.ZoomID.000032.h5part"
	I = [700,750,800,850,900,950,1000,1050,1075,1100,1150]
else:
	#Config H+
	SrcP = "../H100/H.100keV.ZoomID.000010.h5part"
	I = [14000,14500,15000,15100,15200,15300,15400,15600]


#How many fields to trace
NumT = 30 #How many to trace


tRadFld=0.00125 #Field line thickness
tRadTrj=0.0025 #Particle trajectory thickness

FldCmap = "Autumn" #Winter,YlGnBu,YlGn
SlcCmap = "viridis"


#Read some data from file
pId = 0 #Only using single particle H5ps
# t,tCr = lfmpp.getH5pid(SrcP,"tCr",pId)
# t,xCr = lfmpp.getH5pid(SrcP,"xCr",pId)
# t,yCr = lfmpp.getH5pid(SrcP,"yCr",pId)
# t,zCr = lfmpp.getH5pid(SrcP,"zCr",pId)
t,xP  = lfmpp.getH5pid(SrcP,"x",pId)
t,yP  = lfmpp.getH5pid(SrcP,"y",pId)
t,zP  = lfmpp.getH5pid(SrcP,"z",pId)
t,mp  = lfmpp.getH5pid(SrcP,"mp",pId)

#Pick trajectory points to trace at
i0 = 0 #First step
i1 = mp.argmax() #Last step before loss from sim
print(i0,i1)


# I = random.sample(range(i0,i1),NumT)
# I.sort()

Ns = len(I) #Number of seeds
print("Particle alive between %f and %f"%(t[i0],t[i1]))
print("Using %d seeds from crossings"%(Ns))
print(t[I])

#Turn points into list
x = xP[I]
y = yP[I]
z = zP[I]


#Now do visit initialization
if (Quiet):
        LaunchNowin()
else:
        Launch()

#Do some defaults
pyv.lfmExprsEB()
pyv.pvInit()

#Field data
OpenDatabase(SrcF)
pyv.lfmPCol(SrcF,"Bmag",vBds=[1,500],cMap=SlcCmap,pcOpac=0.85,Legend=False,Log=True)

AddOperator("Slice")
sOp = GetOperatorOptions(0)
sOp.axisType = 2
sOp.project2d = 0
#print(sOp)
SetOperatorOptions(sOp)

#Do field lines
pyv.lfmStream(SrcF,"Bfld",x,y,z,cMap=FldCmap,tRad=tRadFld,Legend=False)
icOp = GetOperatorOptions(0)
icOp.criticalPointThreshold = 0.1
if (not doProd):
	icOp.maxSteps = 50
	icOp.relTol = 1e-04
	icOp.absTolAbsolute = 1.0e-4
SetOperatorOptions(icOp)

#Change to constant colors
pcOp = GetPlotOptions()
pcOp.minFlag = 1
pcOp.maxFlag = 1
pcOp.min = -5.0
pcOp.max = -4.0
SetPlotOptions(pcOp)

#Display some of the configs
print(icOp)
print(pcOp)

AddOperator("Tube")
tOp = GetOperatorOptions(1)
tOp.radiusFractionBBox = tRadFld
tOp.fineness = 10
tOp.capping = 1
SetOperatorOptions(tOp)

#Block out central cutout
AddPlot("Contour","RadAll")
cOps = GetPlotOptions()
cOps.colorType = 0
cOps.singleColor = (0, 0, 0, 255)
cOps.singleColor = (192, 192, 192, 255)
cOps.contourMethod = 1
cOps.contourValue = (2.2)
cOps.legendFlag = 0
SetPlotOptions(cOps)

#Particles
OpenDatabase(SrcP)
ActivateDatabase(SrcP)

Nt = TimeSliderGetNStates()
#print(Nt)
DefineScalarExpression("Trap","Op+Om")
pyv.lfmPCol(SrcP,"Trap",cMap="Cool",vBds=[0,1],Legend=False,Light=True,Inv=False)
pOp = GetPlotOptions()
SetPlotOptions(pOp)

AddOperator("PersistentParticles")
ppOp = GetOperatorOptions(0)

ppOp.stopIndex = Nt
ppOp.connectParticles = 1
ppOp.indexVariable = "id"
ppOp.stride = 1
#print(ppOp)
SetOperatorOptions(ppOp)

AddOperator("Tube")
tOp = GetOperatorOptions(1)
tOp.radiusFractionBBox = tRadTrj
tOp.fineness = 10
tOp.capping = 1
#print(tOp)
SetOperatorOptions(tOp)
w3d = GetView3D()
if (doConfig1):
	w3d.viewNormal = (-0.0197239, 0.985998, 0.165585)
	w3d.focus = (-1.025, 0, 0.000166655)
	w3d.viewUp = (0.00953341, -0.165424, 0.986176)
	w3d.viewAngle = 30
	w3d.parallelScale = 25.6497
	w3d.nearPlane = -51.2994
	w3d.farPlane = 51.2994
	w3d.imagePan = (0.0874301, 0.0139772)
	w3d.imageZoom = 3.79749
	w3d.perspective = 1
	w3d.eyeAngle = 2
	w3d.centerOfRotationSet = 0
	w3d.centerOfRotation = (-1.025, 0, 0.000166655)
	w3d.axis3DScaleFlag = 0
	w3d.axis3DScales = (1, 1, 1)
	w3d.shear = (0, 0, 1)
	w3d.windowValid = 0
else:
	#Doing H+
	w3d.viewNormal = (0.973617, 0.0921289, 0.208763)
	w3d.focus = (-1.025, 0, 0.00223994)
	w3d.viewUp = (-0.209201, -0.00498575, 0.97786)
	w3d.viewAngle = 30
	w3d.parallelScale = 25.6503
	w3d.nearPlane = -51.3007
	w3d.farPlane = 51.3007
	w3d.imagePan = (-0.0645008, 0.0175247)
	w3d.imageZoom = 3.7975
	w3d.perspective = 1
	w3d.eyeAngle = 2
	w3d.centerOfRotationSet = 0
	w3d.centerOfRotation = (-1.025, 0, 0.00223994)
	w3d.axis3DScaleFlag = 0
	w3d.axis3DScales = (1, 1, 1)
	w3d.shear = (0, 0, 1)
	w3d.windowValid = 1	
SetView3D(w3d)



DrawPlots()
#pyv.cleanLegends(plXs,plYs,plTits)

pyv.setAtts()

SaveWindow()
if (not Quiet):
	OpenGUI()
