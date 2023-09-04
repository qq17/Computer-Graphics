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
        self.A_lbl = QLabel(self.centralwidget)
        self.A_lbl.setObjectName(u"A_lbl")

        self.horizontalLayout.addWidget(self.A_lbl)

        self.x1_lbl = QLabel(self.centralwidget)
        self.x1_lbl.setObjectName(u"x1_lbl")

        self.horizontalLayout.addWidget(self.x1_lbl)

        self.x1_sb = QSpinBox(self.centralwidget)
        self.x1_sb.setObjectName(u"x1_sb")
        self.x1_sb.setMinimum(-100)
        self.x1_sb.setMaximum(100)

        self.horizontalLayout.addWidget(self.x1_sb)

        self.y1_lbl = QLabel(self.centralwidget)
        self.y1_lbl.setObjectName(u"y1_lbl")

        self.horizontalLayout.addWidget(self.y1_lbl)

        self.y1_sb = QSpinBox(self.centralwidget)
        self.y1_sb.setObjectName(u"y1_sb")
        self.y1_sb.setMinimum(-100)
        self.y1_sb.setMaximum(100)

        self.horizontalLayout.addWidget(self.y1_sb)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.B_lbl = QLabel(self.centralwidget)
        self.B_lbl.setObjectName(u"B_lbl")

        self.horizontalLayout_2.addWidget(self.B_lbl)

        self.x2_lbl = QLabel(self.centralwidget)
        self.x2_lbl.setObjectName(u"x2_lbl")

        self.horizontalLayout_2.addWidget(self.x2_lbl)

        self.x2_sb = QSpinBox(self.centralwidget)
        self.x2_sb.setObjectName(u"x2_sb")
        self.x2_sb.setMinimum(-100)
        self.x2_sb.setMaximum(100)

        self.horizontalLayout_2.addWidget(self.x2_sb)

        self.y2_lbl = QLabel(self.centralwidget)
        self.y2_lbl.setObjectName(u"y2_lbl")

        self.horizontalLayout_2.addWidget(self.y2_lbl)

        self.y2_sb = QSpinBox(self.centralwidget)
        self.y2_sb.setObjectName(u"y2_sb")
        self.y2_sb.setMinimum(-100)
        self.y2_sb.setMaximum(100)
        self.y2_sb.setValue(0)

        self.horizontalLayout_2.addWidget(self.y2_sb)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.C_lbl = QLabel(self.centralwidget)
        self.C_lbl.setObjectName(u"C_lbl")

        self.horizontalLayout_3.addWidget(self.C_lbl)

        self.x3_lbl = QLabel(self.centralwidget)
        self.x3_lbl.setObjectName(u"x3_lbl")

        self.horizontalLayout_3.addWidget(self.x3_lbl)

        self.x3_sb = QSpinBox(self.centralwidget)
        self.x3_sb.setObjectName(u"x3_sb")
        self.x3_sb.setMinimum(-100)
        self.x3_sb.setMaximum(100)

        self.horizontalLayout_3.addWidget(self.x3_sb)

        self.y3_lbl = QLabel(self.centralwidget)
        self.y3_lbl.setObjectName(u"y3_lbl")

        self.horizontalLayout_3.addWidget(self.y3_lbl)

        self.y3_sb = QSpinBox(self.centralwidget)
        self.y3_sb.setObjectName(u"y3_sb")
        self.y3_sb.setMinimum(-100)
        self.y3_sb.setMaximum(100)

        self.horizontalLayout_3.addWidget(self.y3_sb)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.Point_lbl = QLabel(self.centralwidget)
        self.Point_lbl.setObjectName(u"Point_lbl")

        self.horizontalLayout_4.addWidget(self.Point_lbl)

        self.x0_lbl = QLabel(self.centralwidget)
        self.x0_lbl.setObjectName(u"x0_lbl")

        self.horizontalLayout_4.addWidget(self.x0_lbl)

        self.x0_sb = QSpinBox(self.centralwidget)
        self.x0_sb.setObjectName(u"x0_sb")
        self.x0_sb.setMinimum(-100)
        self.x0_sb.setMaximum(100)

        self.horizontalLayout_4.addWidget(self.x0_sb)

        self.y0_lbl = QLabel(self.centralwidget)
        self.y0_lbl.setObjectName(u"y0_lbl")

        self.horizontalLayout_4.addWidget(self.y0_lbl)

        self.y0_sb = QSpinBox(self.centralwidget)
        self.y0_sb.setObjectName(u"y0_sb")
        self.y0_sb.setMinimum(-100)
        self.y0_sb.setMaximum(100)
        self.y0_sb.setValue(0)

        self.horizontalLayout_4.addWidget(self.y0_sb)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.angle_lbl = QLabel(self.centralwidget)
        self.angle_lbl.setObjectName(u"angle_lbl")

        self.horizontalLayout_5.addWidget(self.angle_lbl)

        self.angle_sb = QSpinBox(self.centralwidget)
        self.angle_sb.setObjectName(u"angle_sb")
        self.angle_sb.setMinimum(-360)
        self.angle_sb.setMaximum(360)
        self.angle_sb.setValue(0)

        self.horizontalLayout_5.addWidget(self.angle_sb)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.draw_button = QPushButton(self.centralwidget)
        self.draw_button.setObjectName(u"draw_button")

        self.verticalLayout.addWidget(self.draw_button)

        self.turn_button = QPushButton(self.centralwidget)
        self.turn_button.setObjectName(u"turn_button")

        self.verticalLayout.addWidget(self.turn_button)


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
        self.A_lbl.setText(QCoreApplication.translate("MainWindow", u"A: ", None))
        self.x1_lbl.setText(QCoreApplication.translate("MainWindow", u"x1", None))
        self.y1_lbl.setText(QCoreApplication.translate("MainWindow", u"y1", None))
        self.B_lbl.setText(QCoreApplication.translate("MainWindow", u"B: ", None))
        self.x2_lbl.setText(QCoreApplication.translate("MainWindow", u"x2", None))
        self.y2_lbl.setText(QCoreApplication.translate("MainWindow", u"y2", None))
        self.C_lbl.setText(QCoreApplication.translate("MainWindow", u"C: ", None))
        self.x3_lbl.setText(QCoreApplication.translate("MainWindow", u"x3", None))
        self.y3_lbl.setText(QCoreApplication.translate("MainWindow", u"y3", None))
        self.Point_lbl.setText(QCoreApplication.translate("MainWindow", u"\u0422\u043e\u0447\u043a\u0430:", None))
        self.x0_lbl.setText(QCoreApplication.translate("MainWindow", u"x0", None))
        self.y0_lbl.setText(QCoreApplication.translate("MainWindow", u"y0", None))
        self.angle_lbl.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0433\u043e\u043b:", None))
        self.draw_button.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0440\u0438\u0441\u043e\u0432\u0430\u0442\u044c \u0444\u0438\u0433\u0443\u0440\u0443", None))
        self.turn_button.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0432\u043e\u0440\u043e\u0442", None))
    # retranslateUi

