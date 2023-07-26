from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("Clock") # setting title of the widget
bg = PhotoImage(file = "pic1 (Custom).png") # creating image

root.geometry("500x284") # specifing size
canvas = Canvas( root, width = 500,height = 284) # constructing a canvas
canvas.pack(fill = "both", expand = True)
canvas.create_image(0,0,image = bg , anchor = "nw") # setting image as background image

def time():
    string = strftime("%I:%M:%S:%p") # making string of time
    canvas.after(1000, time) # setting recall
    canvas.create_image(0,0,image = bg , anchor = "nw") # recreating canvas for refreshing the image every time the function is called
    canvas.create_text(250,142,text= string, font= ("DS-Digital",72, "bold" , "italic")) # displying the string(time)

time() # function call
mainloop() # runs the program in loop