# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QPushButton

def function():
    print("This function has been called")
if __name__ == "__main__":
    app = QApplication(sys.argv)
    # ...
    button = QPushButton("FUNCTION CALL")
    button.clicked.connect(function)
    button.show()
    sys.exit(app.exec())
