import datetime
import time
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi


class MyWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        loadUi('lab_08.ui', self)

        self.btn_time.clicked.connect(self.insert_time)
        self.btn_go.clicked.connect(self.calc_time)

    def insert_time(self):
        self.time_line.setText(datetime.datetime.now().strftime("%X"))

    def calc_time(self):
        time_str = self.time_line.text()
        if (time_str == ""):
            time_str = datetime.datetime.now().strftime("%X")
            self.time_line.setText(time_str)

        now_time = datetime.datetime.strptime(time_str, "%X")
        end_day = now_time.replace(hour=23, minute=59, second=59)
        delta = end_day - now_time
        seconds = delta.seconds + 1
        self.res.setText(str(seconds))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    mainWin = MyWindow()
    mainWin.show()

    sys.exit(app.exec_())
