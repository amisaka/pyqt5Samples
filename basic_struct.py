# Import necessary modules
import sys
from PyQt5.QtWidgets import QApplication, QWidget

class ExampleClass(QWidget):

    def __init__(self):  # Create default constructor
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Initialize the window and display its contents to the screen"""
        self.setGeometry(100, 100, 500, 400)
        self.setWindowTitle('Empty Window in PyQt')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ExampleClass()
    sys.exit(app.exec_())
