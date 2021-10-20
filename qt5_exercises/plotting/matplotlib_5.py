import sys

from PyQt5 import QtCore, QtWidgets  # import PyQt5 before matplotlib

import matplotlib
import pandas as pd
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure


matplotlib.use("Qt5Agg")


class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super().__init__(fig)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Create the maptlotlib FigureCanvas object,
        # which defines a single set of axes as self.axes.
        sc = MplCanvas(self, width=5, height=4, dpi=100)

        # Create our pandas DataFrame with some simple
        # data and headers.
        df = pd.DataFrame(
            [[0, 10], [5, 15], [2, 20], [15, 25], [4, 10],], columns=["A", "B"]
        )

        # plot the pandas DataFrame, passing in the
        # matplotlib Canvas axes.
        df.plot(ax=sc.axes)

        self.setCentralWidget(sc)
        self.show()


app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
app.exec_()
