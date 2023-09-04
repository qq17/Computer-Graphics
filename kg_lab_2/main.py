import sys

import numpy as np
from PySide2.QtCore import *
from PySide2.QtWidgets import *

from MainWindow import Ui_MainWindow

class ListItem(QWidget):
    def __init__(self):
        super(ListItem, self).__init__()

        self.row = QHBoxLayout()
        self.x_spin_box = QSpinBox()
        self.x_spin_box.setMinimum(-100)
        self.x_spin_box.setMaximum(100)

        self.y_spin_box = QSpinBox()
        self.y_spin_box.setMinimum(-100)
        self.y_spin_box.setMaximum(100)

        self.row.addWidget(QLabel('x:'))
        self.row.addWidget(self.x_spin_box)
        self.row.addWidget(QLabel('y:'))
        self.row.addWidget(self.y_spin_box)

        self.setLayout(self.row)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        for i in range(5):
            self.add_point()

        self.delete_point_button.setDisabled(True)

        self.add_point_button.clicked.connect(self.add_point)
        self.delete_point_button.clicked.connect(self.delete_point)
        self.draw_button.clicked.connect(self.draw)

        self.show()

    def add_point(self):
        item = QListWidgetItem(self.points_list_widget)
        self.points_list_widget.addItem(item)
        row = ListItem()
        item.setSizeHint(row.minimumSizeHint())
        self.points_list_widget.setItemWidget(item, row)
        self.delete_point_button.setDisabled(False)

    def delete_point(self):
        self.points_list_widget.takeItem(self.points_list_widget.currentRow())
        if (self.points_list_widget.count() < 6):
            self.delete_point_button.setDisabled(True)

    def draw(self):
        P = np.array([np.array([self.points_list_widget.itemWidget(self.points_list_widget.item(i)).x_spin_box.value(), self.points_list_widget.itemWidget(self.points_list_widget.item(i)).y_spin_box.value()]) for i in range(self.points_list_widget.count())])
        self.plot_widget.plot(P)

if __name__ == '__main__':
    app = QApplication([])
    p = MainWindow()
    p.show()

    sys.exit(app.exec_())