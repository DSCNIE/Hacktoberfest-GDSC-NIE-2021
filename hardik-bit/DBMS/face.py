import os
from datetime import datetime
from tkinter import Label, Button, Tk
from tkinter import messagebox

import cv2
import mysql.connector
from PIL import Image, ImageTk


def mark_attendance(r, n, d, c):
    if not os.path.exists("attendance_sheet.csv"):
        with open('attendance_sheet.csv', 'x') as operational_file:
            operational_file.close()
    with open("attendance_sheet.csv", "r+", newline = '\n') as operational_file:
        my_data_list = []
        my_data_list = operational_file.readlines()
        name_list = []
        date_list = []
        for line in my_data_list:
            entry = line.split(',')
            print(str(entry))
            name_list.append(entry[0])
            date_list.append(entry[4])
        if (r not in name_list) and (n not in name_list) and (d not in name_list) and (c not in name_list):
            now = datetime.now()
            date = now.strftime("%d/%m/%y")
            time = now.strftime("%H:%M:%S")
            if date not in date_list:
                operational_file.writelines(f"\n{r},{n},{d},{c},{date},{time},Present")
            else:
                pass
        operational_file.close()


class DetectFace:
    def __init__(self, win_tk_root):  # constructor

        # setup for the mainframe of the window
        # window title
        self.root = win_tk_root
        self.root.title("Attendance System")

        # get screen dimensions
        screen_width = win_tk_root.winfo_screenwidth()
        screen_height = win_tk_root.winfo_screenheight()

        self.root.geometry("%dx%d+0+0" % (screen_width, screen_height))  # full screen window
        self.root.resizable(False, False)  # resizable window

        # setup content of the window
        left_image = Image.open("project_images/img_detect_face.jpeg")
        left_image = left_image.resize((round(screen_width * 0.5), screen_height), Image.ANTIALIAS)
        self.left_photo_image = ImageTk.PhotoImage(left_image)
        left_image_label = Label(self.root, image = self.left_photo_image)
        left_image_label.place(x = 0, y = 0, width = screen_width / 2, height = screen_height)

        top_right_image = Image.open("project_images/img_detect_face_side_view.jpg")
        top_right_image = top_right_image.resize((round(screen_width * 0.5), round(screen_height * 0.5)),
                                                 Image.ANTIALIAS)
        self.top_right_photo_image = ImageTk.PhotoImage(top_right_image)
        top_right_image_label = Label(self.root, image = self.top_right_photo_image)
        top_right_image_label.place(x = round(screen_width / 2), y = 0, width = screen_width / 2,
                                    height = screen_height / 2)

        bottom_right_image = Image.open("project_images/img_detect_face_high_tech.png")
        bottom_right_image = bottom_right_image.resize((round(screen_width * 0.5), round(screen_height * 0.5)),
                                                       Image.ANTIALIAS)
        self.bottom_right_photo_image = ImageTk.PhotoImage(bottom_right_image)
        bottom_right_image_label = Label(self.root, image = self.bottom_right_photo_image)
        bottom_right_image_label.place(x = round(screen_width / 2), y = round(screen_height / 2),
                                       width = screen_width / 2,
                                       height = screen_height / 2)
        detect_button = Button(left_image_label, text = "Detect Face for Attendance", command = self.detect_face_fn,
                               cursor = "hand2", font = ("Times New Roman", 18, "bold"), background = "Teal",
                               foreground = "White")
        detect_button.place(x = round(screen_width * 0.1), y = round(screen_height * 0.1),
                            width = round(screen_width * 0.2), height = round(screen_height * 0.08))

    def draw_boundary(self, img, classifier, scaleFactor, minNeighbors, color, text, clf):
        gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)
        coord = []
        for (x, y, w, h) in features:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
            r_id, predict = clf.predict(gray_image[y:y + h, x:x + w])  # r_id here represents roll no.
            confidence = int((100 * (1 - predict / 300)))

            conn = mysql.connector.connect(host = "localhost", username = "root", password = "toor",
                                           database = "attendance_system_using_face_recognition")
            my_cursor = conn.cursor()

            my_cursor.execute("select student_name from student where roll_no=" + str(r_id))
            n = my_cursor.fetchone()
            n = "+".join(n)

            my_cursor.execute("select department from student where roll_no=" + str(r_id))
            d = my_cursor.fetchone()
            d = "+".join(d)

            my_cursor.execute("select course from student where roll_no=" + str(r_id))
            c = my_cursor.fetchone()
            c = "+".join(c)

            if confidence > 77:
                cv2.putText(img, f"Roll no:{r_id}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                cv2.putText(img, f"Name:{n}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                cv2.putText(img, f"Department:{d}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                cv2.putText(img, f"Course :{c}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                mark_attendance(r_id, n, d, c)
            else:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
            coord = [x, y, w, y]
        return coord

    # face detector code stub
    def detect_face_fn(self):
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        def recognize(img, classifier, faceCascade):
            coord = self.draw_boundary(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img

        video_cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome To Face Recognition", img)
            if cv2.waitKey(1) == 27:
                break
            video_cap.release()
            cv2.destroyAllWindows()


if __name__ == '__main__':
    winTk = Tk()
    flag = True
    obj = DetectFace(winTk)


    def on_closing():
        close = messagebox.askyesno("Close", "Are you sure you want to exit the System ?")
        if close:
            winTk.destroy()


    if flag:
        winTk.protocol("WM_DELETE_WINDOW", on_closing)
    winTk.mainloop()
