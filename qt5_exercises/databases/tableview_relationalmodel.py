import sys

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtSql import QSqlDatabase, QSqlRelation, QSqlRelationalTableModel
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableView

db = QSqlDatabase("QSQLITE")
db.setDatabaseName("chinook.sqlite")
db.open()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.table = QTableView()

        self.model = QSqlRelationalTableModel(db=db)

        self.table.setModel(self.model)

        # tag::setRelation[]
        self.model.setTable("Track")
        self.model.setRelation(2, QSqlRelation("Album", "AlbumId", "Title"))
        self.model.setRelation(3, QSqlRelation("MediaType", "MediaTypeId", "Name"))
        self.model.setRelation(4, QSqlRelation("Genre", "GenreId", "Name"))
        self.model.select()
        # end::setRelation[]

        self.setMinimumSize(QSize(1024, 600))
        self.setCentralWidget(self.table)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
