import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi


class MyWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        loadUi('lab_04.ui', self)
        self.a = self.b = self.c = list()

        self.btn_gen.clicked.connect(self.generate)
        self.btn_go.clicked.connect(self.calc)

    def generate(self):
        n = int(self.line_n.text())
        self.a = np.random.uniform(1, 10, n)
        self.b = np.random.uniform(1, 10, n)
        self.list_a.setText(", ".join(str(v) for v in self.a))
        self.list_b.setText(", ".join(str(v) for v in self.b))

    def calc(self):
        self.c = self.a * self.b
        self.list_c.setText(", ".join(str(v) for v in self.c))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    mainWin = MyWindow()
    mainWin.show()

    sys.exit(app.exec_())
