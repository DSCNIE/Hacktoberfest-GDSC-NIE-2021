from tkinter import *
from tkinter import ttk, Tk
from tkinter.font import Font
import tkinter
from PIL import Image,ImageTk
from tkinter import messagebox
from mystudent import Student
import os
from time import strftime
from datetime import datetime
from mystudent import Student
from mytrain import Train
from myface_recognisation import DetectFace
from developer import Developer
from help import Help
from attendance import Attendance

class AAS:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition system")

        #image1
        img=Image.open(r"img\facialreco.jfif")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.proimage=ImageTk.PhotoImage(img)

        flbl1=Label(self.root,image= self.proimage)
        flbl1.place(x=0,y=0,width=450,height=130)

        #image2
        img1=Image.open(r"img\facialrecognition.png")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.proimage1=ImageTk.PhotoImage(img1)

        flbl1=Label(self.root,image= self.proimage1)
        flbl1.place(x=458,y=0,width=450,height=130)

        #image3
        img2=Image.open(r"img\img3.png")
        img2=img2.resize((500,130),Image.ANTIALIAS)
        self.proimage2=ImageTk.PhotoImage(img2)

        flbl1=Label(self.root,image= self.proimage2)
        flbl1.place(x=916,y=0,width=450,height=130)

        #bg_img       
        img3=Image.open(r"img\bg1.jpg")
        img3=img3.resize((1366,638),Image.ANTIALIAS)
        self.proimage3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image= self.proimage3)
        bg_img.place(x=0,y=130,width=1366,height=638)

        title_lbl1=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",25,"bold"),bg="white",fg="black")
        title_lbl1.place(x=0,y=0,width=1366,height=45)

#********************************************time***********************************************************

        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000, time)
        
        lbl = Label(title_lbl1, font = ('times new roman',14,'bold'),background = 'white', foreground = 'black')
        lbl.place(x=0,y=0,width=110,height=50)
        time()

        #Student Button Image
        img4=Image.open(r"img\studentdetails.jfif")
        img4=img4.resize((200,140),Image.ANTIALIAS)
        self.proimage4=ImageTk.PhotoImage(img4)
        
        b1=Button(bg_img,image=self.proimage4,command=self.student_details,cursor="hand2")
        b1.place(x=120,y=100,width=200,height=140)

        b1_title=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="red")
        b1_title.place(x=120,y=240,width=200,height=40)

        #Detect Face Button
        img5=Image.open(r"img\facedetector.jfif")
        img5=img5.resize((200,140),Image.ANTIALIAS)
        self.proimage5=ImageTk.PhotoImage(img5)
        
        b1=Button(bg_img,image=self.proimage5,cursor="hand2", command=self.face_data)
        b1.place(x=400,y=100,width=200,height=140)

        b1_title=Button(bg_img,text="Face Detector",cursor="hand2", command=self.face_data, font=("times new roman",15,"bold"),bg="blue",fg="red")
        b1_title.place(x=400,y=240,width=200,height=40)

        #Attenddance Button
        img6=Image.open(r"img\attendance.jfif")
        img6=img6.resize((200,140),Image.ANTIALIAS)
        self.proimage6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.proimage6,cursor="hand2",command=self.attendance_data)
        b1.place(x=680,y=100,width=200,height=140)

        b1_title=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="blue",fg="red")
        b1_title.place(x=680,y=240,width=200,height=40)

        #Help Button
        img7=Image.open(r"img\helpdesk.png")
        img7=img7.resize((200,140),Image.ANTIALIAS)
        self.proimage7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.proimage7,cursor="hand2",command=self.help_data)
        b1.place(x=960,y=100,width=200,height=140)

        b1_title=Button(bg_img,text="Help Desk",cursor="hand2",command=self.help_data,font=("times new roman",15,"bold"),bg="blue",fg="red")
        b1_title.place(x=960,y=240,width=200,height=40)

        #Train Face Button
        img8=Image.open(r"img\traindata.png")
        img8=img8.resize((200,140),Image.ANTIALIAS)
        self.proimage8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.proimage8,cursor="hand2", command=self.train_data)
        b1.place(x=120,y=340,width=200,height=140)

        b1_title=Button(bg_img,text="Train Data",cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="red")
        b1_title.place(x=120,y=480,width=200,height=40)
        
        #Photos Face Button 
        img9=Image.open(r"img\photos.png")
        img9=img9.resize((200,140),Image.ANTIALIAS)
        self.proimage9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.proimage9,cursor="hand2",command=self.open_img)
        b1.place(x=400,y=340,width=200,height=140)

        b1_title=Button(bg_img,text="Photos",cursor="hand2", command=self.open_img,font=("times new roman",15,"bold"),bg="blue",fg="red")
        b1_title.place(x=400,y=480,width=200,height=40)

        #Developer Button
        img10=Image.open(r"img\developer.png")
        img10=img10.resize((200,140),Image.ANTIALIAS)
        self.proimage10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.proimage10,cursor="hand2",command=self.develop_data)
        b1.place(x=680,y=340,width=200,height=140)

        b1_title=Button(bg_img,text="Developer",cursor="hand2",command=self.develop_data,font=("times new roman",15,"bold"),bg="blue",fg="red")
        b1_title.place(x=680,y=480,width=200,height=40)
        
        #Exit Button
        img11=Image.open(r"img\exit1.jfif")
        img11=img11.resize((200,140),Image.ANTIALIAS)
        self.proimage11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.proimage11,cursor="hand2",command=root.destroy)
        b1.place(x=960,y=340,width=200,height=140)

        b1_title=Button(bg_img,text="Exit",cursor="hand2",command=root.destroy, font=("times new roman",15,"bold"),bg="blue",fg="red")
        b1_title.place(x=960,y=480,width=200,height=40)

    def open_img(self):
        os.startfile("data")



#******************************************Function buttons*****************************************
    
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=DetectFace(self.new_window)

    def develop_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)


if __name__=="__main__":
    root=Tk()
    obj=AAS(root)
    root.mainloop()
