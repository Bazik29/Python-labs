import sys
import time
import math
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi


def summ(n):
    # return (-1)**n/(2.*n + 1)
    return (-1)**(n % 2) / (2. * n + 1)


class MyWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        loadUi('lab_03.ui', self)
        self.btn_go.clicked.connect(self.calcPi)

    def toLog(self, log):
        self.log_field.insertPlainText(log)
        self.log_field.insertPlainText("\n")

    def calcPi(self):
        znak = int(self.n_znak.text())
        n, s, s1, s2 = 0, 0, 0, 0
        eps = 10**(-znak)
        diff = 0
        self.toLog("EPS = {eps:.{znak}f}".format(**vars()))
        t = time.time()
        self.toLog("Время старта: {}".format(time.ctime(t)))

        while (True):
            s1 = summ(n)
            s2 = summ(n + 1)
            s += s1
            n += 1
            diff = abs(s2 - s1)
            if diff <= eps:
                break
        pi = 4 * s
        self.toLog("Время завершения: {}".format(time.ctime(time.time())))
        self.toLog("Время выволнения: {} сек".format(time.time() - t))
        self.toLog("Сосчитанное число Пи: {pi:.{znak}f}\n".format(**vars()))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    mainWin = MyWindow()
    mainWin.show()

    sys.exit(app.exec_())
