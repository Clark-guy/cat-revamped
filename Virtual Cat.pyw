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


#global vars
catColor = "white"

def main():
        
        catsList = [
                "cats/cat.txt",	#0 sitting
                "cats/cat0.txt",#1 sitting blink
                "cats/cat1.txt",#2 standing
                "cats/cat2.txt",#3 walk1
                "cats/cat3.txt",#4 walk2
                "cats/cat4.txt",#5 sitting look left
                "cats/cat5.txt",#6 sitting look left blink
                "cats/cat6.txt",#7 sleep1
                "cats/cat7.txt"]#8 sleep2

        #turn into dictionary TODO
        sit = [0,0,1,0,0,1,0,0]
        lookLeft = [5,5,6,5,5,6,5,5]
        walk = [3,4,3,4,3,4]
        sleep = [7,8,7,8,7,8,7,8]
        actions = [sit, walk, lookLeft, sleep]

        #window creation
        print("running")
        alphaColor = "orange"
        root = Tk()
        root.configure(bg=alphaColor)
        root.minsize(width=300, height=180)
        root.geometry("300x180+970+490")
        root.overrideredirect(1)
        root.attributes('-alpha', 1)
        root.attributes('-topmost', True)
        #catColor = "white"
        global catColor
        

        img = ImageTk.PhotoImage(Image.open("images/paw.png").resize((20,20), Image.LANCZOS))
        #img = img.resize((10,10), Image.ANTIALIAS)

        fontTuple = ("Fixedsys", 10, "bold")
        b = Button(root, relief="flat", command=lambda: colorSwitch(b), bg=alphaColor, fg=catColor, justify=LEFT, text="\n"+drawCat(0, catsList).read())
        b.configure(font= fontTuple)
        panel1 = Button(root, image = img, bg="blue", command=lambda: colorSwitch(b))
        panel = Button(root, image = img, bg="red", command=root.destroy)

        #pack panels
        panel.pack(side="right", fill = "none", expand = "no", anchor=SE)
        panel1.pack(side="right", fill = "none", expand = "no", anchor=SE)
        b.pack()

        root.wm_attributes("-transparentcolor", alphaColor)

        #can call many of these concurrently - maybe one to manage statuses, one for view?
        # maybe would be better to consolidate all to one function, and go from there
        #
        #idea 1 - create object cat, pass to root.after function below, call object method to increase hunger and sleepiness from within that
        #
        #root.after(1000, lambda: drawAnimate(0, catsArray, b))
        root.after(1000, lambda: animateForever(root, 0, catsList, actions, sit, b))
        #root.after(30000, destroyFunction)

        root.mainloop()


if __name__ == "__main__":
        main()
