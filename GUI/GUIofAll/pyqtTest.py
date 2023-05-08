from PyQt6.QtWidgets import QApplication, QWidget
import sys
# pyuic6 -x Window.ui -o Window.py
app = QApplication(sys.argv)
window = QWidget()

window.show()
sys.exit(app.exec())




