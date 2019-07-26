class MovingWord:
	# try the canvas element as Class var instead of instance var
	gID = 0
	canvas = None

	def __init__(self,x,y,txt,pid,lang):
		padding = 0
		if len(txt) > 8:
			moreThan8 = len(txt) - 8
			for i in range(0,moreThan8):
				padding += 10

		self.cID = MovingWord.gID
		MovingWord.gID += 1
		if lang == "eng":
			color = "white"
		else:
			color = "#ffffb3" #light yellow
		self.pairID = pid
		self.x = x
		self.y = y
		self.width = 100 + padding
		self.height = 50
		self.rectangle = MovingWord.canvas.create_rectangle(x,y,x + self.width , y + self.height ,fill = color,activefill='cyan')
		self.Selected = False
		self.text = txt
		self.txtObj = MovingWord.canvas.create_text(x + 45 + (padding /2), y + 20, font=("Purisa", 12), text = txt,fill = "blue")
		self.mX = 0
		self.mY = 0
		self.waitingToMove = False
		self.toBeRemoved = False

	@staticmethod
	def initCanvas(c):
		MovingWord.canvas = c;

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
		MovingWord.canvas.move(self.rectangle,a,b)
		MovingWord.canvas.move(self.txtObj,a,b)

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