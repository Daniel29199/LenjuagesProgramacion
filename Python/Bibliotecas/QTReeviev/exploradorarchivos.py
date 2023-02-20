import sys
from tkinter import dialog

from PyQt5.QtWidgets import QApplication,QFileSystemModel, QTreeView, QWidget, QVBoxLayout

class ExploradorArchivos(QWidget):
    def __init__(self):
        super().__init__()

        self.inicializarGui()

        def inicializarGui(self):
            self.setWindodwTitle('Explorador de archivos')
            self.setFixedSize(600,600)

            self.show()
            
             
def main():
    app=QApplication(sys.argv)
    dialogo= ExploradorArchivos()

    sys.exit(app.exec_())

if __name__== '__main__':
    main()