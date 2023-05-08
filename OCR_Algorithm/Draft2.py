import cv2
import pytesseract
import openpyxl
import re
import time

# Set an initial threshold value which depends on
# environmental variable (light) it only affects
# the running time of the program
initial = 150


# New Excel file making
# @param name - the file name (str)
# @return wb - the work book (xlsx file)
# @return file - the sheet in work book (xlsx file)
def create_workBook(name):
    wb = openpyxl.Workbook()
    file = wb.active
    file.title = name
    file.append(['Number', 'UV Transmission', 'IR Transmission', 'VL Transmission'])
    return wb, file


# Tesseract-OCR path locating
def openTesseract():
    pytesseract.pytesseract.tesseract_cmd = pytesseract.pytesseract.tesseract_cmd = r"C:\Program " \
                                                                                    r"Files\Tesseract-OCR\tesseract" \
                                                                                    r".exe "


# Image open
# @param image - the file name (str)
# @return mg - revised image (jpg, png...)
def openImage(image):
    mg = cv2.imread(image)
    # Resizing for scan
    mg = cv2.resize(mg, None, fx=1.1, fy=1.1)
    mg = mg[0:750, 200:460]
    return mg


# Image threshold dividing Method
# @param image - the revised image (jpg, png...)
# @param ti - initial threshold value (int)
# @param tn - appended increasing threshold value (int)
# @return rr - final version of the image revised by this method (jpg, png...)
def thresholdMethod(image, tn, ti):
    rt, r1 = cv2.threshold(image, ti + tn, 255, cv2.THRESH_BINARY)
    # rt - frame of the image
    # r1 - the revised image by step 1
    rz = cv2.cvtColor(r1, cv2.COLOR_BGR2GRAY)
    # rz - graying image in step 1 which is the step 2
    rt, rr = cv2.threshold(rz, 0, 255, cv2.THRESH_BINARY)
    # rt - frame of the image
    # rr - the revised image - B & W method
    return rr


# Extract Text From Image
# @param image - the revised image (jpg, png...)
# @return text - Text From Image (str)
def extractTextFromImage(image):
    text = pytesseract.image_to_string(image)
    text = text.replace(" ", "")  # space remove
    text = text.replace(",", ".")  # comma replace by period
    return text


# Read text put in a cell
# @param text - text from image (str)
# @return - numerical text only (cell)
def readText(text):
    return re.findall(r"\d+\.?\d*", text)  # \.?


# Check cell length
# @param cell - numerical text only (cell)
# @return - whether the length of the cell is 3 or not (boolean)
def lenCheck(cell):
    return len(cell) == 3


#  check char in number list
# @param text - text from Image (str)
# @param subtext - a revised line in text
# @return - whether the cell include expected number or not (boolean)
def textCheck(text, subtext):
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
                    if (line.find(".") == -1) & (line.find("100") == -1):
                        testchar = 1
                else:
                    if subtext.find("100") == -1:
                        testchar = 1
        else:
            if line.find("%") != -1:
                testchar = 1
    return testchar


# open camera
cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)
signal = cap.isOpened()
index = 1
document, sheet = create_workBook("Testing")

# open Tesseract
openTesseract()
temp = ''

# Main Process - utilize the increasing threshold value to
# find a suitable number in current environmental condition
# if there are some reading errors, it will skip to the next
# threshold value until it found by the program
while signal:
    ret, frame = cap.read()
    cv2.imshow("Current", frame)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('s'):
        cv2.imwrite("C:/Users/umbmz/PycharmProjects/project/HW/Section_I/" + "Test" + str(index) + ".jpg", frame)
        print("save" + str(index) + ".jpg successfully!")

        imageName = "Test" + str(index) + ".jpg"
        print(imageName)
        img = openImage(imageName)
        i = 0
        checker = 0

        # loop for test the accurate number
        while True:
            start = time.perf_counter()  # time counter
            print(i)
            # extract the text from image
            txt = extractTextFromImage(thresholdMethod(img, i, initial))
            a = readText(txt)
            if lenCheck(a):
                for n in range(3):
                    # "100" is a special case which do not have period ".",
                    # and its position is right-skewing. Therefore,
                    # a special case dealing method is needed

                    if a[n].find("100") != -1:  # if it finds "100" in line
                        a[n] = '100'
                        # change whole line to "100" - remove interferences
                        # such as %&^100, 10009, etc.
                    if len(a[n]) > 4:
                        # remove interferences such as 87.07
                        # since the float should be 0.0 form
                        a[n] = a[n][0:2]  # change 0.00 to 0.0
                    a[n] = str(round(float(a[n]), 1))
                    temp = a[n]
                checker = textCheck(txt, temp)
                if checker == 0:  # it will print the expected number
                    # print it out for checking
                    print(txt + "\n")
                    print(i + initial)
                    end = time.perf_counter()
                    print("time consuming : {:.2f}s".format(end - start))
                    break
                else:
                    i += 1
                    checker = 0
            else:
                i += 1
            if (initial + i) >= 255:  # force break
                break

        # print the recognized data
        print(a)

        # insert the1 index in Excel
        a.insert(0, index)
        sheet.append(a)

        # document saving
        document.save('Testing.xlsx')
        index += 1
        cv2.waitKey(0)
    elif k == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

