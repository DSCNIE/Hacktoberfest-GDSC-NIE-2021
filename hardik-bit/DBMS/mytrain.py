from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector 
import cv2
import os
import numpy as np

class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("face Recognition system")


        title_lbl1=Label(self.root,text="TRAIN DATA SET",font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
        title_lbl1.place(x=0,y=0,width=1530,height=45)

        top_img=Image.open(r"img\facialrecognition.png")
        top_img=top_img.resize((1530,325),Image.ANTIALIAS)
        self.proimage_top=ImageTk.PhotoImage(top_img)

        left_label=Label(self.root,image= self.proimage_top)
        left_label.place(x=0,y=55,width=1530,height=325)

        # button
        b1_title=Button(self.root,text="TRAIN DATA", command=self.train_classifier, cursor="hand2",font=("times new roman",30,"bold"),bg="red",fg="white")
        b1_title.place(x=0,y=380,width=1530,height=60)

        bottom_img=Image.open(r"img\1_5TRuG7tG0KrZJXKoFtHlSg.jpeg")
        bottom_img=bottom_img.resize((1530,325),Image.ANTIALIAS)
        self.proimage_bottom=ImageTk.PhotoImage(bottom_img)

        left_label=Label(self.root,image= self.proimage_top)
        left_label.place(x=0,y=440,width=1530,height=325)

    def train_classifier(self):
        data_dir=("Data")
        path=[os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') #gray scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1]) 
            
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==2
        ids=np.array(ids)

        #====================== Train the classifier And Save ===================
        clf=cv2.face.LBPHFaceRecognizer_create() 
        clf.train(faces,ids) 
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!!")

if __name__=="__main__":
    root=Tk() 
    obj=Train(root)
    root.mainloop()