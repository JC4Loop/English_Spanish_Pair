from tkinter import*
import time
from random import shuffle
from pairDb import*


class Component:
	# try the canvas element as Class var instead of instance var
	gID = 0
	canvas = None

	def __init__(self,x,y,txt,pid):
		padding = 0
		if len(txt) > 8:
			moreThan8 = len(txt) - 8
			for i in range(0,moreThan8):
				padding += 10

		self.cID = Component.gID
		Component.gID += 1
		self.pairID = pid
		self.x = x
		self.y = y
		self.width = 100 + padding
		self.height = 50
		self.rectangle = Component.canvas.create_rectangle(x,y,x + self.width , y + self.height ,fill = "white",activefill='cyan')
		self.Selected = False
		self.text = txt
		self.txtObj = Component.canvas.create_text(x + 45 + (padding /2), y + 20, font=("Purisa", 12), text = txt,fill = "blue")
		self.mX = 0
		self.mY = 0
		self.waitingToMove = False
		self.toBeRemoved = False

	@staticmethod
	def initCanvas(c):
		Component.canvas = c;

	def getRectangle(self):
		return self.rectangle
	def getTxtObj(self):
		return self.txtObj
	def getX(self):
		return self.x
	def getY(self):
		return self.y
	def getMX(self):
		return self.mX
	def setMX(self,v):
		self.mX = v
	def getMY(self):
		return self.mY
	def setMY(self,v):
		self.mY = v

	def getLeft(self):
		return self.x
	def getRight(self):
		return self.x + self.width
	def getTop(self):
		return self.y
	def getBottom(self):
		return self.y + self.height

	def moveComp(self,a,b):
		self.x += a
		self.y += b
		c.move(self.rectangle,a,b)
		c.move(self.txtObj,a,b)


	def canMoveLeft(self,otherS):
		bCanMoveL = True
		gap = 20
		for i in range(0,len(otherS)):
			bCanMoveL = True
			if otherS[i].cID == self.cID: 
				continue
			if self.getLeft() <= otherS[i].getRight() + gap and not(self.getBottom() <= otherS[i].getTop() or self.getTop() >= otherS[i].getBottom()):
				if otherS[i].getLeft() > self.getRight():
					continue
				else:
					bCanMoveL = False
					break
	
		return bCanMoveL

	def collision(self,otherS):
		bCollision = True
		for i in range(0,len(otherS)):
			bCollision = True
			gap = 20
			if otherS[i].cID == self.cID: # dont check for collision with itself
				bCollision = False
				continue
			if self.getLeft() >=  otherS[i].getRight() + gap or self.getRight() <= otherS[i].getLeft() - gap \
				or self.getBottom() <= otherS[i].getTop() - gap or self.getTop() >= otherS[i].getBottom() + gap:
				bCollision = False
			if bCollision == True:
				break
	
		return bCollision

#---------------------------------------------------END of Component Class

def removeFromActiveComps(cID):
	for i in range(len(activeComponents)-1,-1,-1):
		if activeComponents[i].cID == cID:
			activeComponents.remove(activeComponents[i])
			#print(len(activeComponents),"active comps")
			break

def prepareRemoveFromActiveComps(pID):
	for i in range(0,len(activeComponents)):
		if activeComponents[i].pairID == pID:
			activeComponents[i].toBeRemoved = True
			finishedComponents.append(activeComponents[i])
	

	activeLen = sum(y.toBeRemoved == False for y in activeComponents)
	#print(activeLen,"active components")

	if activeLen == 0:
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
				incrementTimesInCor(pairID,selectedCs[1].pairID)
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
	incrementTimesCorrect(pairID)
	selectedCs[0].setMY(-5)
	selectedCs[1].setMY(-5)
	#print("Found pair With pairID:",pairID)
	selectedCs.remove(selectedCs[1])
	selectedCs.remove(selectedCs[0])
	prepareRemoveFromActiveComps(pairID)
	#print(len(selectedCs))


gui = Tk()
gui.resizable(width=False,height=False)


gui.geometry("800x800")
img = PhotoImage( file = "tickEngrave.png")
small_img = PhotoImage.subsample( img, x = 2, y = 2)
c = Canvas(gui, width=800 ,height=800)
c.pack()
c.create_rectangle(0,0,800,800, fill="black")
c.create_image((500, 500), image = small_img)
Component.initCanvas(c)

selectedCs = []
activeComponents = []
finishedComponents = []

global_incorrectPair = {"iPair":False,"num":0}
lastPlaced = 0
maxOnScreen = 8


pairsData = getPairs()

def preparePairs(pairsData, maxOnScreen):
	preparedPairs = []
	keepCount = 0
	global lastPlaced
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
		activeComponents.append(Component(x,y,preparePairs[j].word, preparePairs[j].pairID))
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
	
preparePairs(pairsData,maxOnScreen)
print("last placed outside func is",lastPlaced)



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

frameCount = 0
second = 0
gui.title("Canvas Animate")
while True:
	try:
		frameCount += 1
		gui.update_idletasks()
		gui.update()
		movementCalc(frameCount)
	except:
		print("Caught gui.update() error") # error only occurs on close
		break
	
	time.sleep(.01)

	if frameCount >= 100:
		frameCount = 0
		second += 1
		if (second == 10):
			second = 0

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
	


#gui.mainloop() # have self made loop