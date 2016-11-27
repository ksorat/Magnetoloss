#Plots 3D field tracings over 2D phi slice

import numpy as np
import os
from visit import *
from visit_utils import *
from visit_utils.common import lsearch #lsearch(dir(),"blah")
import lfmGrids as lfm
import pyVisit as pyv

#fIn = "fldDatLorez.vti"
fIn = "fldDat.vti"
db = fIn
Quiet = True

PhiCs = [0,30,45,60,75]
LatCs = [25,25,22.5,20,15]

Nl = 3
Nr = 10
dLam = 5 #+/ from critical latitude


#Rc = 10.5 #
Rc0 = 9.5
Rc1 = 11.5

dpMax = 7.5
dBzMax = 35

Np = 2*Nl*Nr
#Theta = np.linspace(30,150,Nl)
Theta = np.linspace(-dLam,dLam,Nl)
Rad = np.linspace(Rc0,Rc1,Nr)

pcOpac = 0.75
pcOpacP = 0.5

if (Quiet):
	LaunchNowin()
else:
	Launch()

OpenDatabase(fIn)
md = GetMetaData(fIn) #Metadata

#Import definitions
pyv.lfmExprsEB()

#Start plotting
pyv.setAtts() #Some defaults

Nphi = len(PhiCs)
radScl = np.pi/180.0
for k in range(Nphi):
	PhiC = PhiCs[k]
	LatC = LatCs[k]

	fOut = "Slc.P%d.png"%np.int(PhiC)
	#Generate seed points
	Cp = np.cos(PhiC*radScl)
	Sp = np.sin(PhiC*radScl)
	ThCp = 90 - LatC #Critical latitudes in theta
	ThCm = 90 + LatC

	x = np.zeros(Np); y = np.zeros(Np); z = np.zeros(Np)
	n=0
	for i in range(Nr):
		for j in range(Nl):

			thP = (ThCp + Theta[j])*radScl
			thM = (ThCm + Theta[j])*radScl
			R = Rad[i]

			x[n] = R*Cp*np.sin(thP)
			y[n] = R*Sp*np.sin(thP)
			z[n] = R*   np.cos(thP)

			x[n+1] = R*Cp*np.sin(thM)
			y[n+1] = R*Sp*np.sin(thM)
			z[n+1] = R*   np.cos(thM)

			n=n+2

	dPhiStr = "Phi-%f"%(PhiC)
	
	DefineScalarExpression("dPhi",dPhiStr)
	
	
	print("Generating %d streamlines\n"%(Nr*Nl))
	# pyv.lfmPCol(db,"dBz",vBds=(-dBzMax,dBzMax),Inv=True,pcOpac=pcOpac,Light=False)
	
	# #Field slice, equatorial
	# AddOperator("Slice")
	# sOps = GetOperatorOptions(0); 
	# sOps.axisType=2; sOps.project2d=0
	# SetOperatorOptions(sOps)
	
	#Add phi slice
	pyv.lfmPCol(db,"dBz",vBds=(-dBzMax,dBzMax),Inv=True,pcOpac=pcOpacP,Light=False,Legend=False)
	
	AddOperator("Slice")
	sOps = GetOperatorOptions(0); 
	sOps.axisType=4; sOps.project2d=0
	sOps.phi = 0; sOps.theta = PhiC
	SetOperatorOptions(sOps)
	
	#Block out central cutout
	AddPlot("Contour","RadAll")
	cOps = GetPlotOptions()
	cOps.contourMethod = 1
	cOps.contourValue = (2.2)
	cOps.legendFlag = 0
	SetPlotOptions(cOps)
	
	#Block out critical latitude
	AddPlot("Contour","MLat")
	cOps = GetPlotOptions()
	cOps.contourMethod = 1
	cOps.contourValue = tuple([-LatC,LatC])
	cOps.legendFlag = 0
	cOps.lineWidth = 2
	cOps.colorType = 0
	SetPlotOptions(cOps)
	AddOperator("Slice")
	sOps = GetOperatorOptions(0); 
	sOps.axisType=4; sOps.project2d=0
	sOps.phi = 0; sOps.theta = PhiC
	SetOperatorOptions(sOps)

	#Do streams
	pyv.lfmStream(fIn,"Bfld",x,y,z,cMap="Cool",tRad=0.0015,Legend=False)
	icOp = GetOperatorOptions(0)
	icOp.dataValue = 10
	icOp.dataVariable = "dPhi" 
	SetOperatorOptions(icOp)

	pcOp = GetPlotOptions()
	pcOp.minFlag=1; pcOp.maxFlag=1
	pcOp.min = -dpMax; pcOp.max = dpMax
	SetPlotOptions(pcOp)

	pyv.SetWin3D(Ax=2,Ang=-PhiC)
	pyv.SetWin3D(Ax=0,Ang=-90)
	pyv.SetWin3D(Zoom=3)
	pyv.ShiftWin3D(-.185,0)

	#Create labels
	mltHr = np.int(PhiC/15) + 12
	mltStr = "MLT %d:00"%mltHr
	lcStr = "Critical Latitude = %d"%np.int(LatC)

	mltLab = pyv.genTit(mltStr,Pos=(0.025,0.1) )
	lcLab = pyv.genTit(lcStr,Pos=(0.025,0.075))
	lcLab.height = 0.015

	#Show them all
	DrawPlots()
	print("Writing to %s at Phi=%f"%(fOut,PhiC))

	swa = GetSaveWindowAttributes()
	swa.fileName = fOut
	SetSaveWindowAttributes(swa)
	SaveWindow()
	ResetView()
	DeleteAllPlots()

	pyv.killAnnotations()
	#Run trim on file
	#ComS = 'convert tmpVid/%s'%fOut + ' -trim -border 20x20 -bordercolor "#FFFFFF" P%d.png'%np.int(PhiC)
	ComS = 'convert tmpVid/%s'%fOut + ' -trim P%d.png'%np.int(PhiC)
	os.system(ComS)
