from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont # проверка типов вводимых значений
from PyQt5.QtWidgets import (
       QApplication, QWidget,
       QHBoxLayout, QVBoxLayout, QGridLayout,
       QGroupBox, QRadioButton,
       QPushButton, QLabel, QListWidget, QLineEdit)
      
from instr import *


class FinalWin(QWidget):
    def __init__(self, exp):
        super().__init__()
        self.exp = exp
        self.results()
        self.initUI()
        self.set_appear()
        self.show()

    def results(self):
        self.index=(4*(int(self.exp.t1)+int(self.exp.t2)+int(self.exp.t3))-200)/10
        if int(self.exp.age) >= 15:
            if self.index >= 15:
                return txt_res1
            elif self.index >= 11 and self.index <= 14.9:
                return txt_res2
            elif self.index >= 6 and self.index <= 10.9:
                return txt_res3
            elif self.index >= 0.5 and self.index <= 5.9:
                return txt_res4
            else:
                return txt_res5
        if self.exp.age == 13 or 14:
            if self.index == 16.5:
                return txt_res1
            elif self.index >= 12.5 and self.index <= 16.4:
                return txt_res2
            elif self.index >= 7.5 and self.index <= 12.4:
                return txt_res3
            elif self.index >= 2 and self.index <= 7.4:
                return txt_res4
            else:
                return txt_res5
        if self.exp.age == 11 or 12:
            if self.index >= 18:
                return txt_res1
            elif self.index >= 14 and self.index <= 17.9:
                return txt_res2
            elif self.index >= 9 and self.index <= 13.9:
                return txt_res3
            elif self.index >= 3.5 and self.index <= 8.9:
                return txt_res4
            else:
                return txt_res5
        if self.exp.age == 9 or 10:
            if self.index >= 19.5:
                return txt_res1
            elif self.index >= 15.5 and self.index <= 19.4:
                return txt_res2
            elif self.index >= 10.5 and self.index <= 15.4:
                return txt_res3
            elif self.index >= 5 and self.index <= 10.4:
                return txt_res4
            else:
                return txt_res5
        if self.exp.age == 7 or 8:
            if self.index >= 21:
                return txt_res1
            elif self.index >= 17 and self.index <= 20.9:
                return txt_res2
            elif self.index >= 12 and self.index <= 16.9:
                return txt_res3
            elif self.index >= 6.5 and self.index <= 11.9:
                return txt_res4
            else:
                return txt_res5

    def initUI(self):
        self.work_text = QLabel(txt_workheart + self.results())
        self.index_text = QLabel(txt_index + str(self.index))
        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.index_text, alignment = Qt.AlignCenter)
        self.layout_line.addWidget(self.work_text, alignment = Qt.AlignCenter)        
        self.setLayout(self.layout_line)


    def set_appear(self):
        self.setWindowTitle(txt_finalwin)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
