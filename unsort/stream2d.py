import sys
import numpy as np
import datetime
from visit import *
from visit_utils import *
from visit_utils.common import lsearch #lsearch(dir(),"blah")
import pyVisit as pyv

RunID = 2 #Which pStub to use
pStub = ["e.100keV","H.100keV","O.100keV"]
pLabs = ["Electron (100 keV)", "Hydrogen (100 keV)", "Oxygen (100 keV)"]
Base = "~/Work/magnetoloss/"
EqDir = Base + "eqSlc" #eqSlc database
pDir = Base + "synth" #Directory of h5part

slBoxX = [-10,10]; slBoxY = [-15,15]; slBoxZ = [-4,4]
Nln = 20
Quiet = False

titS = pLabs[RunID]

dt = 10 #Cadence [s]

#dBz 
abBz = 25; 
dBzBds = [-abBz,abBz]

#Particles
kevBds = [50,150]
pCMap = "Cool" #ColorTableNames()

# Nx = 10
# Ny = 5
Np = 500
# xx = np.linspace(-12,-8,Nx)
# yy = np.linspace(-5,5,Ny)
# Np = Nx*Ny
# x2,y2 = np.meshgrid(xx,yy)
# Pts = np.zeros((Np,3))
# Pts[:,0] = x2.flatten()
# Pts[:,1] = y2.flatten()
#x0 = -12;x1=-8
#y0 = -5; y1=5
x = [3,7]
y = [-7,7]

Pts = np.random.random((Np,3))
Pts[:,2] = 0
Pts[:,0] = (Pts[:,0]*(x[1]-x[0]) + x[0])
Pts[:,1] = (Pts[:,1]*(y[1]-y[0]) + y[0])



if (Quiet):
	LaunchNowin()
else:
	Launch()

#Legends
plXs = [0.03]
plYs = [0.9,0.4]
plTits = ["Residual Bz [nT]","Particle Energy [keV]"]
#Construct filenames/directory structure
#Use ActivateDatabase to swap between
#md0 = GetMetaData(dbs[0]) for info

Src0 = EqDir + "/eqSlc.*.vti database"
Src1 = pDir + "/" + pStub[RunID] + ".h5part" 
 
dbs = [Src0,Src1]

#Do some defaults
pyv.lfmExprs()

#Open databases
OpenDatabase(dbs[0])
OpenDatabase(dbs[1])


#Create database correlation
CreateDatabaseCorrelation("P2Fld",dbs,0)

#Field stuff
pyv.lfmPCol(dbs[0],"dBz",vBds=dBzBds,pcOpac=0.7,Inv=True)

#Pathline plot
ActivateDatabase(dbs[0])
AddPlot("Streamline","V2D")
slOps = GetPlotOptions()

# slOps.sourceType = 3	
# slOps.radius = 4
# slOps.sphereOrigin = (-10,0,0)

slOps.sourceType = 1
slOps.pointList = tuple(Pts.flatten())
#slOps.coloringMethod = 2
slOps.coloringMethod = 5
slOps.coloringMethod = 3

#slOps.randomSamples = 1
#slOps.numberOfRandomSamples = 4

slOps.pathlines = 0
slOps.issueStiffnessWarnings = 0
slOps.geomDisplayQuality = 3
slOps.showSeeds = 1
slOps.seedRadiusBBox = 0.0025

slOps.maxSteps = 1000
slOps.showHeads = 1
slOps.legendMinFlag = 1
slOps.legendMaxFlag = 1
slOps.legendMin = 0
slOps.legendMax = 20

slOps.headRadiusBBox = 0.005
slOps.colorTableName = "Cool"
SetPlotOptions(slOps)

DrawPlots()
