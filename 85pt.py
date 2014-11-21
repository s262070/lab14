from Tkinter import *
root = Tk()
drawpadwidth = 480
drawpadheight = 320
drawpad = Canvas(root, width=drawpadwidth, height=drawpadheight, background='white')
oval = drawpad.create_oval(160,160,320,320, fill="red")

class MyApp:
    def __init__(self, parent):
# Make sure the drawpad is accessible from inside the function
        global drawpad
        self.myParent = parent
        self.myContainer1 = Frame(parent)
        self.myContainer1.pack()
        self.button1 = Button(self.myContainer1)
        self.button1.configure(text="Left", background= "green")
        self.button1.grid(row=0,column=0)
        # "Bind" an action to the first button
        self.button1.bind("<Button-1>", self.button1Click)
        self.button2 = Button(self.myContainer1)
        self.button2.configure(text="right", background= "green")
        self.button2.grid(row=0,column=1)
        # "Bind" an action to the first button
        self.button2.bind("<Button-1>", self.button2Click)
# This creates the drawpad - no need to change this
        drawpad.pack()
    def button1Click(self, event):
        global oval
        global drawpad
        global drawpadwidth
        global drawpadheight
        x1,y1,x2,y2 = drawpad.coords(oval)
        if x1 > 0:
            drawpad.move(oval,-20,0)
    def button2Click(self, event):
        global oval
        global drawpad
        global drawpadwidth
        global drawpadheight
        x1,y1,x2,y2 = drawpad.coords(oval)
        if x2 < 475:
            drawpad.move(oval,20,0)
        # Add the button2Click method
myapp = MyApp(root)

root.mainloop()