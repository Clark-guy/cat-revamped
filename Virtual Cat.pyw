from tkinter import *
from PIL import ImageTk, Image
import random

# Cool Cat
#
# To do
# - make cat object, with class variables for hunger, tiredness
# - give it states - have image react based on current state
# - maybe little indicator bars?




def destroyFunction(root):
	root.destroy()

def transparencyFunc(root, alphaColor, panel2):
	global invisibleWindow
	if invisibleWindow == 0:
		root.wm_attributes("-transparentcolor", alphaColor)
		root.overrideredirect(1)
		root.minsize(width=300, height=180)
		invisibleWindow = 1
	else:
		root.wm_attributes("-transparentcolor", "")
		root.overrideredirect(1)
		root.minsize(width=300, height=180)
		invisibleWindow = 0


#How to use root.after to animate cat indefinitely?
#make an array of indexes for action, pass to drawAnimate
#this is recursive, so at the end of array escape and
#have plan for what's next

def drawCat(i, catsList):
	cat = open(catsList[i])
	return cat


#actions is the list of actions
#currentAction is the action
def animateForever(root, index, catsList, actions, currentAction, label):
	if(index<len(currentAction)):
		label.config(text="\n"+drawCat(currentAction[index], catsList).read())
		root.after(500, lambda: animateForever(root, index+1, catsList, actions, currentAction, label))
	else: #switch animation
		choice = random.randint(0,7)
		#root.after(100, lambda: moveLeft(root, 10, 550))
		global winX
		print("choice: " + str(choice))
		print(actions[choice])
		match choice:
			case 0:
				currentAction = actions[0]
			case 1:
				currentAction = actions[1]
				if winX>300:
					root.after(100, lambda: moveRight(root, -10, 300))				
			case 2:
				currentAction = actions[2]
				#root.after(100, lambda: test(root, 10, 400))
			case 3:
				currentAction = actions[3]
			case 4:
				currentAction = actions[4]#walkR
			case 5:
				currentAction = actions[5]#walkL
				if root.winfo_screenwidth() > winX:
					root.after(100, lambda: moveLeft(root, 10, 550))				
			case 6:
				currentAction = actions[6]
			case _:
				currentAction = actions[7]
		root.after(0, lambda: animateForever(root, 0, catsList, actions, currentAction, label))
		

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

def moveLeft(root, interval, maxSize):
	global winX #size of window X
	global winY #size of window Y
	global posX #screen position X
	global posY #screen position Y
	if(winX < maxSize):
		winX +=interval
		posX -=interval
		root.after(100, lambda: moveLeft(root, interval, maxSize))
		root.geometry(str(winX)+"x"+
			      str(winY)+
			      "+"+
			      str(posX)+"+"+   #to get size from left - posX + winX
			      str(posY))
	print("moveLeft")
	print("posx: " + str(posX) + "    WinX: " + str(winX))
	print(maxSize)

def moveRight(root, interval, maxSize):
	global winX #size of window X
	global winY #size of window Y
	global posX #screen position X
	global posY #screen position Y
	if(winX > maxSize):
		winX +=interval
		posX -=interval
		root.after(100, lambda: moveRight(root, interval, maxSize))
		root.geometry(str(winX)+"x"+
			      str(winY)+
			      "+"+
			      str(posX)+"+"+   #to get size from left - posX + winX
			      str(posY))
	print("moveRight")
	print("posx: " + str(posX) + "    WinX: " + str(winX))
	print(maxSize)



#global vars
catColor = "gray1"
invisibleWindow = 0
winX = 300
winY = 200
posX = 800
posY = 400


def main():
	fullscreen=False#True
	catsList = [
		"cats/cat.txt",	#0 sitting
		"cats/cat0.txt",#1 sitting blink
		"cats/cat1.txt",#2 standing left
		"cats/cat2.txt",#3 walk1 left
		"cats/cat3.txt",#4 walk2 left
		"cats/cat4.txt",#5 sitting look left
		"cats/cat5.txt",#6 sitting look left blink
		"cats/cat6.txt",#7 sleep1
		"cats/cat7.txt",#8 sleep2
		"cats/catL.txt", #0L sitting
		"cats/cat0L.txt",#1L sitting blink
		"cats/cat1L.txt",#2L standing left
		"cats/cat2L.txt",#3L walk1 left
		"cats/cat3L.txt",#4L walk2 left
		"cats/cat4L.txt",#5L sitting look left
		"cats/cat5L.txt",#6L sitting look left blink
		"cats/cat6L.txt",#7L sleep1
		"cats/cat7L.txt"]#8L sleep2

	#turn into dictionary TODO
	sit = [0,0,1,0,0,1,0,0]                 #0 sit
	sitL = [x+9 for x in sit]               #1 sitl
	lookLeft = [5,5,6,5,5,6,5,5]            #2 lookl
	lookRight = [x+9 for x in lookLeft]     #3 lookr
	walk = [3,4,3,4,3,4]                    #4 walk
	walkL = [x+9 for x in walk]             #5 walkl
	sleep = [7,8,7,8,7,8,7,8]               #6 sleep
	sleepL = [x+9 for x in sleep]           #7 sleepl
	actions = [sit, walk, lookLeft, sleep, sitL, walkL, lookRight, sleepL]

	#window creation
	print("running")
	alphaColor = "orange"
	root = Tk()
	global posX
	global posY
	posX = root.winfo_screenwidth()-winX-20
	posY = root.winfo_screenheight()-winY-40
	root.configure(bg=alphaColor)
	root.minsize(width=winX, height=winY)
	root.title("Burgle")
	root.geometry(str(winX)+"x"+str(winY)+"+"+str(posX)+"+"+str(posY))
	root.resizable(False,False)

	if fullscreen:
		root.attributes('-fullscreen', True)
		marginy = 45
		marginx = 5
	else:
		#Going back and forth on using overrideRedirect here- could make it a lot easier to style the window
		root.overrideredirect(1)
		marginy = 5
		marginx = 20

	#root.wm_attributes("-transparentcolor", alphaColor)


	#root.attributes('-alpha', 1)
	root.attributes('-topmost', True)
	global catColor
	

	img = ImageTk.PhotoImage(Image.open("images/paw.png").resize((20,20), Image.LANCZOS))
	#img = img.resize((10,10), Image.ANTIALIAS)

	fontTuple = ("Fixedsys", 10, "bold")

	#making frames
	root.sticky='NESW'
	root.grid_columnconfigure(0,weight=1)
	catFrame = Frame(root, height=100)
	buttonFrame = Frame(root, height=100, borderwidth=6, relief="sunken")
	buttonFrame.grid(column=0,row=0, columnspan=2, sticky='NESW')
	buttonFrame.grid_columnconfigure(3,weight=1)
	catFrame.grid(column=0,row=1, sticky='W')


	cat = Label(catFrame, relief="flat",bg=alphaColor, fg=catColor, justify=LEFT, text="\n"+drawCat(0, catsList).read())
	cat.configure(font= fontTuple)
	panel2 = Button(buttonFrame, image = img, justify=LEFT, bg="green",  cursor="hand2", command=lambda: transparencyFunc(root, alphaColor, panel2))
	panel1 = Button(buttonFrame, image = img, justify=LEFT, bg="blue",  cursor="hand2",  command=lambda: colorSwitch(cat))
	panel0 = Button(buttonFrame, image = img, justify=LEFT, bg="red",  cursor="hand2",   command=root.destroy)
	bar = Button(buttonFrame, bg="grey", justify=LEFT, height=0, cursor="fleur")

	#pack panels
	#panel0.pack(side="left",)
	#panel1.pack(side="left",)
	#panel2.pack(side="left",)
	#b.pack(side="left", anchor=SE)

	panel0.grid(column=0,row=0, sticky="NESW")
	panel1.grid(column=1,row=0, sticky="NESW")
	panel2.grid(column=2,row=0, sticky="NESW")
	bar.grid(column=3,row=0, sticky='NESW')
	cat.grid(column=0,row=1)



	#can call many of these concurrently - maybe one to manage statuses, one for view?
	# maybe would be better to consolidate all to one function, and go from there
	#
	#idea 1 - create object cat, pass to root.after function below, call object method to increase hunger and sleepiness from within that
	#
	#
	#
	# moving cat - need to figure out how this is going to work.
	# Optimal - wherever you put the cat on the screen, it will be
	#       free to walk left or right, pushing the boundaries of the
	#       window but not go offscreen.
	#
	# First thing i need to do- stronger info on screen size, as well
	# as current location.
	#
	#

	root.after(1000, lambda: animateForever(root, 0, catsList, actions, sit, cat))
	
	#root.after(30000, destroyFunction)

	root.mainloop()


if __name__ == "__main__":
	main()
