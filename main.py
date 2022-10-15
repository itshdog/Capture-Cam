import tkinter as tk
from tkinter import ttk, Frame
from PIL import ImageTk, Image
import cv2

### Install Dependencies
# pip install opencv-python
# pip install Pillow

### App window
class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Capture Cam [DASHBOARD]')
        self.geometry('400x300')
        img = Image.open('images/camera.png')
        imgTk = ImageTk.PhotoImage(img, master=self, width=10, height=3)
        self.iconphoto(False, imgTk)

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
        # label
        label = ttk.Label(self, text='Input license plate')
        label.grid(column=0, row=2, padx=5, columnspan=3, sticky='w')
        # entry
        textbox = ttk.Entry(self)
        textbox.grid(column=0, row=3, ipadx=90, padx=5, columnspan=2)
        # button
        btn = ttk.Button(self, text='Submit')
        btn.grid(column=2, row=3)

### Initialize Camera
cap = cv2.VideoCapture(0)
root = tk.Tk()
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
