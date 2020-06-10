class Word:
	def __init__(self,w,pid,lang):
		self.word = w
		self.pairID = pid
		self.lang = lang

class Pair:
	def __init__(self,esp,eng):
		self.esp = esp
		self.eng = eng

class PairInput:
	def __init__(self,espW,engW):
		self.espW = espW
		self.engW = engW

	def getEspW(self):
		return self.espW
	def getEngW(self):
		return self.engW

def convertPairListToWordList(pairList):
	wordList = []
	for i in range(len(pairList)):
		wordList.append(pairList[i].esp)
		wordList.append(pairList[i].eng)
	return wordList