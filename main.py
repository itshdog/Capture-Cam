import tkinter as tk
from tkinter import ttk, Frame, StringVar
from tkinter import *
from PIL import ImageTk, Image
import cv2
import re

### Install Dependencies
# pip install opencv-python
# pip install Pillow

regex = r'^[A-Z0-9]{0,4}-*\s*[A-Z0-9]{0,4}$'

### App window
class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # Initialize dashboard
        self.title('Capture Cam [DASHBOARD]')
        self.geometry('400x300')
        self.resizable(0,0)
        img = Image.open('images/camera.png')
        imgTk = ImageTk.PhotoImage(img, master=self, width=10, height=3)
        self.iconphoto(False, imgTk)

        def submit(*args):
            out = format(textbox.get())
            print("Submitted plate: " + out, end = " ")
            if not re.match(regex, out):
                output.config(text = "Invalid Plate!")
                print("-> Rejected!")
            else:
                output.config(text = out)
                print("-> Accepted!")
            textbox.delete(0, tk.END)

        def format(string):
            string = string.upper().replace("-", ' ')
            if len(string) > 3 and len(string) <= 7:
                return string[:3] + ' ' + string[3:]
            elif len(string) > 7:
                return string[:4] + ' ' + string[4:]
            else:
                return string
            
        # Image
        img = Image.open('images/app-title.png')
        imgResize = img.resize((400,96))
        imgTk = ImageTk.PhotoImage(imgResize, master=self, width=10, height=2)
        imgLabel = ttk.Label(
            self,
            image=imgTk
        )
        imgLabel.image = imgTk
        imgLabel.grid(row=0, columnspan=3)
        # Whitespace
        whitespace = ttk.Label(
            self,
            text=' ',
        )
        whitespace.grid(row=1, columnspan=3)
        # Edit Label
        label = ttk.Label(self, text='Edit license plate')
        label.grid(column=0, row=2, padx=5, columnspan=3, sticky='w')
        # Edit Entrybox
        textbox = ttk.Entry(self)
        textbox.bind('<Return>', submit)
        textbox.grid(column=0, row=3, ipadx=90, padx=5, columnspan=2)
        # Edit Button
        btn = ttk.Button(self, command=submit, text='Submit')
        btn.grid(column=2, row=3)

        whitespace.grid(row=4, columnspan=3)

        # Output Label
        outputTitle = ttk.Label(self, text='Current plate')
        outputTitle.grid(column=0, row=5, padx=5, columnspan=3, sticky='w')
        # Output Info
        output = ttk.Label(
            self,
            text="---",
            font=("Arial", 25),
        )
        output.grid(column=0, row=6, pady=25, columnspan=3)
            
### Initialize Camera
cap = cv2.VideoCapture(0)
root = tk.Tk()
root.resizable(0,0)
root.title('Capture Cam [INPUT]')
img = Image.open('images/camera.png')
imgTk = ImageTk.PhotoImage(img, master=root, width=10, height=3)
root.iconphoto(False, imgTk)
lmain = ttk.Label(root)
lmain.grid()

### Camera Input
def video_stream():
    _, frame = cap.read()
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(1, video_stream) 

### Main
if __name__ == "__main__":
    app = App()
    video_stream()
    app.mainloop()
