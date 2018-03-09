import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi


class MyWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        loadUi('lab_07.ui', self)
        
        self.btn_go.clicked.connect(self.count_spaces)

    def count_spaces(self):
        text = self.text.toPlainText()
        sp_list = []
        for i in range(len(text)):
            if text[i] == " ":
                sp_list.append(i)
        self.res.setText(", ".join(str(v) for v in sp_list))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    mainWin = MyWindow()
    mainWin.show()

    sys.exit(app.exec_())
