#from tkinter import*
from MovingWord import *
import time , threading
from random import shuffle
from pairDb import*

def resetGlobals():
	global global_running, global_runLoop
	global c,numLeft, pairsData, maxOnScreen
	global selectedCs, activeComponents, finishedComponents,global_incorrectPair,lastPlaced
	global lCorrectPairsIncrement, lWrongPairsIncrement, incThread
	global bSqlite
	global_running = False
	global_runLoop = True
	bSqlite = False
	c = IncThread = None
	numLeft = None
	pairsData = None
	maxOnScreen = None
	selectedCs = []
	activeComponents = []
	finishedComponents = []
	lCorrectPairsIncrement = []
	lWrongPairsIncrement = []
	global_incorrectPair = {"iPair":False,"num":0}
	lastPlaced = 0


# function for when components are outside of viewable canvas
def removeFromActiveComps(cID):
	for i in range(len(activeComponents)-1,-1,-1):
		if activeComponents[i].cID == cID:
			activeComponents.remove(activeComponents[i])
			#print(len(activeComponents),"active comps")
			break

# function to set components for canvas exit
def prepareRemoveFromActiveComps(pID):
	for i in range(0,len(activeComponents)):
		if activeComponents[i].pairID == pID:
			activeComponents[i].toBeRemoved = True
			finishedComponents.append(activeComponents[i])
	
	activeLen = sum(y.toBeRemoved == False for y in activeComponents)
	#print(activeLen,"active components")

	if activeLen == 0:
		if (len(pairsData) - lastPlaced) > 0:
			print("now should require next set")
			preparePairs(pairsData,maxOnScreen)

		
	
def bindComponent(obj):
	c.tag_bind(obj.getRectangle(),"<Button-1>", lambda event, arg = obj: objectClicked(event, arg) )
	c.tag_bind(obj.getTxtObj(),"<Button-1>", lambda event, arg = obj: objectClicked(event,obj) )

def objectClicked(event,obj):
	nSelcs = len(selectedCs)
	if nSelcs == 0 or nSelcs == 1:
		#print(len(selectedCs))
		componentSelected(obj)
		if len(selectedCs) == 2:
			pairID = selectedCs[0].pairID
			if pairID == selectedCs[1].pairID:
				#print("Match found")
				pairFoundAni(pairID)
			else:
				#print("Incorrect Pair")
				if bSqlite == False:
					lWrongPairsIncrement.append(pairID)
					lWrongPairsIncrement.append(selectedCs[1].pairID)
					#incrementTimesInCor(pairID,selectedCs[1].pairID)
				global_incorrectPair["iPair"] = True

def componentSelected(obj):
	if obj.Selected == False:
		obj.Selected = True
		selectedCs.append(obj)
		c.itemconfig(obj.rectangle, fill = "red",activefill="red")
	else:
		obj.Selected = False
		selectedCs.remove(obj)
		c.itemconfig(obj.rectangle, fill = "white",activefill="cyan")

	#print(obj.text, "pairID = " , obj.pairID )

def incorrectPairtoWhite():
	c.itemconfig(selectedCs[0].rectangle, fill = "white", activefill="")
	c.itemconfig(selectedCs[1].rectangle, fill = "white", activefill="")

def incorrectPairtoRed():
	c.itemconfig(selectedCs[0].rectangle, fill = "red")
	c.itemconfig(selectedCs[1].rectangle, fill = "red")

def pairFoundAni(pairID):
	if bSqlite == False:
		lCorrectPairsIncrement.append(pairID)
	selectedCs[0].setMY(-5)
	selectedCs[1].setMY(-5)
	#print("Found pair With pairID:",pairID)
	selectedCs.remove(selectedCs[1])
	selectedCs.remove(selectedCs[0])
	prepareRemoveFromActiveComps(pairID)
	#print(len(selectedCs))

def preparePairs(pairsData, maxOnScreen):
	preparedPairs = []
	keepCount = 0
	global lastPlaced
	global numLeft
	numLeft = len(pairsData) - lastPlaced
	print(numLeft," left to be placed")

	if numLeft >= maxOnScreen:
		lastToBe = lastPlaced + maxOnScreen
	else:
		lastToBe = lastPlaced + numLeft

	for i in range(lastPlaced,lastToBe):
		preparedPairs.append(pairsData[i]);
		keepCount +=1

	shuffle(preparedPairs)
	placeOnCanvas(preparedPairs,maxOnScreen,lastPlaced,lastToBe,numLeft)
	lastPlaced += keepCount


def placeOnCanvas(preparePairs, maxOnScreen,first,last,numLeft):
	acLen = len(activeComponents)
	first = acLen
	if numLeft  >= maxOnScreen:
		last = maxOnScreen + acLen
	else:
		last = numLeft + acLen

	#print("len of active comps is",len(activeComponents))
	x ,y = 500, 100
	j = 0
	for i in range(first,last):
		activeComponents.append(MovingWord(x,y,preparePairs[j].word, preparePairs[j].pairID,preparePairs[j].lang))
		activeComponents[i].setMX(-1)
		j += 1
		y += 150
		if y > 600:
			y = 400
			x += 250
	for i in range(first,last):
		bindComponent(activeComponents[i])
	activeComponents[0].setMX(1)
	activeComponents[1].setMX(1)
	

def movementCalc(frameCount):
	cmpsLen = len(activeComponents)
	for i in range(cmpsLen -1,-1,-1): # start with last active cmpnt to the first - this way removing from activeComps will not result in outofBounds
		if (not(activeComponents[i].getMX() == 0 and activeComponents[i].getMY() == 0) and activeComponents[i].toBeRemoved == False):
			#if the component has movement value and is not to be removed
			if (frameCount > 80):
				activeComponents[i].waitingToMove = False
			if activeComponents[i].canMoveLeft(activeComponents) == False:
				activeComponents[i].waitingToMove = True

		if activeComponents[i].getY() < 400:
			if activeComponents[i].getX() < 5 or activeComponents[i].getX() > 500:
				activeComponents[i].setMX( - activeComponents[i].getMX())
		else:
			if activeComponents[i].getX() <= 10:
				activeComponents[i].setMX(0)
		if activeComponents[i].waitingToMove == False or activeComponents[i].toBeRemoved == True:
			activeComponents[i].moveComp(activeComponents[i].getMX(),activeComponents[i].getMY())

		if (activeComponents[i].getY() + activeComponents[i].height) < 0:
			removeFromActiveComps(activeComponents[i].cID)
#------------------------------------------------------------------END movementCalc

def checkIncrementThread():
	global lWrongPairsIncrement,lCorrectPairsIncrement,incThread
	if len(lWrongPairsIncrement) > 0 or len(lCorrectPairsIncrement) > 0:
		# if not using SQLite database, using Postgres
		if bSqlite == False:
			if incThread == None:
				incThread = thread_Increment(lCorrectPairsIncrement,lWrongPairsIncrement)
				incThread.start()
				lWrongPairsIncrement = []
				lCorrectPairsIncrement = []
			else:
				if not incThread.is_alive():
					try:
						incThread.start()
					except RuntimeError:
						print("attempting to create thread again")
						incThread = thread_Increment(lCorrectPairsIncrement,lWrongPairsIncrement)
						incThread.start()
					lCorrectPairsIncrement = []
					lWrongPairsIncrement = []

class thread_Increment (threading.Thread):
	def __init__(self, cpInc,wpInc):
		threading.Thread.__init__(self)
		self.cpInc = cpInc
		self.wpInc = wpInc

	def run(self):
		wpSize = len(self.wpInc)
		cCount = wCount = 0
		if wpSize % 2 != 0:
			print("SERIOUS ERROR in wrong pairs list!")
		for i in range(len(self.wpInc)):
			print(self.wpInc[i])
			if i % 2 == 0:
				print("i = ",i)
				wCount += incrementTimesInCor(self.wpInc[i],self.wpInc[i+1])
		for i in range(len(self.cpInc)):
			print(self.cpInc[i])
			cCount += incrementTimesCorrect(self.cpInc[i])
		print("Incremented",cCount,"correct pairs\tIncremented",wCount,"wrong pairs")

def StartCanvas(tk,letter,pairsD,bsql):
	global global_running, global_runLoop,bSqlite
	global pairsData,activeComponents, lWrongPairsIncrement,lCorrectPairsIncrement
	global c, incThread
	global lastPlaced, maxOnScreen
	if global_running == False:
		print("false - beginning run")
		global_running = True
		pairsData = pairsD
		print("letter selected ", letter)
		gui = tk.Toplevel()
		gui.resizable(width=False,height=False)
		gui.geometry("800x800")
		img = tk.PhotoImage( file = "tickEngrave.png")
		small_img = tk.PhotoImage.subsample( img, x = 2, y = 2)
		c = tk.Canvas(gui, width=800 ,height=800)
		c.pack()
		c.create_rectangle(0,0,800,800, fill="black")
		c.create_image((500, 500), image = small_img)
		MovingWord.initCanvas(c)
		lastPlaced = 0
		maxOnScreen = 8
		preparePairs(pairsData,maxOnScreen)
		print("last placed outside func is",lastPlaced)
		bSqlite = bsql
		print(bSqlite)

		frameCount = 0
		second = 0
		gui.title("Canvas Animate")
		runLoop = True

		while global_runLoop:
			try:
				frameCount += 1
				gui.update_idletasks()
				gui.update()
				movementCalc(frameCount)


				if len(activeComponents) == 0:
					global_runLoop = False
					print("global_runLoop is false")

			except:
				print("Caught gui.update() error") # error only occurs on close
				resetGlobals()
				break

			time.sleep(.01)

			if frameCount >= 100:
				frameCount = 0
				second += 1
				if (second == 5):
					second = 0
					checkIncrementThread()
					
				#print("second 5, setting to 0")
					

			if global_incorrectPair["iPair"] == True:
				if(global_incorrectPair["num"] == 0 or global_incorrectPair["num"] == 60):
					incorrectPairtoWhite()
				if(global_incorrectPair["num"] == 30 or global_incorrectPair["num"] == 90):
					incorrectPairtoRed()
				global_incorrectPair["num"] += 1

				if(global_incorrectPair["num"] == 120):
					global_incorrectPair["num"] = 0
					global_incorrectPair["iPair"] = False
					#set the two incorrect pairs to be unselected
					componentSelected(selectedCs[1])
					componentSelected(selectedCs[0])
		print("finished - checking incrementThread")
		checkIncrementThread()
		resetGlobals()
		gui.destroy() # close the gui window, not the whole program

	else:
		print("true - wont run")



global_running = False
global_runLoop = True
bSqlite = False
c = None
numLeft = None
pairsData = None
maxOnScreen = incThread = None
selectedCs = []
activeComponents = []
finishedComponents = []
lCorrectPairsIncrement = []
lWrongPairsIncrement = []
global_incorrectPair = {"iPair":False,"num":0}
lastPlaced = 0