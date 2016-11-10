#Reads in 3D Cartesian field VTI and plots some field lines
#3D field data is in code units, transfer to B field in nT

import numpy as np
from visit import *
from visit_utils import *
from visit_utils.common import lsearch #lsearch(dir(),"blah")
import lfmGrids as lfm
import pyVisit as pyv

fIn = "fldDatLorez.vti"
#fIn = "fldDat.vti"
db = fIn
pcOpac = 0.75

#Create pointlist for streamline
Np = 5
R = 5
x = np.zeros(Np); y = np.zeros(Np); z = np.zeros(Np)
s = np.linspace(0,2*np.pi,Np)
x = R*np.cos(s); y = R*np.sin(s); z = 0*s

#Do parabola pointlist
Np = 5
xMin = -8
Scl = [0.05]
xN = [9,10,11,12]

x = [];y=[];z=[]

for nS in range(len(Scl)):
	for nN in range(len(xN)):
		xl = np.linspace(xMin,xN[nN],Np)
		yl = yl = np.sqrt( (xN[nN]-xl)/Scl[nS] )
		for n in range(Np):
			x.append(xl[n]);y.append(yl[n]);z.append(0)
			x.append(xl[n]);y.append(-yl[n]);z.append(0)


Launch()

OpenDatabase(fIn)
md = GetMetaData(fIn) #Metadata

#Import definitions
pyv.lfmExprsEB()

#Start plotting
pyv.setAtts() #Some defaults

pyv.lfmPCol(db,"dBz",vBds=(-25,25),Inv=True,pcOpac=pcOpac,Light=False)

#Field slice, equatorial
AddOperator("Slice")
sOps = GetOperatorOptions(0); 
sOps.axisType=2; sOps.project2d=0
SetOperatorOptions(sOps)

#Block out central cutout
AddPlot("Contour","RadAll")
cOps = GetPlotOptions()
cOps.contourMethod = 1
cOps.contourValue = (2.2)
cOps.legendFlag = 0
SetPlotOptions(cOps)

#Do streams
pyv.lfmStream(fIn,"Bfld",x,y,z)
#pyv.lfmStream(fIn,"V",x,y,z)


#Show them all
DrawPlots()