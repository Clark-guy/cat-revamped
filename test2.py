from tkinter import *
import random

#	want a loop where cat image updates for a bit and then disappears
#
#
#

catsList = [
	"cats/cat.txt",	#sitting
	"cats/cat0.txt",#sitting blink
	"cats/cat1.txt",#standing
	"cats/cat2.txt",#walk1
	"cats/cat3.txt",#walk2
	"cats/cat4.txt",#sitting look left
	"cats/cat5.txt",#sitting look left blink
	"cats/cat6.txt",#sleep1
	"cats/cat7.txt"]#sleep2

sit = [0,0,1,0,0,1,0,0]
walk = [3,4,3,4,3,4]


def destroyFunction():
	root.destroy()

#How to use root.after to animate cat indefinitely?
#make an array of indexes for action, pass to drawAnimate
#this is recursive, so at the end of array escape and
#have plan for what's next

def drawCat(i, catsList):
	cat = open(catsList[i])
	return cat


def animateForever(index, catsList, actionList, label):
	if(index<len(actionList)):
		label.config(text="\n"+drawCat(actionList[index], catsList).read())
		root.after(500, lambda: animateForever(index+1, catsList, actionList, label))
	else:
		print("there")
		choice = random.randint(0,1)
		if choice == 0:
			actionList = [0,0,1,0,0,1,0,0]
		else:
			actionList = [2,3,2,4,2,3,2,4]
		root.after(0, lambda: animateForever(0, catsList, actionList, label))
		

def drawAnimate(index, catsList, label):
	print(index)
	label.config(text="\n"+drawCat(index, catsList).read())
	root.after(1000, lambda: drawAnimate(index+1, catsList, label))
	
def colorSwitch(b):
	global catColor
	print(catColor)
	if catColor == "white":
		b.config(fg="gray1")
		catColor="gray1"
	else:
		catColor="white"
		b.config(fg="white")

print("running")

root = Tk()
root.configure(bg="black")
root.minsize(width=300, height=250)
root.geometry("300x250+900+460")
root.overrideredirect(1)
root.attributes('-alpha', 1)
root.attributes('-topmost', True)
catColor = "white"

fontTuple = ("Fixedsys", 15, "bold")
b = Button(root, relief="flat", command=lambda: colorSwitch(b), bg="black", fg=catColor, justify=LEFT, text="\n"+drawCat(0, catsList).read())
b.configure(font= fontTuple)
b.pack()

root.wm_attributes("-transparentcolor", "black")

#root.after(1000, lambda: drawAnimate(0, catsArray, b))
root.after(1000, lambda: animateForever(0, catsList, sit, b))
root.after(30000, destroyFunction)

root.mainloop()
