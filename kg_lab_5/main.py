import sys

import numpy as np
from PySide2.QtCore import *
from PySide2.QtWidgets import *

from MainWindow import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.draw_button.clicked.connect(self.draw)
        self.del_invis_button.clicked.connect(self.del_invis)

        self.show()

    def draw(self):
        P = np.array([np.array([self.a_x_sb.value(), self.a_y_sb.value(), self.a_z_sb.value()]),
                      np.array([self.b_x_sb.value(), self.b_y_sb.value(), self.b_z_sb.value()]),
                      np.array([self.c_x_sb.value(), self.c_y_sb.value(), self.c_z_sb.value()]),
                      np.array([self.a1_x_sb.value(), self.a1_y_sb.value(), self.a1_z_sb.value()])])
        self.plot_widget.plot(P)

    def del_invis(self):
        P = np.array([np.array([self.a_x_sb.value(), self.a_y_sb.value(), self.a_z_sb.value()]),
                      np.array([self.b_x_sb.value(), self.b_y_sb.value(), self.b_z_sb.value()]),
                      np.array([self.c_x_sb.value(), self.c_y_sb.value(), self.c_z_sb.value()]),
                      np.array([self.a1_x_sb.value(), self.a1_y_sb.value(), self.a1_z_sb.value()])])
        self.plot_widget.plot_del_invis(P)



if __name__ == '__main__':
    app = QApplication([])
    p = MainWindow()
    p.show()

    sys.exit(app.exec_())