import sys
import math
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi


class MyWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        loadUi('lab_06.ui', self)

        self.btn_go.clicked.connect(self.calc)

    def func(self, a, b, c):
        return math.log((a + math.sin(b)) / math.cos(2 * a), 10) + math.pow(5 + math.pow(2 + c, 1. / 2), 1. / 4)

    def calc(self):
        a = 0.785
        b = 1.5708
        c = 3.777
        y = self.func(a, b, c)
        self.res.setText(str(y))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    mainWin = MyWindow()
    mainWin.show()

    sys.exit(app.exec_())
