from tkinter import *
from tkinter import messagebox

root= Tk()
root.title("Tick-Tac-Toe")
root.iconbitmap('images/file.ico') #Only ICO extension files allowed use png_to_ico.py to convert 
clicked=True
count=0
winner=False
#Buttons There will be 9 Buttons according to rules of tick-tac-toe
b1= Button(root,text=" ",font=("bold",20),height=4,width=6,bg="White",command=lambda: b_click(b1))
b2= Button(root,text=" ",font=("bold",20),height=4,width=6,bg="White",command=lambda: b_click(b2))
b3= Button(root,text=" ",font=("bold",20),height=4,width=6,bg="White",command=lambda: b_click(b3))
b4= Button(root,text=" ",font=("bold",20),height=4,width=6,bg="White",command=lambda: b_click(b4))
b5= Button(root,text=" ",font=("bold",20),height=4,width=6,bg="White",command=lambda: b_click(b5))
b6= Button(root,text=" ",font=("bold",20),height=4,width=6,bg="White",command=lambda: b_click(b6))
b7= Button(root,text=" ",font=("bold",20),height=4,width=6,bg="White",command=lambda: b_click(b7))
b8= Button(root,text=" ",font=("bold",20),height=4,width=6,bg="White",command=lambda: b_click(b8))
b9= Button(root,text=" ",font=("bold",20),height=4,width=6,bg="White",command=lambda: b_click(b9))
#Grid Buttons to screen(adjust the grid of buttons)
# for row = 0: 
b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)
#for row = 1:
b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)
#for row = 2:
b7.grid(row=2, column=0)
b8.grid(row=2, column=1)
b9.grid(row=2, column=2)
#To disable the board after winner is found
def disable_all():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)
#To find winnder
def checkwin():
    global winner
    winner=False
    #checking for X winner
    if b1["text"]=="X" and b2["text"]=="X" and b3["text"]=="X":
        b1.config(bg="Red")
        b2.config(bg="Red")
        b3.config(bg="Red")
        winner=True
        messagebox.showinfo("Tick-Tac-Toe","Player X Wins")
        disable_all()
    elif b4["text"]=="X" and b5["text"]=="X" and b6["text"]=="X":
        b4.config(bg="Red")
        b5.config(bg="Red")
        b6.config(bg="Red")
        winner=True
        messagebox.showinfo("Tick-Tac-Toe","Player X Wins")
        disable_all()
    elif b7["text"]=="X" and b8["text"]=="X" and b9["text"]=="X":
        b7.config(bg="Red")
        b8.config(bg="Red")
        b9.config(bg="Red")
        winner=True
        messagebox.showinfo("Tick-Tac-Toe","Player X Wins")
        disable_all()
    elif b1["text"]=="X" and b4["text"]=="X" and b7["text"]=="X":
        b1.config(bg="Red")
        b4.config(bg="Red")
        b7.config(bg="Red")
        winner=True
        messagebox.showinfo("Tick-Tac-Toe","Player X Wins")
        disable_all()
    elif b2["text"]=="X" and b5["text"]=="X" and b8["text"]=="X":
        b2.config(bg="Red")
        b5.config(bg="Red")
        b8.config(bg="Red")
        winner=True
        messagebox.showinfo("Tick-Tac-Toe","Player X Wins")
        disable_all()
    elif b3["text"]=="X" and b6["text"]=="X" and b9["text"]=="X":
        b3.config(bg="Red")
        b6.config(bg="Red")
        b9.config(bg="Red")
        winner=True
        messagebox.showinfo("Tick-Tac-Toe","Player X Wins")
        disable_all()
    
    elif b3["text"]=="X" and b5["text"]=="X" and b7["text"]=="X":
        b3.config(bg="Red")
        b5.config(bg="Red")
        b7.config(bg="Red")
        winner=True
        messagebox.showinfo("Tick-Tac-Toe","Player X Wins")
        disable_all()
    elif b1["text"]=="X" and b5["text"]=="X" and b9["text"]=="X":
        b1.config(bg="Red")
        b5.config(bg="Red")
        b9.config(bg="Red")
        winner=True
        messagebox.showinfo("Tick-Tac-Toe","Player X Wins")
        disable_all()
    #checking for O winner
    elif b1["text"]=="O" and b2["text"]=="O" and b3["text"]=="O":
        b1.config(bg="Red")
        b2.config(bg="Red")
        b3.config(bg="Red")
        winner=True
        messagebox.showinfo("Tick-Tac-Toe","Player O Wins")
        disable_all()
    elif b4["text"]=="O" and b5["text"]=="O" and b6["text"]=="O":
        b4.config(bg="Red")
        b5.config(bg="Red")
        b6.config(bg="Red")
        winner=True
        messagebox.showinfo("Tick-Tac-Toe","Player O Wins")
        disable_all()
    elif b7["text"]=="O" and b8["text"]=="O" and b9["text"]=="O":
        b7.config(bg="Red")
        b8.config(bg="Red")
        b9.config(bg="Red")
        winner=True
        messagebox.showinfo("Tick-Tac-Toe","Player O Wins")
        disable_all()
    elif b1["text"]=="O" and b4["text"]=="O" and b7["text"]=="O":
        b1.config(bg="Red")
        b4.config(bg="Red")
        b7.config(bg="Red")
        winner=True
        messagebox.showinfo("Tick-Tac-Toe","Player O Wins")
        disable_all()
    elif b2["text"]=="O" and b5["text"]=="O" and b8["text"]=="O":
        b2.config(bg="Red")
        b5.config(bg="Red")
        b8.config(bg="Red")
        winner=True
        messagebox.showinfo("Tick-Tac-Toe","Player O Wins")
        disable_all()
    elif b3["text"]=="O" and b6["text"]=="O" and b9["text"]=="O":
        b3.config(bg="Red")
        b6.config(bg="Red")
        b9.config(bg="Red")
        winner=True
        messagebox.showinfo("Tick-Tac-Toe","Player O Wins")
        disable_all()
    
    elif b3["text"]=="O" and b5["text"]=="O" and b7["text"]=="O":
        b3.config(bg="Red")
        b5.config(bg="Red")
        b7.config(bg="Red")
        winner=True
        messagebox.showinfo("Tick-Tac-Toe","Player O Wins")
        disable_all()
    elif b1["text"]=="O" and b5["text"]=="O" and b9["text"]=="O":
        b1.config(bg="Red")
        b5.config(bg="Red")
        b9.config(bg="Red")
        winner=True
        messagebox.showinfo("Tick-Tac-Toe","Player O Wins")
        disable_all()
    if count==9 and winner==False:
        messagebox.showinfo("Tick-Tac-Toe","This round is a tie! Try Again")
        disable_all() 
#Button clicked Function
def b_click(b):
    global clicked,count
    if b["text"]==" " and clicked==True:
        b["text"] = "X"
        clicked = False
        count+=1
        checkwin()
    elif b["text"]==" " and clicked==False:
        b["text"] = "O"
        clicked = True
        count+=1
        checkwin()
    else:
        messagebox.showerror("Tick-Tac-Toe","That is Already Selected Choose any other Box Empty")

root.mainloop()
