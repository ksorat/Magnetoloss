#Calculate time lost particles spend on open field lines before leaving box
import numpy as np
import lfmViz as lfmv
import lfmPostproc as lfmpp
import matplotlib as mpl
import matplotlib.pyplot as plt

def CountXs(tCr,pids):
	#Take array of tCr, count number of crossings
	#There should be a cleaner way of doing this w/ apply_along_axis
	Nt,Np = tCr.shape
	NumX = np.zeros(Np)
	for n in range(Np):
		NumX[n] = len(np.unique(tCr[:,n])) - 1 #Don't include zero default
	print("\t\tNumber = %d\n"%(Np))
	print("\t\tNumX Min/Max = %d %d\n"%(np.amin(NumX),np.amax(NumX)))
	print("\t\tpIDs Min/Max = %d %d\n"%(pids[np.argmin(NumX)], pids[np.argmax(NumX)] ) )
	return NumX
def NumCross(fIn,onlyOut=True):

	isOut = lfmpp.getOut(fIn)
	t,tCrF = lfmpp.getH5p(fIn,"tCr")
	t,pids = lfmpp.getH5p(fIn,"id")
	pids = pids[-1,:]
	print("\tAll particles:\n")
	NumX_All = CountXs(tCrF,pids)
	print("\tOnly out:\n")
	NumX_Out = CountXs(tCrF[:,isOut],pids[isOut])
	print("\tOnly in:\n")
	NumX_In = CountXs(tCrF[:,np.logical_not(isOut)],pids[np.logical_not(isOut)])
	print("\t# of In + MP-X = %d\n"% np.sum(NumX_In>0))

	return NumX_All,NumX_Out,NumX_In
dirStub = "/Users/soratka1/Work/magnetoloss/synth"
fileStub = "100keV.h5part"

spcs = ["H","O","e"]
Leg = ["Hydrogen","Oxygen","Electron"]

Ns = len(spcs)


aNumX = []
for i in range(Ns):

	fIn = dirStub + "/" + spcs[i] + "." + fileStub
	print("Reading %s"%(fIn))
	print("Species %s"%(Leg[i]))
	NumX_All,NumX_Out,NumX_In = NumCross(fIn)
	aNumX.append(NumX_Out)
	#aNumX.append(NumX_In)

Nb = 50
N0 = 0; N1 = 30
bins = np.linspace(N0,N1,Nb)

doNorm = True
doLog = True

nxFig = plt.hist(aNumX,bins,normed=doNorm,log=doLog)
plt.legend(Leg)
plt.xlabel("Number of MP Crossings")
plt.ylabel("PDF")
plt.show()
#plt.savefig("NumMPx.png")
#plt.close()