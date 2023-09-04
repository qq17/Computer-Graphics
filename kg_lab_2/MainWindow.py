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
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.points_list_widget = QListWidget(self.centralwidget)
        self.points_list_widget.setObjectName(u"points_list_widget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.points_list_widget.sizePolicy().hasHeightForWidth())
        self.points_list_widget.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.points_list_widget)

        self.add_point_button = QPushButton(self.centralwidget)
        self.add_point_button.setObjectName(u"add_point_button")

        self.verticalLayout.addWidget(self.add_point_button)

        self.delete_point_button = QPushButton(self.centralwidget)
        self.delete_point_button.setObjectName(u"delete_point_button")

        self.verticalLayout.addWidget(self.delete_point_button)

        self.draw_button = QPushButton(self.centralwidget)
        self.draw_button.setObjectName(u"draw_button")

        self.verticalLayout.addWidget(self.draw_button)


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
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.add_point_button.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0442\u043e\u0447\u043a\u0443", None))
        self.delete_point_button.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0442\u043e\u0447\u043a\u0443", None))
        self.draw_button.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0440\u0438\u0441\u043e\u0432\u0430\u0442\u044c \u0441\u043f\u043b\u0430\u0439\u043d", None))
    # retranslateUi

