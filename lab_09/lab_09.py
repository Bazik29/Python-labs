import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi


class MyWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        loadUi('lab_09.ui', self)
        
        self.expr.setText("\"Правда\" > \"Ложь\" or True != False")
        self.expr_left.setText("\"Правда\" > \"Ложь\"")
        self.expr_right.setText("True != False")
        res = str("Правда" > "Ложь" or True != False)
        res_left = str("Правда" > "Ложь")
        res_right = str(True != False)
        self.res.setText(res)
        self.res_left.setText(res_left)
        self.res_right.setText(res_right)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    mainWin = MyWindow()
    mainWin.show()

    sys.exit(app.exec_())
