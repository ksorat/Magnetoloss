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
Quiet = False
doProd = False
doRand = True

PhiCs = [0,15,30,45,60,75,90]
LatCs = [25,25,25,22,17,12,7.5]
thR = 60

Nl = 3
Nr = 10
dLam = 5 #+/ from critical latitude

#Rc0 = 8.0
#Rc1 = 11.0
Rc0 = 8.5
Rc1 = 11.0

dpMax = 5.0
dBzMax = 35

Np = 2*Nl*Nr
#Theta = np.linspace(30,150,Nl)
Theta = np.linspace(-dLam,dLam,Nl)
Rad = np.linspace(Rc0,Rc1,Nr)
dR = Rad[1]-Rad[0]

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
#Create points

Nphi = 1
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
	if (doRand):
		DelR = Rc1 - Rc0
		Q1 = np.random.rand(Np)
		Q2 = np.random.rand(Np)
		Q3 = np.random.rand(Np)
		Theta = np.zeros(Np)

		R = (Q2*DelR + Rc0) #Random rads
		dTh = (Q1*2*dLam - dLam) #Delta theta
		Ip = Q3>=0.5; Im = Q3<0.5
		Theta[Ip] = radScl*(ThCp+dTh[Ip])
		Theta[Im] = radScl*(ThCm+dTh[Im])

		x[:] = (R)*Cp*np.sin(Theta)
		y[:] = (R)*Sp*np.sin(Theta)
		z[:] = (R)*   np.cos(Theta)

	else:

		for i in range(Nr):
			for j in range(Nl):
	
				thP = (ThCp + Theta[j])*radScl
				thM = (ThCm + Theta[j])*radScl
				R = Rad[i]
	
				x[n] = R*Cp*np.sin(thP)
				y[n] = R*Sp*np.sin(thP)
				z[n] = R*   np.cos(thP)
	
				x[n+1] = (R+dR)*Cp*np.sin(thM)
				y[n+1] = (R+dR)*Sp*np.sin(thM)
				z[n+1] = (R+dR)*   np.cos(thM)
	
				n=n+2

	dPhiStr = "Phi-%f"%(PhiC)
	
	DefineScalarExpression("dPhi",dPhiStr)
	
	
	print("Generating %d streamlines\n"%(Nr*Nl))
	
	#Add phi slice
	#pyv.lfmPCol(db,"Bmag",vBds=(10,500),cMap="viridis",Log=True,pcOpac=pcOpacP,Light=False,Legend=False)
	pyv.lfmPCol(db,"pKappa",vBds=(1.0e-2,1.0e+2),cMap="viridis",Log=True,pcOpac=pcOpacP,Light=False,Legend=True)

	AddOperator("Slice")
	sOps = GetOperatorOptions(0); 
	sOps.axisType=4; sOps.project2d=0
	sOps.phi = 0; sOps.theta = PhiC
	SetOperatorOptions(sOps)
	
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
	
	#Block out critical latitude
	AddPlot("Contour","MLat")
	cOps = GetPlotOptions()
	cOps.contourMethod = 1
	cOps.contourValue = tuple([-LatC,LatC])
	cOps.legendFlag = 0
	cOps.lineWidth = 2
	cOps.colorType = 0
	cOps.singleColor = (0, 0, 0, 255)
	SetPlotOptions(cOps)
	AddOperator("Slice")
	sOps = GetOperatorOptions(0); 
	sOps.axisType=4; sOps.project2d=0
	sOps.phi = 0; sOps.theta = PhiC
	SetOperatorOptions(sOps)

	#Do streams
	if (doProd):
		#Only do streams for final version
		scMap = "RdBu"
		#scMap = "Cool"
		pyv.lfmStream(fIn,"Bfld",x,y,z,cMap=scMap,tRad=0.0015,Legend=False)
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

	#yS = 0.075
	#dx = 0.025
	dx = 0.015
	yS = 0.15
	dy = 0.025
	mltLab = pyv.genTit(mltStr,Pos=(dx,yS+dy) )
	lcLab = pyv.genTit(lcStr,  Pos=(dx,yS))
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
