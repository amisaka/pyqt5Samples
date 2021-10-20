import sys

from PySide2.QtCore import QSize, Qt
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__() # we must always call the __init__ of the
                           # super() class
        self.setWindowTitle("My App")
        button = QPushButton("Press Me!")
        # Set the central widget of the Window.
        self.setCentralWidget(button) # Use .setCentralWidget to place
                                      # a widget in the QMainWindow

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
