from tkinter import *
from PairInput import *
from pairDb import *

def loadFile(option):
	print("loadfile executed")
	fileSrc = "esp_Somewords.txt" if (option == "spanish") else "demoFile.txt"
	file = open(fileSrc,"r")

	linesCount = len(open(fileSrc).readlines())

	print("lines in file", linesCount)

	
	
	#textOutput.insert(END,fileLine[3])

	for i in range(0,linesCount):
		fileLine = file.readline()
		lineLen = len(fileLine)
		bSpanish = True
		spanishWord = englishWord = "";

		if lineLen > 3 and (fileLine[0] != "/" and fileLine[1] != "/"):
			for j in range(0,lineLen):
				char = fileLine[j]
				if char == "\t":
					continue;
				elif char == "\n":
					break;
				if (char == " " or char == "\t"):
					if (fileLine[j + 1] == " " or fileLine[j + 1] == "\t" or fileLine[j + 1] == ":"):
						continue
					else:
						textOutput.insert(END,fileLine[j])
						if bSpanish == True:
							spanishWord += fileLine[j]
						else:
							englishWord += fileLine[j]

					textOutput.insert(END,fileLine[j])
				elif (char == ":"):
					textOutput.insert(END, "\t\t")
					bSpanish = False
				else:
					textOutput.insert(END,fileLine[j])
					if bSpanish == True:
						spanishWord += fileLine[j]
					else:
						englishWord += fileLine[j]
		
			print("spanish word = ",spanishWord,len(spanishWord))
			print("english word = ",englishWord,len(englishWord))
			pairsFromFile.append(PairInput(spanishWord,englishWord))
			textOutput.insert(END, "\t\t\tLenOfEsp " + str(len(spanishWord)) + "\t\t LenOfEng " + str(len(englishWord)) + "\n")

			
			if i == 1:
				print("\t The len of spaWord ", len(spanishWord) ," len of engWord " , len(englishWord))
				for k in range(0,len(spanishWord)):
					if spanishWord[k] == " ":
						print("space")
					elif spanishWord[k] == "\t":
						print("tab")
					elif spanishWord[k] == "\n":
						print("nLine")
					else:
						print(spanishWord[k])

	#textOutput.insert(END,fileLine)
	#textOutput.insert(END,lineLen)

def submitPairs():
	numOf = len(pairsFromFile)
	if numOf == 0:
		print("Nothing to submit")
	else:
		print("in submit pairs Len of pairs collection is",len(pairsFromFile))
		newRows = handleAllInput(pairsFromFile)
		print(newRows)

window = Tk()
Label(window, text="Language").grid(row=0,column=0,columnspan = 2)

textOutput = Text(window, height =20, width = 100,bg="black",fg="#99ff33")
textOutput.grid(row=2,column=0,columnspan = 2)
btnSpn = Button(window, text='Spanish', command = lambda: loadFile("spanish"))
btnSpn.grid(row=3, column=0,sticky=W,pady=4)

pairsFromFile = []

btnSubmit = Button(window,text="Submit",command= submitPairs)
btnSubmit.grid(row=3,column = 1, sticky=W)

mainloop()