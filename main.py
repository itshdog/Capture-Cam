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
        self.style = ttk.Style(self)

        # title
        title = ttk.Label(
            self,
            text='Capture Cam',
            font=('Arial', 20)
        )
        title.grid(row=0, columnspan=3)
        subtitle = ttk.Label(
            self,
            text='University of Iowa Hackathon 2022',
            font=('Arial', 8)
        )
        subtitle.grid(row=1, columnspan=3)
        whitespace = ttk.Label(
            self,
            text=' ',
        )
        whitespace.grid(row=2, columnspan=3)

        # label
        label = ttk.Label(self, text='Input license plate')
        label.grid(column=0, row=3, padx=5, columnspan=3, sticky='w')
        # entry
        textbox = ttk.Entry(self)
        textbox.grid(column=0, row=4, ipadx=90, padx=5, columnspan=2)
        # button
        btn = ttk.Button(self, text='Submit')
        btn.grid(column=2, row=4)

### Initialize Camera
cap = cv2.VideoCapture(0)
# Tkinter frame
root = tk.Tk()
root.title('Capture Cam [INPUT]')
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
