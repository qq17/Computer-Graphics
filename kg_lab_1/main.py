import sys

from PySide2.QtWidgets import QMainWindow, QApplication

from MainWindow import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.draw_button.clicked.connect(self.draw)
        self.turn_button.clicked.connect(self.turn)

        self.show()

    def draw(self):
        x1 = self.x1_sb.value()
        y1 = self.y1_sb.value()
        x2 = self.x2_sb.value()
        y2 = self.y2_sb.value()
        x3 = self.x3_sb.value()
        y3 = self.y3_sb.value()

        x0 = self.x0_sb.value()
        y0 = self.y0_sb.value()

        self.plot_widget.plot(x1, y1, x2, y2, x3, y3, x0, y0)

    def turn(self):
        x1 = self.x1_sb.value()
        y1 = self.y1_sb.value()
        x2 = self.x2_sb.value()
        y2 = self.y2_sb.value()
        x3 = self.x3_sb.value()
        y3 = self.y3_sb.value()

        x0 = self.x0_sb.value()
        y0 = self.y0_sb.value()
        a = self.angle_sb.value()

        self.plot_widget.turn(x1, y1, x2, y2, x3, y3, x0, y0, a)

if __name__ == '__main__':
    app = QApplication([])
    p = MainWindow()
    p.show()

    sys.exit(app.exec_())