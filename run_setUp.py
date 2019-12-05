import tkinter as tk
import tkinter.messagebox as msgbox
import EspEngPair11 as canvas
from pairDb import*


def chooseData():
	#msgbox.showinfo("Selection","Your Choice: " + var.get() )
	#canvas.StartCanvas(tk,var.get())
	global pairsData
	pairsData = getPairsByLetter(var.get())
	tOutText.set(int(len(pairsData)/2))
	if int(tOutText.get()) > 0:
		btnGo.config(state = "normal")
	else :
		btnGo.config(state = "disabled")

def requestStart():
	canvas.StartCanvas(tk,var.get(),pairsData)
	

window = tk.Tk()
pairsData = []

lblTop = tk.Label( window, width = 20,text = 'Setup options', bg="white")
lblTop.config(font=("Courier", 44))

mainFrame = tk.Frame(window,height=2, bd=1) #,relief=tk.SUNKEN) #bd == borderwidth
btmFrame = tk.Frame(window, bd = 1)


lblmFTitle = tk.Label(mainFrame,text = "Filters",pady = 5, font =("Courier",20)).pack(side = tk.TOP)

lblLetters = tk.Label( mainFrame,text = "Choose beginning letter of words", padx = 5).pack(side = tk.LEFT)

tOutText = tk.StringVar()
tOut = tk.Entry(btmFrame,textvariable = tOutText,borderwidth = 1)
tOut.config(bg="black",fg="#99ff33",font="Helvetica 30 bold",justify='right',width = 10)
tOut.pack()

#choices = [ 'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z' ]
choices = [ 'A','B','C','H','L','P','Q','R','S','T','V' ]
var = tk.StringVar(mainFrame)
var.set("Select letter") # initial value
dropDown1 = tk.OptionMenu(mainFrame, var, *choices)
dropDown1.config(bg="white",font=("Courier",18))
dropDown1.pack()

ddOptions = dropDown1.nametowidget(dropDown1.menuname) # gets menu of OptionMenu
ddOptions.config(font=("Courier",14),bg="white") #font of the options

btnChoose = tk.Button( mainFrame, text = "Choose", command = chooseData )
btnChoose.pack()

btnGo = tk.Button(btmFrame,text = "GO",command = requestStart,state = "disabled")
btnGo.pack()

lblTop.grid(row = 0, column = 0, columnspan = 3)
mainFrame.grid(row = 1, column = 0, columnspan = 3)
btmFrame.grid(row = 3, column = 0, columnspan = 3,pady=(50, 5))


window.title('Language Pair')
window.resizable(0,0)

window.mainloop()

