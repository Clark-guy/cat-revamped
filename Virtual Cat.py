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
                root.overrideredirect(0)
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
		choice = random.randint(0,3)
		match choice:
			case 0:
				currentAction = actions[0]
			case 1:
				currentAction = actions[1]
			case 2:
				currentAction = actions[2]
			case _:
				currentAction = actions[3]
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

def test(root, interval, maxSize):
        global winX
        global winY
        global posX
        global posY
        if(winX < maxSize):
                winX +=interval
                posX +=interval
                root.after(100, lambda: test(root, interval, maxSize))
                root.geometry(str(winX)+"x"+
                              str(winY)+
                              "+"+
                              str(winY+200-posX)+"+"+
                              str(posY))
        print(interval)
        print(maxSize)



#global vars
catColor = "gray1"
invisibleWindow = 0
winX = 300
winY = 180
posX = 100
posY = 100


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
                "cats/catL.txt",#0L sitting
                "cats/cat0L.txt",#1L sitting blink
                "cats/cat1L.txt",#2L standing left
                "cats/cat2L.txt",#3L walk1 left
                "cats/cat3L.txt",#4L walk2 left
                "cats/cat4L.txt",#5L sitting look left
                "cats/cat5L.txt",#6L sitting look left blink
                "cats/cat6L.txt",#7L sleep1
                "cats/cat7L.txt"]#8L sleep2

        #turn into dictionary TODO
        sit = [0,0,1,0,0,1,0,0]
        sitL = [x+1 for x in sit]
        lookLeft = [5,5,6,5,5,6,5,5]
        lookRight = [x+1 for x in lookRight]
        walk = [3,4,3,4,3,4]
        walkL = [x+1 for x in walk]
        sleep = [7,8,7,8,7,8,7,8]
        sleepL = [x+1 for x in sleep]
        actions = [sit, walk, lookLeft, sleep]

        #window creation
        print("running")
        alphaColor = "orange"
        root = Tk()
        root.configure(bg=alphaColor)
        root.minsize(width=300, height=180)
        root.title("Burgle")
        root.geometry("300x180+100+100")

        if fullscreen:
                root.attributes('-fullscreen', True)
                marginy = 45
                marginx = 5
        else:
                #I kinda like this without the overrideredirect
                #root.overrideredirect(1)
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
        catFrame = Frame(root, width=100, height=100)
        buttonFrame = Frame(root, width=100, height=100)
        catFrame.pack(side="left")
        buttonFrame.pack(side="right")


        
        b = Label(catFrame, relief="flat",bg=alphaColor, fg=catColor, justify=LEFT, text="\n"+drawCat(0, catsList).read())
        b.configure(font= fontTuple)
        panel2 = Button(buttonFrame, image = img, bg="green", command=lambda: transparencyFunc(root, alphaColor, panel2))
        panel1 = Button(buttonFrame, image = img, bg="blue", command=lambda: colorSwitch(b))
        panel0 = Button(buttonFrame, image = img, bg="red", command=root.destroy)

        #pack panels
        #panel0.pack(side="right", fill = "none", expand = "no", anchor=SE, pady=marginy)
        #panel1.pack(side="right", fill = "none", expand = "no", anchor=SE, pady=marginy)
        #panel2.pack(side="right", fill = "none", expand = "no", anchor=SE, pady=marginy)
        #b.pack(side="right", anchor=SE, pady=marginy)

        panel0.grid(column=0,row=0, sticky="W")
        panel1.grid(column=0,row=1)
        panel2.grid(column=0,row=2)
        b.grid(column=0,row=0)



        #can call many of these concurrently - maybe one to manage statuses, one for view?
        # maybe would be better to consolidate all to one function, and go from there
        #
        #idea 1 - create object cat, pass to root.after function below, call object method to increase hunger and sleepiness from within that
        #
        #
        #
        # moving cat - 
        #
        #

        root.after(1000, lambda: animateForever(root, 0, catsList, actions, sit, b))
        root.after(100, lambda: test(root, 10, 400))
        
        #root.after(30000, destroyFunction)

        root.mainloop()


if __name__ == "__main__":
        main()
