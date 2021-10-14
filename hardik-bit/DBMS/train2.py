import os
from tkinter import Label, Tk, messagebox, Button

import cv2
import numpy as np
from PIL import Image, ImageTk


class Train:
    def __init__(self, win_tk_root):  # constructor
        print("hello ", __name__)
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
        title_label = Label(self.root, text = "Train Face Data", font = ("Times New Roman", 35, "bold"),
                            background = "Black", foreground = "Cyan")
        title_label.place(x = 0, y = 0, width = screen_width, height = 45)

        top_image = Image.open("img\facialrecognition.png")
        top_image = top_image.resize((screen_width, screen_height), Image.ANTIALIAS)
        self.top_photo_image = ImageTk.PhotoImage(top_image)
        top_image_label = Label(self.root, image = self.top_photo_image)
        top_image_label.place(x = 0, y = 45, width = screen_width, height = screen_height)
        train_data_button = Button(self.root, text = "Train Data", command = self.train_classifier, cursor = "hand2",
                                   font = ("Times New Roman", 30, "bold"), background = "Green", foreground = "White")
        train_data_button.place(x = 50, y = screen_height - 100, width = screen_width * 0.2, height = 60)

    @staticmethod
    def train_classifier():
        data_dir = "face_data"
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]
        faces = []
        ids = []
        for image in path:
            img = Image.open(image).convert('L')  # gray scale image
            image_np = np.array(img, 'uint8')
            face_id = int(os.path.split(image)[1].split('_')[1])
            faces.append(image_np)
            ids.append(face_id)
            cv2.imshow("Training", image_np)
            cv2.waitKey(1) == 13
        ids = np.array(ids)

        # now train the classifier and save

        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training datasets completed!")

def test():
    print(__name__)
    print("tested")

if __name__ == '__main__':
    winTk = Tk()
    flag = True
    obj = Train(winTk)


    def on_closing():
        close = messagebox.askyesno("Close", "Are you sure you want to exit the System ?")
        if close:
            winTk.destroy()


    if flag:
        winTk.protocol("WM_DELETE_WINDOW", on_closing)
    winTk.mainloop()