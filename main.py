import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import cv2

### Install Dependencies
# pip install opencv-python
# pip install Pillow

### App window
class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Capture Cam')
        self.geometry('400x300')
        self.style = ttk.Style(self)

        # label
        label = ttk.Label(self, text='Capture Cam')
        label.pack()

### Initialize Camera
cap = cv2.VideoCapture(0)
lmain = ttk.Label()
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
