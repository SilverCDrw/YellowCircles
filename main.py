import sys
from random import randint

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5 import uic


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.trig = False
        uic.loadUi("UI.ui", self)
        self.pushButton.clicked.connect(self.on_click)

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        if self.trig:
            self.drawCircles(qp)
            self.drawCircles(qp)
            self.drawCircles(qp)
            self.drawCircles(qp)
            self.drawCircles(qp)
            self.drawCircles(qp)
            self.trig = False
        qp.end()

    def drawCircles(self, qp):
        qp.setBrush(QColor('#ffcc00'))
        x = randint(1, self.width())
        y = randint(1, self.height())
        d = randint(10, 200)
        qp.drawEllipse(x - d // 2, y - d // 2, d, d)

    def on_click(self, btn):
        self.trig =  True
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Widget()
    ex.show()
    sys.exit(app.exec_())
