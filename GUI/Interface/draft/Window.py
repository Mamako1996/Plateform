from PyQt6 import QtCore, QtGui, QtWidgets
import time
from DCMotorControl import MotorControl
from RMControl import ServoControl


class Ui_GUIofAll(object):

    def setupUi(self, InterfaceI):
        InterfaceI.setObjectName("GUIofAll")
        InterfaceI.resize(892, 613)
        InterfaceI.setStyleSheet("QWidget{\n"
                                 "background-color:rgb(0, 0, 0)\n"
                                 "}")
        self.label = QtWidgets.QLabel(InterfaceI)
        self.label.setGeometry(QtCore.QRect(60, 140, 171, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(InterfaceI)
        self.label_2.setGeometry(QtCore.QRect(60, 190, 171, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(InterfaceI)
        self.label_3.setGeometry(QtCore.QRect(60, 240, 171, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(InterfaceI)
        self.label_4.setGeometry(QtCore.QRect(60, 290, 171, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(InterfaceI)
        self.label_5.setGeometry(QtCore.QRect(60, 340, 171, 21))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(InterfaceI)
        self.label_6.setGeometry(QtCore.QRect(60, 390, 171, 21))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(InterfaceI)
        self.label_7.setGeometry(QtCore.QRect(490, 140, 171, 21))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(InterfaceI)
        self.label_8.setGeometry(QtCore.QRect(490, 190, 171, 21))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(InterfaceI)
        self.label_9.setGeometry(QtCore.QRect(490, 240, 171, 21))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(InterfaceI)
        self.label_10.setGeometry(QtCore.QRect(490, 290, 171, 21))
        font = QtGui.QFont()
        font.setKerning(True)
        self.label_10.setFont(font)
        self.label_10.setAutoFillBackground(False)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(InterfaceI)
        self.label_11.setGeometry(QtCore.QRect(490, 340, 171, 21))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(InterfaceI)
        self.label_12.setGeometry(QtCore.QRect(490, 390, 171, 21))
        self.label_12.setObjectName("label_12")
        self.lineEdit = QtWidgets.QLineEdit(InterfaceI)
        self.lineEdit.setGeometry(QtCore.QRect(260, 140, 101, 21))
        self.lineEdit.setStyleSheet("QWidget{\n"
                                    "background-color:rgb(255, 255, 255)\n"
                                    "}")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(InterfaceI)
        self.lineEdit_2.setGeometry(QtCore.QRect(260, 190, 101, 21))
        self.lineEdit_2.setStyleSheet("QWidget{\n"
                                      "background-color:rgb(255, 255, 255)\n"
                                      "}")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(InterfaceI)
        self.lineEdit_3.setGeometry(QtCore.QRect(260, 240, 101, 21))
        self.lineEdit_3.setStyleSheet("QWidget{\n"
                                      "background-color:rgb(255, 255, 255)\n"
                                      "}")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(InterfaceI)
        self.lineEdit_4.setGeometry(QtCore.QRect(260, 290, 101, 21))
        self.lineEdit_4.setStyleSheet("QWidget{\n"
                                      "background-color:rgb(255, 255, 255)\n"
                                      "}")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(InterfaceI)
        self.lineEdit_5.setGeometry(QtCore.QRect(260, 340, 101, 21))
        self.lineEdit_5.setStyleSheet("QWidget{\n"
                                      "background-color:rgb(255, 255, 255)\n"
                                      "}")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(InterfaceI)
        self.lineEdit_6.setGeometry(QtCore.QRect(260, 390, 101, 21))
        self.lineEdit_6.setStyleSheet("QWidget{\n"
                                      "background-color:rgb(255, 255, 255)\n"
                                      "}")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(InterfaceI)
        self.lineEdit_7.setGeometry(QtCore.QRect(690, 140, 101, 21))
        self.lineEdit_7.setStyleSheet("QWidget{\n"
                                      "background-color:rgb(255, 255, 255)\n"
                                      "}")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(InterfaceI)
        self.lineEdit_8.setGeometry(QtCore.QRect(690, 190, 101, 21))
        self.lineEdit_8.setStyleSheet("QWidget{\n"
                                      "background-color:rgb(255, 255, 255)\n"
                                      "}")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(InterfaceI)
        self.lineEdit_9.setGeometry(QtCore.QRect(690, 240, 101, 21))
        self.lineEdit_9.setStyleSheet("QWidget{\n"
                                      "background-color:rgb(255, 255, 255)\n"
                                      "}")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_10 = QtWidgets.QLineEdit(InterfaceI)
        self.lineEdit_10.setGeometry(QtCore.QRect(690, 290, 101, 21))
        self.lineEdit_10.setStyleSheet("QWidget{\n"
                                       "background-color:rgb(255, 255, 255)\n"
                                       "}")
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_11 = QtWidgets.QLineEdit(InterfaceI)
        self.lineEdit_11.setGeometry(QtCore.QRect(690, 340, 101, 21))
        self.lineEdit_11.setStyleSheet("QWidget{\n"
                                       "background-color:rgb(255, 255, 255)\n"
                                       "}")
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.lineEdit_12 = QtWidgets.QLineEdit(InterfaceI)
        self.lineEdit_12.setGeometry(QtCore.QRect(690, 390, 101, 21))
        self.lineEdit_12.setStyleSheet("QWidget{\n"
                                       "background-color:rgb(255, 255, 255)\n"
                                       "}")
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.label_13 = QtWidgets.QLabel(InterfaceI)
        self.label_13.setGeometry(QtCore.QRect(50, 40, 811, 51))
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(InterfaceI)
        self.label_14.setGeometry(QtCore.QRect(370, 140, 41, 21))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(InterfaceI)
        self.label_15.setGeometry(QtCore.QRect(370, 190, 41, 21))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(InterfaceI)
        self.label_16.setGeometry(QtCore.QRect(370, 240, 41, 21))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(InterfaceI)
        self.label_17.setGeometry(QtCore.QRect(370, 290, 41, 21))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(InterfaceI)
        self.label_18.setGeometry(QtCore.QRect(370, 340, 41, 21))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(InterfaceI)
        self.label_19.setGeometry(QtCore.QRect(370, 390, 41, 21))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(InterfaceI)
        self.label_20.setGeometry(QtCore.QRect(800, 140, 41, 21))
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(InterfaceI)
        self.label_21.setGeometry(QtCore.QRect(800, 190, 41, 21))
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(InterfaceI)
        self.label_22.setGeometry(QtCore.QRect(800, 240, 41, 21))
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(InterfaceI)
        self.label_23.setGeometry(QtCore.QRect(800, 290, 41, 21))
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(InterfaceI)
        self.label_24.setGeometry(QtCore.QRect(800, 340, 41, 21))
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(InterfaceI)
        self.label_25.setGeometry(QtCore.QRect(800, 390, 41, 21))
        self.label_25.setObjectName("label_25")
        self.pushButton = QtWidgets.QPushButton(InterfaceI)
        self.pushButton.setGeometry(QtCore.QRect(710, 440, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("QWidget{\n"
                                      "background-color:rgb(255, 255, 255)\n"
                                      "}\n"
                                      "QLabel{\n"
                                      "color:rgb(255, 255, 255)\n"
                                      "}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.clicked_btn)
        self.label_26 = QtWidgets.QLabel(InterfaceI)
        self.label_26.setGeometry(QtCore.QRect(60, 440, 231, 21))
        self.label_26.setObjectName("label_26")
        self.lineEdit_13 = QtWidgets.QLineEdit(InterfaceI)
        self.lineEdit_13.setGeometry(QtCore.QRect(320, 440, 101, 21))
        self.lineEdit_13.setStyleSheet("QWidget{\n"
                                       "background-color:rgb(255, 255, 255)\n"
                                       "}")
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.label_27 = QtWidgets.QLabel(InterfaceI)
        self.label_27.setGeometry(QtCore.QRect(430, 440, 41, 21))
        self.label_27.setObjectName("label_27")

        self.retranslateUi(InterfaceI)
        QtCore.QMetaObject.connectSlotsByName(InterfaceI)

    def clicked_btn(self):
        t = ""
        if self.lineEdit_13.text() != "":
            t = str(int(self.lineEdit_13.text()) * 60 * 60 * 1000)
        motorGroup1 = MotorControl(self.emptyCheck(t), self.emptyCheck(self.lineEdit.text()),
                                   self.emptyCheck(self.lineEdit_2.text()),
                                   self.emptyCheck(self.lineEdit_3.text()), self.emptyCheck(self.lineEdit_4.text()),
                                   "MotorGroup1")
        motorGroup1.startMotor()
        motorGroup2 = MotorControl(self.emptyCheck(t), self.emptyCheck(self.lineEdit_5.text()),
                                   self.emptyCheck(self.lineEdit_6.text()),
                                   self.emptyCheck(self.lineEdit_7.text()), self.emptyCheck(self.lineEdit_8.text()),
                                   "MotorGroup2")
        motorGroup2.startMotor()
        motorGroup3 = MotorControl(self.emptyCheck(t), self.emptyCheck(self.lineEdit_9.text()),
                                   self.emptyCheck(self.lineEdit_10.text()),
                                   self.emptyCheck(self.lineEdit_11.text()), self.emptyCheck(self.lineEdit_12.text()),
                                   "MotorGroup3")
        motorGroup3.startMotor()


        # ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        # Stirring Module:
        # Start Rotating
        motorGroup1.openFile()
        motorGroup2.openFile()
        motorGroup3.openFile()

        # time.sleep(int(self.lineEdit_13.text()) * 60 * 60)

        # # Stop Rotating
        motorGroup1.stopRoating()
        motorGroup2.stopRoating()
        motorGroup3.stopRoating()

        # ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        # Coating Module:

        rmb = ServoControl(True, False, "Bottom", "Glasses")
        rmb.startRM()
        time.sleep(3)
        rmb.stopMove()
        # ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        # Collecting Module:
        # Robotic Arms:
        rmg = ServoControl(False, True, "Bottom", "Glasses")
        rmg.startRM()
        time.sleep(3)
        rmg.stopMove()


    def retranslateUi(self, InterfaceI):
        _translate = QtCore.QCoreApplication.translate
        InterfaceI.setWindowTitle(_translate("GUIofAll", "GUIofAll"))
        self.label.setText(_translate("GUIofAll",
                                      "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600; color:#ffffff; vertical-align:super;\">Strring Motor #1</span></p></body></html>"))
        self.label_2.setText(_translate("GUIofAll",
                                        "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600; color:#ffffff; vertical-align:super;\">Strring Motor #2</span></p></body></html>"))
        self.label_3.setText(_translate("GUIofAll",
                                        "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600; color:#ffffff; vertical-align:super;\">Strring Motor #3</span></p><p><br/></p></body></html>"))
        self.label_4.setText(_translate("GUIofAll",
                                        "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600; color:#ffffff; vertical-align:super;\">Strring Motor #4</span></p></body></html>"))
        self.label_5.setText(_translate("GUIofAll",
                                        "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600; color:#ffffff; vertical-align:super;\">Strring Motor #5</span></p></body></html>"))
        self.label_6.setText(_translate("GUIofAll",
                                        "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600; color:#ffffff; vertical-align:super;\">Strring Motor #6</span></p></body></html>"))
        self.label_7.setText(_translate("GUIofAll",
                                        "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600; color:#ffffff; vertical-align:super;\">Strring Motor #7</span></p></body></html>"))
        self.label_8.setText(_translate("GUIofAll",
                                        "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600; color:#ffffff; vertical-align:super;\">Strring Motor #8</span></p></body></html>"))
        self.label_9.setText(_translate("GUIofAll",
                                        "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600; color:#ffffff; vertical-align:super;\">Strring Motor #9</span></p></body></html>"))
        self.label_10.setText(_translate("GUIofAll",
                                         "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600; color:#ffffff; vertical-align:super;\">Strring Motor #10</span></p></body></html>"))
        self.label_11.setText(_translate("GUIofAll",
                                         "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600; color:#ffffff; vertical-align:super;\">Strring Motor #11</span></p></body></html>"))
        self.label_12.setText(_translate("GUIofAll",
                                         "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600; color:#ffffff; vertical-align:super;\">Strring Motor #12</span></p></body></html>"))
        self.label_13.setText(_translate("GUIofAll",
                                         "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-weight:600; color:#ffffff;\">DC Motors Speed Control Interface</span></p></body></html>"))
        self.label_14.setText(_translate("GUIofAll",
                                         "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">rpm</span></p></body></html>"))
        self.label_15.setText(_translate("GUIofAll",
                                         "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">rpm</span></p></body></html>"))
        self.label_16.setText(_translate("GUIofAll",
                                         "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">rpm</span></p></body></html>"))
        self.label_17.setText(_translate("GUIofAll",
                                         "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">rpm</span></p></body></html>"))
        self.label_18.setText(_translate("GUIofAll",
                                         "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">rpm</span></p></body></html>"))
        self.label_19.setText(_translate("GUIofAll",
                                         "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">rpm</span></p></body></html>"))
        self.label_20.setText(_translate("GUIofAll",
                                         "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">rpm</span></p></body></html>"))
        self.label_21.setText(_translate("GUIofAll",
                                         "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">rpm</span></p></body></html>"))
        self.label_22.setText(_translate("GUIofAll",
                                         "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">rpm</span></p></body></html>"))
        self.label_23.setText(_translate("GUIofAll",
                                         "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">rpm</span></p></body></html>"))
        self.label_24.setText(_translate("GUIofAll",
                                         "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">rpm</span></p></body></html>"))
        self.label_25.setText(_translate("GUIofAll",
                                         "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">rpm</span></p></body></html>"))
        self.pushButton.setText(_translate("GUIofAll", "Confirm"))
        self.label_26.setText(_translate("GUIofAll",
                                         "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600; color:#ffffff; vertical-align:super;\">The Longest Time Spend</span></p></body></html>"))
        self.label_27.setText(_translate("GUIofAll",
                                         "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">hours</span></p></body></html>"))

    def emptyCheck(self, textSpeed):
        text = textSpeed
        if textSpeed == "":
            text = "0"
        return text


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    GUIofAll = QtWidgets.QWidget()
    ui = Ui_GUIofAll()
    ui.setupUi(GUIofAll)
    GUIofAll.show()
    sys.exit(app.exec())
