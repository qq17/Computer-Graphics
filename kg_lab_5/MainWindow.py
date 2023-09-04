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
        self.horizontalLayout_6 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.a_x_lbl = QLabel(self.centralwidget)
        self.a_x_lbl.setObjectName(u"a_x_lbl")

        self.horizontalLayout.addWidget(self.a_x_lbl)

        self.a_x_sb = QSpinBox(self.centralwidget)
        self.a_x_sb.setObjectName(u"a_x_sb")
        self.a_x_sb.setMinimum(-100)
        self.a_x_sb.setMaximum(100)

        self.horizontalLayout.addWidget(self.a_x_sb)

        self.a_y_lbl = QLabel(self.centralwidget)
        self.a_y_lbl.setObjectName(u"a_y_lbl")

        self.horizontalLayout.addWidget(self.a_y_lbl)

        self.a_y_sb = QSpinBox(self.centralwidget)
        self.a_y_sb.setObjectName(u"a_y_sb")
        self.a_y_sb.setMinimum(-100)
        self.a_y_sb.setMaximum(100)

        self.horizontalLayout.addWidget(self.a_y_sb)

        self.a_z_lbl = QLabel(self.centralwidget)
        self.a_z_lbl.setObjectName(u"a_z_lbl")

        self.horizontalLayout.addWidget(self.a_z_lbl)

        self.a_z_sb = QSpinBox(self.centralwidget)
        self.a_z_sb.setObjectName(u"a_z_sb")
        self.a_z_sb.setMinimum(-100)
        self.a_z_sb.setMaximum(100)

        self.horizontalLayout.addWidget(self.a_z_sb)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.b_x_lbl = QLabel(self.centralwidget)
        self.b_x_lbl.setObjectName(u"b_x_lbl")

        self.horizontalLayout_2.addWidget(self.b_x_lbl)

        self.b_x_sb = QSpinBox(self.centralwidget)
        self.b_x_sb.setObjectName(u"b_x_sb")
        self.b_x_sb.setMinimum(-100)
        self.b_x_sb.setMaximum(100)

        self.horizontalLayout_2.addWidget(self.b_x_sb)

        self.b_y_lbl = QLabel(self.centralwidget)
        self.b_y_lbl.setObjectName(u"b_y_lbl")

        self.horizontalLayout_2.addWidget(self.b_y_lbl)

        self.b_y_sb = QSpinBox(self.centralwidget)
        self.b_y_sb.setObjectName(u"b_y_sb")
        self.b_y_sb.setMinimum(-100)
        self.b_y_sb.setMaximum(100)
        self.b_y_sb.setValue(0)

        self.horizontalLayout_2.addWidget(self.b_y_sb)

        self.b_z_lbl = QLabel(self.centralwidget)
        self.b_z_lbl.setObjectName(u"b_z_lbl")

        self.horizontalLayout_2.addWidget(self.b_z_lbl)

        self.b_z_sb = QSpinBox(self.centralwidget)
        self.b_z_sb.setObjectName(u"b_z_sb")
        self.b_z_sb.setMinimum(-100)
        self.b_z_sb.setMaximum(100)

        self.horizontalLayout_2.addWidget(self.b_z_sb)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.c_x_lbl = QLabel(self.centralwidget)
        self.c_x_lbl.setObjectName(u"c_x_lbl")

        self.horizontalLayout_3.addWidget(self.c_x_lbl)

        self.c_x_sb = QSpinBox(self.centralwidget)
        self.c_x_sb.setObjectName(u"c_x_sb")
        self.c_x_sb.setMinimum(-100)
        self.c_x_sb.setMaximum(100)

        self.horizontalLayout_3.addWidget(self.c_x_sb)

        self.c_y_lbl = QLabel(self.centralwidget)
        self.c_y_lbl.setObjectName(u"c_y_lbl")

        self.horizontalLayout_3.addWidget(self.c_y_lbl)

        self.c_y_sb = QSpinBox(self.centralwidget)
        self.c_y_sb.setObjectName(u"c_y_sb")
        self.c_y_sb.setMinimum(-100)
        self.c_y_sb.setMaximum(100)

        self.horizontalLayout_3.addWidget(self.c_y_sb)

        self.c_z_lbl = QLabel(self.centralwidget)
        self.c_z_lbl.setObjectName(u"c_z_lbl")

        self.horizontalLayout_3.addWidget(self.c_z_lbl)

        self.c_z_sb = QSpinBox(self.centralwidget)
        self.c_z_sb.setObjectName(u"c_z_sb")
        self.c_z_sb.setMinimum(-100)
        self.c_z_sb.setMaximum(100)

        self.horizontalLayout_3.addWidget(self.c_z_sb)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.a1_x_lbl = QLabel(self.centralwidget)
        self.a1_x_lbl.setObjectName(u"a1_x_lbl")

        self.horizontalLayout_4.addWidget(self.a1_x_lbl)

        self.a1_x_sb = QSpinBox(self.centralwidget)
        self.a1_x_sb.setObjectName(u"a1_x_sb")
        self.a1_x_sb.setMinimum(-100)
        self.a1_x_sb.setMaximum(100)

        self.horizontalLayout_4.addWidget(self.a1_x_sb)

        self.a1_y_lbl = QLabel(self.centralwidget)
        self.a1_y_lbl.setObjectName(u"a1_y_lbl")

        self.horizontalLayout_4.addWidget(self.a1_y_lbl)

        self.a1_y_sb = QSpinBox(self.centralwidget)
        self.a1_y_sb.setObjectName(u"a1_y_sb")
        self.a1_y_sb.setMinimum(-100)
        self.a1_y_sb.setMaximum(100)
        self.a1_y_sb.setValue(0)

        self.horizontalLayout_4.addWidget(self.a1_y_sb)

        self.a1_z_lbl = QLabel(self.centralwidget)
        self.a1_z_lbl.setObjectName(u"a1_z_lbl")

        self.horizontalLayout_4.addWidget(self.a1_z_lbl)

        self.a1_z_sb = QSpinBox(self.centralwidget)
        self.a1_z_sb.setObjectName(u"a1_z_sb")
        self.a1_z_sb.setMinimum(-100)
        self.a1_z_sb.setMaximum(100)

        self.horizontalLayout_4.addWidget(self.a1_z_sb)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.draw_button = QPushButton(self.centralwidget)
        self.draw_button.setObjectName(u"draw_button")

        self.verticalLayout.addWidget(self.draw_button)

        self.del_invis_button = QPushButton(self.centralwidget)
        self.del_invis_button.setObjectName(u"del_invis_button")

        self.verticalLayout.addWidget(self.del_invis_button)


        self.horizontalLayout_6.addLayout(self.verticalLayout)

        self.plot_widget = PlotWidget(self.centralwidget)
        self.plot_widget.setObjectName(u"plot_widget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plot_widget.sizePolicy().hasHeightForWidth())
        self.plot_widget.setSizePolicy(sizePolicy)

        self.horizontalLayout_6.addWidget(self.plot_widget)

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
        self.a_x_lbl.setText(QCoreApplication.translate("MainWindow", u"A:  x", None))
        self.a_y_lbl.setText(QCoreApplication.translate("MainWindow", u"y", None))
        self.a_z_lbl.setText(QCoreApplication.translate("MainWindow", u"z", None))
        self.b_x_lbl.setText(QCoreApplication.translate("MainWindow", u"B:  x", None))
        self.b_y_lbl.setText(QCoreApplication.translate("MainWindow", u"y", None))
        self.b_z_lbl.setText(QCoreApplication.translate("MainWindow", u"z", None))
        self.c_x_lbl.setText(QCoreApplication.translate("MainWindow", u"C:  x", None))
        self.c_y_lbl.setText(QCoreApplication.translate("MainWindow", u"y", None))
        self.c_z_lbl.setText(QCoreApplication.translate("MainWindow", u"z", None))
        self.a1_x_lbl.setText(QCoreApplication.translate("MainWindow", u"A1: x", None))
        self.a1_y_lbl.setText(QCoreApplication.translate("MainWindow", u"y", None))
        self.a1_z_lbl.setText(QCoreApplication.translate("MainWindow", u"z", None))
        self.draw_button.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0440\u0438\u0441\u043e\u0432\u0430\u0442\u044c \u0444\u0438\u0433\u0443\u0440\u0443", None))
        self.del_invis_button.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0431\u0440\u0430\u0442\u044c \u043d\u0435\u0432\u0438\u0434\u0438\u043c\u044b\u0435 \u0433\u0440\u0430\u043d\u0438", None))
    # retranslateUi

