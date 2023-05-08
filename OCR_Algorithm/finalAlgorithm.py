import cv2
import pytesseract
import openpyxl
import re

initial = 100
index = 1
imageName = '3.jpg'


# new Excel file making
def create_workBook(name):
    wb = openpyxl.Workbook()
    file = wb.active
    file.title = name
    file.append(['Number', 'UV Transmission', 'IR Transmission', 'VL Transmission'])
    return wb, file


# Tesseract-OCR path
def openTesseract():
    pytesseract.pytesseract.tesseract_cmd = pytesseract.pytesseract.tesseract_cmd = r"C:\Program " \
                                                                                    r"Files\Tesseract-OCR\tesseract" \
                                                                                    r".exe "


# Image open
def openImage(image):
    img = cv2.imread(image)
    # Resizing for scan
    img = cv2.resize(img, None, fx=1, fy=1)
    return img


#  threshold Method
def thresholdMethod(image, tn, ti):
    ret, r1 = cv2.threshold(image, ti + tn, 255, cv2.THRESH_BINARY)
    rz = cv2.cvtColor(r1, cv2.COLOR_BGR2GRAY)
    ret, rr = cv2.threshold(rz, 0, 255, cv2.THRESH_BINARY)
    return rr


#  extract Text From Image
def extractTextFromImage(image):
    text = pytesseract.image_to_string(image)
    text = text.replace(" ", "")
    text = text.replace(",", ".")
    return text


#  Read text put in a cell
def readText(text):
    return re.findall(r"\d+\.?\d*", text)


#  check cell length
def lenCheck(cell):
    return len(cell) == 3


#  check char in number list
def textCheck(text):
    testchar = 0
    for line in text.splitlines():
        b = re.findall(r'\d+', line)
        if len(b) != 0:
            if float(b[0]) > 100:
                testchar = 1
            else:
                if line.find("%") != -1:
                    for c in line:
                        if c.isalpha():
                            testchar = 1
    return testchar


# Setup
document, sheet = create_workBook("Testing")
openTesseract()
img = openImage(imageName)
i = 0
checker = 0

# loop for test the accurate number
while True:
    print(i)
    # extract the text from image
    txt = extractTextFromImage(thresholdMethod(img, i, initial))
    a = readText(txt)
    if lenCheck(a):
        checker = textCheck(txt)
        if checker == 0:
            # print it out for checking
            print(txt + "\n")
            print(i + initial)
            break
        else:
            i += 1
            checker = 0
    else:
        i += 1
    if (initial + i) >= 255:
        break

# print the recognized data
print(a)

# insert the index in Excel
a.insert(0, index)
sheet.append(a)

# show the image
cv2.imshow('Result0', img)
cv2.waitKey(0)
document.save('Testing.xlsx')
