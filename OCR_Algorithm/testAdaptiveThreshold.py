import cv2
import pytesseract
import openpyxl
import re

# new Excel file making
from cv2 import adaptiveThreshold, ADAPTIVE_THRESH_MEAN_C, THRESH_BINARY, ADAPTIVE_THRESH_GAUSSIAN_C

wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = 'Testing Data'
sheet.append(['Number', 'UV Transmission', 'IR Transmission', 'VL Transmission'])

# Tesseract-OCR path
pytesseract.pytesseract.tesseract_cmd = pytesseract.pytesseract.tesseract_cmd = r"C:\Program " \
                                                                                r"Files\Tesseract-OCR\tesseract.exe "
# Image open
img1 = cv2.imread("Test1.jpg")
# Resizing for scan
img1 = cv2.resize(img1, None, fx=1.1, fy=1.1)

img1 = img1[0:750, 200:460]
ret, rr = cv2.threshold(img1, 150 , 255, cv2.THRESH_BINARY)
img = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

# threshold method for dividing the clearer color block
r1 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 25, 10)
r2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 25, 10)

# extract the text from image
text = pytesseract.image_to_string(r1)
text = text.replace(" ", "")
text = text.replace(",", ".")
text2 = pytesseract.image_to_string(r2)
text2 = text2.replace(" ", "")
text2 = text2.replace(",", ".")
# print it out for checking
#print(text + "\n")
#print(text2 + "\n")
# make a cell to hold the data

a = re.findall(r"\d+\.?\d*", text)
#print(a)
if len(a) == 3:
    for n in range(3):
        a[n] = str(round(float(a[n]), 1))

#print(a)
sheet.append(a)
#cv2.imshow('img1', img1)
#cv2.imshow('img', img)
cv2.imshow('new', rr)
#cv2.imshow('Mean', r1)
#cv2.imshow('GAUSSIAN', r2)
cv2.waitKey(0)
print(img1)
print("------------------------------------------------------")
print(rr)
#wb.save('Testing.xlsx')
