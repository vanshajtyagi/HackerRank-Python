from tkinter import Tk
from tkinter.filedialog import askopenfilename
import cv2
pytesseract.pytesseract.tesseract_cmd =r"c:\Program Files(x86)\Tesseract-OCR\tesseract.exe"
#first we would ask the user to select the desired image 
Tk().withdraw()
file = askopenfilename()
image = cv2.imread(file)
text = pytesseract.image_to_string(image)
print ("Number on the car is :", text)
