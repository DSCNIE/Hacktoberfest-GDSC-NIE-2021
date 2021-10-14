from os import spawnve
from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter.font import Font
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector 
import cv2

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("face Recognition system")

        #variables
        self.var_dept=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_USN=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_add=StringVar()
        self.var_teacher=StringVar()
        self.serchTxt_var=StringVar()
        self.search_var=StringVar()
        
        #image1
        img=Image.open(r"img\clg.jpg")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.proimage=ImageTk.PhotoImage(img)

        flbl1=Label(self.root,image= self.proimage)
        flbl1.place(x=0,y=0,width=450,height=130)

        #image2
        img1=Image.open(r"img\student.jpg")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.proimage1=ImageTk.PhotoImage(img1)

        flbl1=Label(self.root,image= self.proimage1)
        flbl1.place(x=458,y=0,width=450,height=130)

        #image3
        img2=Image.open(r"img\girl.jpeg")
        img2=img2.resize((500,130),Image.ANTIALIAS)
        self.proimage2=ImageTk.PhotoImage(img2)

        flbl1=Label(self.root,image= self.proimage2)
        flbl1.place(x=916,y=0,width=450,height=130)

         #bg_img       
        img3=Image.open(r"img\bg1.JPG")
        img3=img3.resize((1366,638),Image.ANTIALIAS)
        self.proimage3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image= self.proimage3)
        bg_img.place(x=0,y=130,width=1366,height=638)

        title_lbl1=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",25,"bold"),bg="white",fg="darkgreen")
        title_lbl1.place(x=0,y=0,width=1366,height=32)
        
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=20,y=55,width=1480,height=600)

        #left side frame
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=2,width=650,height=520)

        left_img=Image.open(r"img\img1s.jpg")
        left_img=left_img.resize((640,100),Image.ANTIALIAS)
        self.proimage_left=ImageTk.PhotoImage(left_img)

        left_label=Label(left_frame,image= self.proimage_left)
        left_label.place(x=5,y=0,width=635,height=100)

        #current course information
        current_course_information=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course information",font=("times new roman",12,"bold"))
        current_course_information.place(x=5,y=90,width=635,height=100)

        # Department 
        dep_label=Label(current_course_information,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=2,pady=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_information,textvariable=self.var_dept,font=("times new roman",10,"bold"),state="read only",width=20)
        dep_combo["values"]=("Select Department","Computer Science","Information Science","Mechanical","Electronics")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #course
        course_label=Label(current_course_information,text="Course",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=2,pady=10,sticky=W)

        course_combo=ttk.Combobox(current_course_information,textvariable=self.var_course,font=("times new roman",10,"bold"),state="read only",width=20)
        course_combo["values"]=("Select Course","FE","SE","TE","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #year
        year_label=Label(current_course_information,text="Year",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=2,sticky=W)

        year_combo=ttk.Combobox(current_course_information,textvariable=self.var_year,font=("times new roman",10,"bold"),state="read only",width=20)
        year_combo["values"]=("Select year","2020-21","2021-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #semester
        sem_label=Label(current_course_information,text="Semester",font=("times new roman",12,"bold"),bg="white")
        sem_label.grid(row=1,column=2,padx=2,sticky=W)

        sem_combo=ttk.Combobox(current_course_information,textvariable=self.var_sem,font=("times new roman",10,"bold"),state="read only",width=20)
        sem_combo["values"]=("Select Semester","1 Sem","2 Sem","3 Sem","4 Sem")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #class student frame
        class_Student_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))
        class_Student_frame.place(x=5,y=190,width=635,height=281)
        
        #student id
        student_id=Label(class_Student_frame,text="StudentID",font=("times new roman",12,"bold"),bg="white")
        student_id.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        student_id_Entry=ttk.Entry(class_Student_frame,textvariable=self.var_USN,width=20,font=("times new roman",10,"bold"))
        student_id_Entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #student name
        student_name=Label(class_Student_frame,text="Student Name:",font=("times new roman",12,"bold"),bg="white")
        student_name.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        student_name_Entry=ttk.Entry(class_Student_frame,textvariable=self.var_std_name,width=20,font=("times new roman",10,"bold"))
        student_name_Entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #class division
        class_division=Label(class_Student_frame,text="Class Division:",font=("times new roman",12,"bold"),bg="white")
        class_division.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        div_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_div,font=("times new roman",10,"bold"),state="read only",width=20)
        div_combo["values"]=("Select Div","A","B","C")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=2,pady=5,sticky=W)
        
        #roll no
        roll_no=Label(class_Student_frame,text="Roll No:",font=("times new roman",12,"bold"),bg="white")
        roll_no.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        roll_no_Entry=ttk.Entry(class_Student_frame,textvariable=self.var_roll,width=20,font=("times new roman",10,"bold"))
        roll_no_Entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
  
        #gender
        gender=Label(class_Student_frame,text="Gender:",font=("times new roman",12,"bold"),bg="white")
        gender.grid(row=2,column=0,padx=10,pady=5,sticky=W)

    
        gender_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_gender,font=("times new roman",10,"bold"),state="read only",width=18)
        gender_combo["values"]=("Select Gender","male","female","other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #dob
        dob=Label(class_Student_frame,text="DOB:",font=("times new roman",12,"bold"),bg="white")
        dob.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        dob_Entry=ttk.Entry(class_Student_frame,textvariable=self.var_dob,width=20,font=("times new roman",10,"bold"))
        dob_Entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

       
        #Email
        Email=Label(class_Student_frame,text="Email:",font=("times new roman",12,"bold"),bg="white")
        Email.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        Email_Entry=ttk.Entry(class_Student_frame,textvariable=self.var_email,width=20,font=("times new roman",10,"bold"))
        Email_Entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #phoneno.
        phone_no=Label(class_Student_frame,text="Phone No:",font=("times new roman",12,"bold"),bg="white")
        phone_no.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phone_no_Entry=ttk.Entry(class_Student_frame,textvariable=self.var_phone,width=20,font=("times new roman",10,"bold"))
        phone_no_Entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)
        
        #address
        address=Label(class_Student_frame,text="Address:",font=("times new roman",12,"bold"),bg="white")
        address.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        address_Entry=ttk.Entry(class_Student_frame,textvariable=self.var_add,width=20,font=("times new roman",10,"bold"))
        address_Entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        #Teachersname
        teacher=Label(class_Student_frame,text="Teachers Name:",font=("times new roman",12,"bold"),bg="white")
        teacher.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        teacher_Entry=ttk.Entry(class_Student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",10,"bold"))
        teacher_Entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        #radiobutton
        self.var_radio1=StringVar()

        radiobutton1=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobutton1.grid(row=5,column=0)


        radiobutton2=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobutton2.grid(row=5,column=1)
        
       
        #buttons frame1
        button_frame1=Frame(class_Student_frame,bd=2,relief=RIDGE)
        button_frame1.place(x=0,y=195,width=630,height=31)

        save_button=Button(button_frame1,text="Save",command=self.add_data,width=15,cursor="hand2",font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_button.grid(row=0,column=0)
        
        update_button=Button(button_frame1,text="Update",command=self.update_data,width=15,cursor="hand2",font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_button.grid(row=0,column=1)

        delete_button=Button(button_frame1,text="Delete",command=self.delete_data,width=15,cursor="hand2",font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_button.grid(row=0,column=2)

        reset_button=Button(button_frame1,text="Reset",command=self.reset_data,width=15,cursor="hand2",font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_button.grid(row=0,column=3)
        
         
        #buttons frame2
        button_frame2=Frame(class_Student_frame,bd=2,relief=RIDGE)
        button_frame2.place(x=0,y=220,width=630,height=31)

        take_photo_button=Button(button_frame2,text="Take Photo Sample",command=self.generate_dataset,width=31,cursor="hand2",font=("times new roman",13,"bold"),bg="blue",fg="white")
        take_photo_button.grid(row=0,column=0)

        update_photo_button=Button(button_frame2,text="Update Photo Sample",command=self.generate_dataset,width=31,cursor="hand2",font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_photo_button.grid(row=0,column=1)

        #Right side frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=670,y=2,width=650,height=545)

        right_img=Image.open(r"img\student.jpg")
        right_img=right_img.resize((640,118),Image.ANTIALIAS)
        self.proimage_right=ImageTk.PhotoImage(right_img)

        right_label=Label(Right_frame,image= self.proimage_right)
        right_label.place(x=5,y=0,width=635,height=118)

        #================ Searching System ==================#

        search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Searching System",font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=123,width=635,height=70)

        #table frame
        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=180,width=580,height=290)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentId")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Roll No")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        
       
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

        #functiondec
    def add_data(self):
        if self.var_dept.get()=="select Department" or self.var_std_name.get()=="" or self.var_USN.get()=="":
                messagebox.showerror("Error","All Fields need to filled",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="7404983564@Ge",database="attendance_database")
                my_cursor=conn.cursor() #quesry is executed using cursor
                my_cursor.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                self.var_dept.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_sem.get(),
                                                                                                                self.var_USN.get(),
                                                                                                                self.var_std_name.get(),
                                                                                                                self.var_div.get(),
                                                                                                                self.var_roll.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_add.get(),
                                                                                                                self.var_teacher.get(),
                                                                                                                self.var_radio1.get()
                                                                                                            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Succesfully Done","The student details have been added",parent=self.root) 
 
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

#fetch data
    def fetch_data(self): 
        conn=mysql.connector.connect(host="localhost",username="root",password="7404983564@Ge",database="attendance_database")
        my_cursor=conn.cursor() #quesry is executed using cursor    
        my_cursor.execute("select * from students")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()  

    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dept.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_sem.set(data[3]),
        self.var_USN.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_add.set(data[12]),
        self.var_teacher.set(data[13])
        self.var_radio1.set(data[14])

#update function
    def update_data(self):
        if self.var_dept.get()=="select Department" or self.var_std_name.get()=="" or self.var_USN.get()=="":
                messagebox.showerror("Error","All Fields need to filled",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update the student details",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="7404983564@Ge",database="attendance_database")
                    my_cursor=conn.cursor()
                    my_cursor.execute("Update students set Department=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,Photosample=%s where USN=%s",(
                                                                                                                                                                                                                    self.var_dept.get(),
                                                                                                                                                                                                                    self.var_course.get(),
                                                                                                                                                                                                                    self.var_year.get(),
                                                                                                                                                                                                                    self.var_sem.get(),
                                                                                                                                                                                                                    self.var_std_name.get(),
                                                                                                                                                                                                                    self.var_div.get(),
                                                                                                                                                                                                                    self.var_roll.get(),
                                                                                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                                                                                    self.var_dob.get(),
                                                                                                                                                                                                                    self.var_email.get(),
                                                                                                                                                                                                                    self.var_phone.get(),
                                                                                                                                                                                                                    self.var_add.get(),
                                                                                                                                                                                                                    self.var_teacher.get(),
                                                                                                                                                                                                                    self.var_radio1.get(),
                                                                                                                                                                                                                    self.var_USN.get()         
                                                                                                                                                                                                                                                                                                                                                                                                                                 
                                                                                                                                                                                                                ))
                else:
                    if not Update:
                        return

                messagebox.showinfo("Success","The details successfully updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)

    def delete_data(self):
        if self.var_USN.get()=="":
            messagebox.showerror("Error","Student USN must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root) 
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="7404983564@Ge",database="attendance_database")
                    my_cursor=conn.cursor()
                    sql="delete from students where USN=%s"
                    val=(self.var_USN.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","successfully deleted Student details",parent=self.root)                        

            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)

#reset
    def reset_data(self):
        self.var_dept.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_sem.set("Select Sem")
        self.var_std_name.set(" ")
        self.var_div("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set(" ")
        self.var_add.set(" ")
        self.var_teacher.set(" ")
        self.var_radio1.set(" ")

    #================ Generate Data Set Or Take Photo Sample =====================
     
    def generate_dataset(self):
        if self.var_dept.get()=="select Department" or self.var_std_name.get()=="" or self.var_USN.get()=="":
                messagebox.showerror("Error","All Fields need to filled",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="7404983564@Ge",database="attendance_database")
                my_cursor=conn.cursor()
                my_cursor.execute("Select * from students")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("Update students set Department=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,Photosample=%s where USN=%s",(
                                                                                                                                                                                                                    self.var_dept.get(),
                                                                                                                                                                                                                    self.var_course.get(),
                                                                                                                                                                                                                    self.var_year.get(),
                                                                                                                                                                                                                    self.var_sem.get(),
                                                                                                                                                                                                                    self.var_std_name.get(),
                                                                                                                                                                                                                    self.var_div.get(),
                                                                                                                                                                                                                    self.var_roll.get(),
                                                                                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                                                                                    self.var_dob.get(),
                                                                                                                                                                                                                    self.var_email.get(),
                                                                                                                                                                                                                    self.var_phone.get(),
                                                                                                                                                                                                                    self.var_add.get(),
                                                                                                                                                                                                                    self.var_teacher.get(),
                                                                                                                                                                                                                    self.var_radio1.get(),
                                                                                                                                                                                                                    self.var_USN.get()==id+1
                                                                                                                                                                                                                    ))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
                conn.commit()   
                self.fetch_data()
                conn.close()

                
                                                                                                                                                                                                              
 #Load Predefined Data On Face Frontal From cv2

                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def faces_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #need to convert colour photos into grayscale
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #1.3- scaling factor
                    #5-Minimum neighbour

                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w] # face will get cropped to this size
                        return face_cropped

                cap=cv2.VideoCapture(0)   #open camera
                img_id=0 # gets captured and stored in this  
                while True:
                    ret,my_frame=cap.read() #we need to read image for processing
                    if faces_cropped(my_frame) is not None:
                        img_id+=1                         # if itd not null then keeps on reading
                        face=cv2.resize(faces_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_path="Data/user."+str(id)+"."+str(img_id)+".jpg"  #joining photo in reference w the USN
                        cv2.imwrite(file_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped photo",face)

                    if cv2.waitKey(1)==6 or int(img_id)==2: #it was 13 and 100 before 
                        break
                cap.release()
                cv2.destroyAllWindows()

                messagebox.showinfo("Result","Generation of data sets completed")

            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)


if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()