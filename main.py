import tkinter as tk
from tkinter import ttk, Frame, StringVar
from tkinter import *
from PIL import ImageTk, Image
from pytesseract import pytesseract
import numpy as np
import imutils
import cv2 as cv
import re

### Install Dependencies
# pip install opencv-python
# pip install Pillow

regex = r'^[A-Z0-9]{1,5}-*\s*[A-Z0-9]{0,5}$'

### App window
class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # Initialize dashboard
        self.title('Capture Cam [DASHBOARD]')
        self.geometry('400x300')
        self.resizable(0,0)
        # Window icon
        img = Image.open('images/camera.png')
        imgTk = ImageTk.PhotoImage(img, master=self, width=10, height=3)
        self.iconphoto(False, imgTk)

        # When submit button is clicked
        def submit(*args):
            out = format(textbox.get())
            print("Submitted plate: " + out, end = " -> ")
            if not re.match(regex, out):
                print("Rejected!")
                if len(out) > 0 and len(out) < 9:
                    output.config(text = "Error: Invalid plate!")
                elif len(out) >= 9:
                    output.config(text = "Error: String too long!")
                else:
                    output.config(text = "Error: Empty string!")
            else:
                output.config(text = out)
                print("Accepted!")
            textbox.delete(0, tk.END)

        # Format input strings for submit
        def format(string):
            string = string.upper().replace("-", ' ')
            if len(string) > 3 and len(string) <= 7:
                return string[:3] + ' ' + string[3:]
            elif len(string) > 7:
                return string[:4] + ' ' + string[4:]
            else:
                return string
            
        # Title Image
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

        # Whitespace
        whitespace.grid(row=4, columnspan=3)

        # Output Label
        outputTitle = ttk.Label(self, text='Current plate')
        outputTitle.grid(column=0, row=5, padx=5, columnspan=3, sticky='w')
        # Output Info
        global output
        output = ttk.Label(
            self,
            text="---",
            font=("Arial", 25),
        )
        output.grid(column=0, row=6, pady=25, columnspan=3)

def camera():
    vid = cv.VideoCapture(1)

    while(True):
        ret, frame = vid.read()
        cv.imshow('frame', frame)
        
        if cv.waitKey(1) & 0xFF == ord('q'):
            img_name = "images/opencv_frame.png"
            cv.imwrite(img_name, frame)
            break

    vid.release()
    cv.destroyAllWindows()

def read_image():
    pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    path_I = 'images/opencv_frame.png'

    img = cv.imread(path_I, cv.IMREAD_COLOR)
    img = cv.resize(img, (600,400))

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) 
    gray = cv.bilateralFilter(gray, 13, 15, 15) 

    edged = cv.Canny(gray,30,200)
    contours = cv.findContours(edged.copy(), cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(contours)
    contours = sorted(contours, key = cv.contourArea, reverse = True)[:10]
    screenCnt = None

    for c in contours:
        peri = cv.arcLength(c, True)
        approx = cv.approxPolyDP(c, 0.018 * peri, True)
     
        if len(approx) == 4:
            screenCnt = approx
            break
    if screenCnt is None:
        detected = 0
        print ("No contour detected")
    else:
        detected = 1

    if detected == 1:
        cv.drawContours(img, [screenCnt], -1, (0, 0, 255), 3)

    mask = np.zeros(gray.shape,np.uint8)
    new_image = cv.drawContours(mask,[screenCnt],0,255,-1,)
    new_image = cv.bitwise_and(img,img,mask=mask)

    (x, y) = np.where(mask == 255)
    (topx, topy) = (np.min(x), np.min(y))
    (bottomx, bottomy) = (np.max(x), np.max(y))
    Cropped = gray[topx:bottomx+1, topy:bottomy+1]

    text_out = pytesseract.image_to_string(Cropped, config='--psm 11')

    print("Plate number is: " + text_out)

    box = App()
    output.config(text = text_out)

    cv.waitKey(0)
    cv.destroyAllWindows()

### Main
if __name__ == "__main__":
    camera()
    read_image()
    
