import cv2
import pytesseract
import openpyxl
import re

# new Excel file making
# wb = openpyxl.Workbook()
# sheet = wb.active
# sheet.title = 'Testing Data'
# sheet.append(['Number', 'UV Transmission', 'IR Transmission', 'VL Transmission'])

# Tesseract-OCR path
pytesseract.pytesseract.tesseract_cmd = pytesseract.pytesseract.tesseract_cmd = r"C:\Program " \
                                                                                r"Files\Tesseract-OCR\tesseract.exe "
# Image open
img = cv2.imread('qqqq.jpg')

# Resizing for scan
img = cv2.resize(img, None, fx=0.15, fy=0.15)

# threshold method for dividing the clearer color block
ret, r1 = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY)
rz = cv2.cvtColor(r1, cv2.COLOR_BGR2GRAY)
ret1, rr = cv2.threshold(rz, 200, 255, cv2.THRESH_BINARY)

# ret1b, bb = cv2.threshold(rr, 0, 255, cv2.THRESH_BINARY_INV)
# extract the text from image
# text = pytesseract.image_to_string(adaptive_threshold)

# print it out for checking
# print(text + "\n")

# make a cell to hold the data

# a = re.findall(r"\d+\.?\d*", text)
# print(a)
# sheet.append(a)

cv2.imshow('Result', img)
cv2.imshow('Results1', r1)
cv2.imshow('Results2', rz)
cv2.imshow('Results3', rr)
# cv2.imshow('Results4', bb)
cv2.waitKey(0)
# wb.save('Testing.xlsx')
