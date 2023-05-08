from PyQt6.QtWidgets import QApplication, QWidget, QSpinBox, QHBoxLayout, QLineEdit, QPushButton, QLabel

import sys
from PyQt6.QtGui import QIcon


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("System Control")
        self.setWindowIcon(QIcon("qt.png"))
        self.setGeometry(500, 300, 500, 400)

        self.create_widgets()
        self.create_spin()

    def create_widgets(self):
        btn = QPushButton("Confirm", self)
        btn.move(200, 0)
        self.label = QLabel("My Label", self)
        self.label.setStyleSheet("color:green")
        btn.clicked.connect(self.clicked_btn)

    def create_spin(self):
        hbox = QHBoxLayout()

        label = QLabel("Laptop Price:")
        self.lineedit = QLineEdit()
        self.spinbox = QSpinBox()
        self.spinbox.valueChanged.connect(self.spin_selected)
        self.result = QLineEdit()

        hbox.addWidget(label)
        hbox.addWidget(self.lineedit)
        hbox.addWidget(self.spinbox)
        hbox.addWidget(self.result)

        self.setLayout(hbox)

    def spin_selected(self):
        if self.lineedit.text() != 0:
            price = int(self.lineedit.text())
            totalPrice = self.spinbox.value() * price
            self.result.setText(str(totalPrice))

    def clicked_btn(self):
        self.label.setText("T")
        self.label.setStyleSheet('background-color:red')


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
