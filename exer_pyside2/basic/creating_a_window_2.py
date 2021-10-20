from PySide2.QtWidgets import QApplication, QPushButton

app = QApplication([])
# Create a Qt widget, which will be our window.
window = QPushButton('Push Me')
window.show() # IMPORTANT!!!!! Windows are hidden by default.

# Start the event loop.
app.exec_()
