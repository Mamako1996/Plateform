import cv2
import pytesseract
import openpyxl
import re

# new Excel file making
wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = 'Testing Data'
sheet.append(['Number', 'UV Transmission', 'IR Transmission', 'VL Transmission'])

# Tesseract-OCR path
pytesseract.pytesseract.tesseract_cmd = pytesseract.pytesseract.tesseract_cmd = r"C:\Program " \
                                                                                r"Files\Tesseract-OCR\tesseract.exe "
# Image open
img = cv2.imread("Test1.jpg")
# Resizing for scan
img = cv2.resize(img, None, fx=1.1, fy=1.1)

img = img[0:750, 200:460]

# threshold method for dividing the clearer color block
ret, r1 = cv2.threshold(img, 191, 255, cv2.THRESH_BINARY)
rz = cv2.cvtColor(r1, cv2.COLOR_BGR2GRAY)
ret, rr = cv2.threshold(rz, 0, 255, cv2.THRESH_BINARY)
# extract the text from image
text = pytesseract.image_to_string(rr)
text = text.replace(" ", "")
text = text.replace(",", ".")

testchar = 0
a = re.findall(r"\d+\.?\d*", text)
# make a cell to hold the data
if len(a) == 3:
    for n in range(3):
        a[n] = str(round(float(a[n]), 1))

print(a)
sheet.append(a)
cv2.imshow('img', img)
cv2.imshow('r1', r1)
cv2.imshow('rz', rz)
cv2.imshow('rr', rr)
cv2.waitKey(0)
#wb.save('Testing.xlsx')
