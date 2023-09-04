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

        self.iv = np.array([1, 0])
        self.jv = np.array([0, 1])
        self.kv = np.array([-0.7 / np.sqrt(2), -0.5 / np.sqrt(2)])

        self.Pi = []

        self.ax = self.figure.add_subplot(111)

        self.line = []
        for i in range(8):
            self.line.append(self.ax.plot([], [], 'b')[0])

        self.bezier_line = []
        for i in range(798):
            self.bezier_line.append(self.ax.plot([], [], 'g')[0])


        self.linex, = self.ax.plot([0, (100 * self.iv + 0 * self.jv + 0 * self.kv)[0]], [0, (100 * self.iv + 0 * self.jv + 0 * self.kv)[1]], 'k')
        self.liney, = self.ax.plot([0, (0 * self.iv + 100 * self.jv + 0 * self.kv)[0]], [0, (0 * self.iv + 100 * self.jv + 0 * self.kv)[1]], 'k')
        self.linez, = self.ax.plot([0, (0 * self.iv + 0 * self.jv + 100 * self.kv)[0]], [0, (0 * self.iv + 0 * self.jv + 100 * self.kv)[1]], 'k')
        self.bezier_point, = self.ax.plot([], [], 'g.')
        self.point, = self.ax.plot([], [], 'b.')

        self.ax.spines['top'].set_color('none')
        self.ax.spines['right'].set_color('none')
        self.ax.spines['bottom'].set_color('none')
        self.ax.spines['left'].set_color('none')

        self.ax.spines['left'].set_position('zero')
        self.ax.spines['bottom'].set_position('zero')

        self.ax.text((100 * self.iv + 0 * self.jv + 0 * self.kv)[0], (100 * self.iv + 0 * self.jv + 0 * self.kv)[1], "x")
        self.ax.text((0 * self.iv + 100 * self.jv + 0 * self.kv)[0], (0 * self.iv + 100 * self.jv + 0 * self.kv)[1], "y")
        self.ax.text((0 * self.iv + 0 * self.jv + 110 * self.kv)[0], (0 * self.iv + 0 * self.jv + 110 * self.kv)[1], "z")

        self.ax.set_xlim([-100, 100])
        self.ax.set_ylim([-100, 100])

        self.ax.xaxis.set_visible(False)
        self.ax.yaxis.set_visible(False)

    def dim3_p(self, P):
        return P[0] * self.iv + P[1] * self.jv + P[2] * self.kv

    def Pf(self, s, t, P):
        res = 0
        for i in range(4):
            for j in range(4):
                res += np.math.comb(3, i)*(s**i)*((1-s)**(3-i)) * np.math.comb(3, j)*(t**j)*((1-t)**(3-j)) * P[4*i+j]
        return res

    def bezier_surf(self, P):
        res = []
        step = 0.05
        for s in np.arange(0, 1, step):
            for t in np.arange(0, 1, step):
                res.append(self.Pf(s, t, P))
        return np.array(res)


    def plot(self):
        self.bezier_points = self.bezier_surf(self.Pi)

        self.bezier_point.set_xdata([i[0] for i in [self.dim3_p(p) for p in self.bezier_points]])
        self.bezier_point.set_ydata([i[1] for i in [self.dim3_p(p) for p in self.bezier_points]])

        self.point.set_xdata([i[0] for i in [self.dim3_p(p) for p in self.Pi]])
        self.point.set_ydata([i[1] for i in [self.dim3_p(p) for p in self.Pi]])

        for i in range(4):
            self.line[i].set_xdata([el[0] for el in [self.dim3_p(p) for p in self.Pi[(4*i):(4*i+4)]]])
            self.line[i].set_ydata([el[1] for el in [self.dim3_p(p) for p in self.Pi[(4*i):(4*i+4)]]])

        for i in range(4):
            self.line[4+i].set_xdata([el[0] for el in [self.dim3_p(p) for p in [self.Pi[j] for j in range(i, 16, 4)]]])
            self.line[4+i].set_ydata([el[1] for el in [self.dim3_p(p) for p in [self.Pi[j] for j in range(i, 16, 4)]]])

        for i in range(20):
            for j in range(19):
                self.bezier_line[20*i+j].set_xdata([self.dim3_p(self.bezier_points[20*i + j])[0], self.dim3_p(self.bezier_points[20*i + j + 1])[0]])
                self.bezier_line[20*i+j].set_ydata([self.dim3_p(self.bezier_points[20*i + j])[1], self.dim3_p(self.bezier_points[20*i + j + 1])[1]])

        for i in range(20):
            for j in range(19):
                self.bezier_line[399+20 * i + j].set_xdata([self.dim3_p(self.bezier_points[20*j + i])[0], self.dim3_p(self.bezier_points[20*(j+1) + i])[0]])
                self.bezier_line[399+20 * i + j].set_ydata([self.dim3_p(self.bezier_points[20*j + i])[1], self.dim3_p(self.bezier_points[20*(j+1) + i])[1]])


        self.figure.canvas.draw()
        self.figure.canvas.flush_events()

    def turn_x(self, a):
        Tx = np.array([[1, 0, 0, 0],
                       [0, np.cos(a * np.pi / 180), np.sin(a * np.pi / 180), 0],
                       [0, -np.sin(a * np.pi / 180), np.cos(a * np.pi / 180), 0],
                       [0, 0, 0, 1]])

        self.Pi = (np.c_[self.Pi, np.ones(len(self.Pi))].dot(Tx))[:, :3]
        self.plot()

    def turn_y(self, a):
        Ty = np.array([[np.cos(a * np.pi / 180), 0, -np.sin(a * np.pi / 180), 0],
                       [0, 1, 0, 0],
                       [np.sin(a * np.pi / 180), 0, np.cos(a * np.pi / 180), 0],
                       [0, 0, 0, 1]])

        self.Pi = (np.c_[self.Pi, np.ones(len(self.Pi))].dot(Ty))[:, :3]
        self.plot()