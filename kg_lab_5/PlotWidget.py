import sys
import numpy as np
from PySide2.QtCore import *
from PySide2.QtWidgets import *

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class PlotWidget(QWidget):

    def __init__(self, parent=None):
        super(PlotWidget, self).__init__(parent)

        self.initUi()

    def initUi(self):
        self.mainLayout = QVBoxLayout(self)

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)

        self.mainLayout.addWidget(self.canvas)

        self.iv = np.array([-0.7 / np.sqrt(2), -0.5 / np.sqrt(2)])
        self.jv = np.array([1, 0])
        self.kv = np.array([0, 1])

        self.ax = self.figure.add_subplot(111)

        self.line = []
        for i in range(6):
            self.line.append(self.ax.plot([], [], 'b')[0])

        self.ax.spines['top'].set_color('none')
        self.ax.spines['right'].set_color('none')
        self.ax.spines['bottom'].set_color('none')
        self.ax.spines['left'].set_color('none')

        self.ax.spines['left'].set_position('zero')
        self.ax.spines['bottom'].set_position('zero')

        self.ax.set_xlim([-100, 100])
        self.ax.set_ylim([-100, 100])

        self.ax.xaxis.set_visible(False)
        self.ax.yaxis.set_visible(False)

    def dim3_p(self, P):
        return P[0] * self.iv + P[1] * self.jv + P[2] * self.kv

    def f(self, p, g):
        x = p[0]
        y = p[1]
        z = p[2]
        x1 = g[0][0]
        x2 = g[1][0]
        x3 = g[2][0]
        y1 = g[0][1]
        y2 = g[1][1]
        y3 = g[2][1]
        z1 = g[0][2]
        z2 = g[1][2]
        z3 = g[2][2]

        A = [[x-x1,  y-y1,  z-z1],
             [x2-x1, y2-y1, z2-z1],
             [x3-x1, y3-y1, z3-z1]]

        return np.linalg.det(A)

    def plot(self, Pi):
        A = Pi[0]
        B = Pi[1]
        C = Pi[2]
        A1 = Pi[3]

        h = A1-A

        D = C-B+A
        B1 = B+h
        C1 = C+h
        D1 = D+h

        V = np.array([2*np.sqrt(2), 1.4, 1])*1000

        O = C+(A1-C)/2

        self.line[0].set_xdata([self.dim3_p(p)[0] for p in [A, B, C, D, A]])
        self.line[0].set_ydata([self.dim3_p(p)[1] for p in [A, B, C, D, A]])

        self.line[1].set_xdata([self.dim3_p(p)[0] for p in [A1, B1, C1, D1, A1]])
        self.line[1].set_ydata([self.dim3_p(p)[1] for p in [A1, B1, C1, D1, A1]])

        self.line[2].set_xdata([self.dim3_p(p)[0] for p in [A, A1, B1, B, A]])
        self.line[2].set_ydata([self.dim3_p(p)[1] for p in [A, A1, B1, B, A]])

        self.line[3].set_xdata([self.dim3_p(p)[0] for p in [A, A1, D1, D, A]])
        self.line[3].set_ydata([self.dim3_p(p)[1] for p in [A, A1, D1, D, A]])

        self.line[4].set_xdata([self.dim3_p(p)[0] for p in [D, D1, C1, C, D]])
        self.line[4].set_ydata([self.dim3_p(p)[1] for p in [D, D1, C1, C, D]])

        self.line[5].set_xdata([self.dim3_p(p)[0] for p in [B, B1, C1, C, B]])
        self.line[5].set_ydata([self.dim3_p(p)[1] for p in [B, B1, C1, C, B]])

        self.figure.canvas.draw()
        self.figure.canvas.flush_events()


    def plot_del_invis(self, Pi):
        A = Pi[0]
        B = Pi[1]
        C = Pi[2]
        A1 = Pi[3]

        h = A1-A

        D = C-B+A
        B1 = B+h
        C1 = C+h
        D1 = D+h

        V = np.array([2*np.sqrt(2), 1.4, 1])*1000

        O = C+(A1-C)/2

        if self.f(O, [A, B, C])*self.f(V, [A, B, C])<0:
            self.line[0].set_xdata([self.dim3_p(p)[0] for p in [A, B, C, D, A]])
            self.line[0].set_ydata([self.dim3_p(p)[1] for p in [A, B, C, D, A]])
        else:
            self.line[0].set_xdata([])
            self.line[0].set_ydata([])

        if self.f(O, [A1, B1, C1]) * self.f(V, [A1, B1, C1]) < 0:
            self.line[1].set_xdata([self.dim3_p(p)[0] for p in [A1, B1, C1, D1, A1]])
            self.line[1].set_ydata([self.dim3_p(p)[1] for p in [A1, B1, C1, D1, A1]])
        else:
            self.line[1].set_xdata([])
            self.line[1].set_ydata([])

        if self.f(O, [A, A1, B1]) * self.f(V, [A, A1, B1]) < 0:
            self.line[2].set_xdata([self.dim3_p(p)[0] for p in [A, A1, B1, B, A]])
            self.line[2].set_ydata([self.dim3_p(p)[1] for p in [A, A1, B1, B, A]])
        else:
            self.line[2].set_xdata([])
            self.line[2].set_ydata([])

        if self.f(O, [A, A1, D1]) * self.f(V, [A, A1, D1]) < 0:
            self.line[3].set_xdata([self.dim3_p(p)[0] for p in [A, A1, D1, D, A]])
            self.line[3].set_ydata([self.dim3_p(p)[1] for p in [A, A1, D1, D, A]])
        else:
            self.line[3].set_xdata([])
            self.line[3].set_ydata([])

        if self.f(O, [D, D1, C1]) * self.f(V, [D, D1, C1]) < 0:
            self.line[4].set_xdata([self.dim3_p(p)[0] for p in [D, D1, C1, C, D]])
            self.line[4].set_ydata([self.dim3_p(p)[1] for p in [D, D1, C1, C, D]])
        else:
            self.line[4].set_xdata([])
            self.line[4].set_ydata([])

        if self.f(O, [B, B1, C1]) * self.f(V, [B, B1, C1]) < 0:
            self.line[5].set_xdata([self.dim3_p(p)[0] for p in [B, B1, C1, C, B]])
            self.line[5].set_ydata([self.dim3_p(p)[1] for p in [B, B1, C1, C, B]])
        else:
            self.line[5].set_xdata([])
            self.line[5].set_ydata([])

        self.figure.canvas.draw()
        self.figure.canvas.flush_events()