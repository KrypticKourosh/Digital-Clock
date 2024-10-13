import sys

from PyQt5.QtCore import QTimer, QTime
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QFontDatabase, QIcon


class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel(self) #but why pass self? aren't we going to use layout?
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Digital Clock")
        self.setWindowIcon(QIcon("images/digital-clock.png"))
        self.setGeometry(600, 400, 300, 100)

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setStyleSheet("""
        font-size:150px;
        color:hsl(130, 86%, 57%);
        """)
        self.setStyleSheet("background-color:black;")

        self.update_time() #it shows the persian numbers
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000) #it updates every 1000ms (1s)

        font_id = QFontDatabase.addApplicationFont("Fonts/DS-DIGIT.TTF")
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        my_font = QFont(font_family, 150)
        self.time_label.setFont(my_font)

    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        self.time_label.setText(current_time)


