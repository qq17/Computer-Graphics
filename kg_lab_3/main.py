import sys

import numpy as np
from PySide2.QtCore import *
from PySide2.QtWidgets import *

from MainWindow import Ui_MainWindow

class ListItem(QWidget):
    def __init__(self, i):
        super(ListItem, self).__init__()

        self.row = QHBoxLayout()
        self.x_sb = QSpinBox()
        self.x_sb.setMinimum(-100)
        self.x_sb.setMaximum(100)

        self.y_sb = QSpinBox()
        self.y_sb.setMinimum(-100)
        self.y_sb.setMaximum(100)

        self.z_sb = QSpinBox()
        self.z_sb.setMinimum(-100)
        self.z_sb.setMaximum(100)

        self.row.addWidget(QLabel(str(i)+': '))
        self.row.addWidget(QLabel('x:'))
        self.row.addWidget(self.x_sb)
        self.row.addWidget(QLabel('y:'))
        self.row.addWidget(self.y_sb)
        self.row.addWidget(QLabel('z:'))
        self.row.addWidget(self.z_sb)

        self.setLayout(self.row)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        x_sample = [-45, -45, -45, -45, -15, -15, -15, -15, 15, 15, 15, 15, 45, 45, 45, 45]
        y_sample = [0, 15, 15, 0, 15, 15, 15, 15, 15, 15, 15, 15, 0, 15, 15, 0]
        z_sample = [45, 15, -15, -45, 45, 15, -15, -45, 45, 15, -15, -45, 45, 15, -15, -45]

        for i in range(16):
            item = QListWidgetItem(self.points_list_widget)
            self.points_list_widget.addItem(item)
            row = ListItem(i+1)
            row.x_sb.setValue(x_sample[i])
            row.y_sb.setValue(y_sample[i])
            row.z_sb.setValue(z_sample[i])
            item.setSizeHint(row.minimumSizeHint())
            self.points_list_widget.setItemWidget(item, row)

        self.draw_button.clicked.connect(self.draw)
        self.turn_x_button.clicked.connect(self.turn_x)
        self.turn_y_button.clicked.connect(self.turn_y)

        self.show()

    def draw(self):
        P = np.array([np.array([self.points_list_widget.itemWidget(self.points_list_widget.item(i)).x_sb.value(),
                                self.points_list_widget.itemWidget(self.points_list_widget.item(i)).y_sb.value(),
                                self.points_list_widget.itemWidget(self.points_list_widget.item(i)).z_sb.value()]) for i in range(self.points_list_widget.count())])
        self.plot_widget.Pi = P
        self.plot_widget.plot()

    def turn_x(self):
        P = np.array([np.array([self.points_list_widget.itemWidget(self.points_list_widget.item(i)).x_sb.value(),
                                self.points_list_widget.itemWidget(self.points_list_widget.item(i)).y_sb.value(),
                                self.points_list_widget.itemWidget(self.points_list_widget.item(i)).z_sb.value()]) for i in range(self.points_list_widget.count())])
        self.plot_widget.Pi = P
        self.plot_widget.turn_x(self.angle_sb.value())

    def turn_y(self):
        P = np.array([np.array([self.points_list_widget.itemWidget(self.points_list_widget.item(i)).x_sb.value(),
                                self.points_list_widget.itemWidget(self.points_list_widget.item(i)).y_sb.value(),
                                self.points_list_widget.itemWidget(self.points_list_widget.item(i)).z_sb.value()]) for i in range(self.points_list_widget.count())])
        self.plot_widget.Pi = P
        self.plot_widget.turn_y(self.angle_sb.value())



if __name__ == '__main__':
    app = QApplication([])
    p = MainWindow()
    p.show()

    sys.exit(app.exec_())