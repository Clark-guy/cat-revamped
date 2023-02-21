from tkinter import *
import random

#	want a loop where cat image updates for a bit and then disappears
#
#
#

catsArray = [
	"cats/cat.txt",
	"cats/cat0.txt",
	"cats/cat1.txt",
	"cats/cat2.txt",
	"cats/cat3.txt",
	"cats/cat4.txt",
	"cats/cat5.txt",
	"cats/cat6.txt"]

def delayFunction():
	root.destroy()


def drawCat(i, catsArray):
	cat = open(catsArray[i])
	return cat

def drawAnimate(index, catsArray, label):
	print(index)
	label.config(text="\n"+drawCat(index, catsArray).read())
	root.after(1000, lambda: drawAnimate(index+1, catsArray, label))
	

print("running")

root = Tk()
#root.minsize(width=300, height=250)
root.geometry("300x250+900+400")
root.overrideredirect(1)
root.attributes('-alpha', 0.5)
root.attributes('-topmost', True)

fontTuple = ("Fixedsys", 15)
b = Label(root, justify=LEFT, text="\n"+drawCat(0, catsArray).read())
b.configure(font= fontTuple)
b.pack()


root.after(1000, lambda: drawAnimate(0, catsArray, b))
root.after(9000, delayFunction)

root.mainloop()
