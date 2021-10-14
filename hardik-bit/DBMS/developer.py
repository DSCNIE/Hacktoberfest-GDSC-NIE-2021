from os import spawnve
from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter.font import Font
from PIL import Image,ImageTk
from tkinter import messagebox
#import mysql.connector 
#import cv2




class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition system")

        title_lbl1=Label(self.root,text="DEVELOPER",font=("times new roman",35,"bold"),bg="white",fg="black")
        title_lbl1.place(x=0,y=0,width=1530,height=45)

        top_img=Image.open(r"img\Coldplay-Photos.jpg")
        top_img=top_img.resize((1530,720),Image.ANTIALIAS)
        self.proimage_top=ImageTk.PhotoImage(top_img)

        left_label=Label(self.root,image= self.proimage_top)
        left_label.place(x=0,y=55,width=1530,height=720)

        #frame
        main_frame=Frame(left_label,bd=2,bg="white")
        main_frame.place(x=850,y=0,width=500,height=600)

        
        top_img1=Image.open(r"img\developer.png")
        top_img1=top_img1.resize((200,200),Image.ANTIALIAS)
        self.proimage_top1=ImageTk.PhotoImage(top_img1)

        left_label=Label(main_frame,image= self.proimage_top1)
        left_label.place(x=300,y=0,width=200,height=200)
        
        #developer info
        dev_label=Label(main_frame,text="hello my name,Hardik",font=("times new roman",15,"bold"),bg="white",fg="blue")
        dev_label.place(x=0,y=5)

        dev_label2=Label(main_frame,text="I am a Full Stack Developer",font=("times new roman",15,"bold"),bg="white",fg="blue")
        dev_label2.place(x=0,y=40)

        top_img2=Image.open(r"img\dev2.jfif")
        top_img2=top_img2.resize((490,390),Image.ANTIALIAS)
        self.proimage_top2=ImageTk.PhotoImage(top_img2)

        left_label=Label(main_frame,image= self.proimage_top2)
        left_label.place(x=0,y=210,width=490,height=390)
        






if __name__=="__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()