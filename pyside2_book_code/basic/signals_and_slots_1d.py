import sys

from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton


# tag::MainWindow[]
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.button_is_checked = True

        self.setWindowTitle("My App")

        self.button = QPushButton("Press Me!")  # <1> Keep a reference to the button
        self.button.setCheckable(True)
        self.button.released.connect(self.the_button_was_released)  # <2> released signal fires
        self.button.setChecked(self.button_is_checked)

        # Set the central widget of the Window.
        self.setCentralWidget(self.button)

    def the_button_was_released(self):
        self.button_is_checked = self.button.isChecked()  # <3> returns the check state of the button

        print(self.button_is_checked)


# end::MainWindow[]

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
