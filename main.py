from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow , QPushButton, QLabel, QMenu, QVBoxLayout, QHBoxLayout, QLineEdit
from sys import argv
from mod4 import *
from mod5 import *

class MainWindow(QMainWindow):

    def sel_module(self,name,displayname,btn):
        self.selectedModule = name
        btn.setText(displayname)

    def __init__(self):
        super().__init__()
        self.resize(300,100)
        self.selectedModule = None
        self.setWindowTitle("Ільчук Іван КМ-42")
        self.dropd = QPushButton("Оберіть модуль",self)
        self.dropd.setGeometry(20,10,260,40)
        module_menu = QMenu(self)

        module_menu.addAction("Модуль 4").triggered.connect(lambda: self.sel_module("mod4","Модуль 4",self.dropd))
        module_menu.addAction("Модуль 5").triggered.connect(lambda: self.sel_module("mod5","Модуль 5",self.dropd))
        
        self.dropd.setMenu(module_menu)

        self.btn_conf = QPushButton("Запустити\nмодуль",self)
        self.btn_conf.setGeometry(20,50,260,40)

        
        self.btn_conf.clicked.connect(self.show_new_window)

    def show_new_window(self,checked):
        if self.selectedModule == "mod5":
            self.mod_win = Module5Window()
            self.mod_win.show()
        elif self.selectedModule == "mod4":
            self.mod_win = Module4Window()
            self.mod_win.show()
        
app = QApplication(argv)
window = MainWindow()
window.show()
app.exec()