# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

from PlotWidget import PlotWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(888, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.points_list_widget = QListWidget(self.centralwidget)
        self.points_list_widget.setObjectName(u"points_list_widget")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.points_list_widget.sizePolicy().hasHeightForWidth())
        self.points_list_widget.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.points_list_widget)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.angle_lbl = QLabel(self.centralwidget)
        self.angle_lbl.setObjectName(u"angle_lbl")

        self.horizontalLayout_2.addWidget(self.angle_lbl)

        self.angle_sb = QSpinBox(self.centralwidget)
        self.angle_sb.setObjectName(u"angle_sb")
        self.angle_sb.setMinimum(-360)
        self.angle_sb.setMaximum(360)

        self.horizontalLayout_2.addWidget(self.angle_sb)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.draw_button = QPushButton(self.centralwidget)
        self.draw_button.setObjectName(u"draw_button")

        self.verticalLayout.addWidget(self.draw_button)

        self.turn_x_button = QPushButton(self.centralwidget)
        self.turn_x_button.setObjectName(u"turn_x_button")

        self.verticalLayout.addWidget(self.turn_x_button)

        self.turn_y_button = QPushButton(self.centralwidget)
        self.turn_y_button.setObjectName(u"turn_y_button")

        self.verticalLayout.addWidget(self.turn_y_button)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.plot_widget = PlotWidget(self.centralwidget)
        self.plot_widget.setObjectName(u"plot_widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.plot_widget.sizePolicy().hasHeightForWidth())
        self.plot_widget.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.plot_widget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 888, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.angle_lbl.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0433\u043e\u043b", None))
        self.draw_button.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u0442\u0440\u043e\u0438\u0442\u044c \u043f\u043e\u0432\u0435\u0440\u0445\u043d\u043e\u0441\u0442\u044c \u0411\u0435\u0437\u044c\u0435", None))
        self.turn_x_button.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0432\u0435\u0440\u043d\u0443\u0442\u044c \u0432\u043e\u043a\u0440\u0443\u0433 \u043e\u0441\u0438 x", None))
        self.turn_y_button.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0432\u0435\u0440\u043d\u0443\u0442\u044c \u0432\u043e\u043a\u0440\u0443\u0433 \u043e\u0441\u0438 y", None))
    # retranslateUi

