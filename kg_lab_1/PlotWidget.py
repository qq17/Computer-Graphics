import numpy as np
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

        self.ax = self.figure.add_subplot(111)

        self.line1, = self.ax.plot([], [])
        self.line2, = self.ax.plot([], [])
        self.point, = self.ax.plot([], [], 'g.')

        self.ax.spines['top'].set_color('none')
        self.ax.spines['right'].set_color('none')

        self.ax.xaxis.set_tick_params(bottom='on', top='off', direction='inout', labelsize=7)
        self.ax.yaxis.set_tick_params(left='on', right='off', direction='inout', labelsize=7)

        self.ax.spines['left'].set_position('zero')
        self.ax.spines['bottom'].set_position('zero')

        self.ax.set_xlim([-100, 100])
        self.ax.set_ylim([-100, 100])

        self.ax.set_xticks(list(range(-100, 0, 10)) + list(range(10, 101, 10)))
        self.ax.set_yticks(list(range(-100, 0, 10)) + list(range(10, 101, 10)))

        self.ax.xaxis.set_ticks_position('bottom')
        self.ax.yaxis.set_ticks_position('left')

        self.figure.tight_layout()

    def plot(self, x1, y1, x2, y2, x3, y3, x0, y0):
        self.line1.set_xdata([x1, x2, x3, x1])
        self.line1.set_ydata([y1, y2, y3, y1])

        self.point.set_xdata(x0)
        self.point.set_ydata(y0)

        self.line2.set_xdata([])
        self.line2.set_ydata([])

        self.figure.canvas.draw()
        self.figure.canvas.flush_events()

    def turn(self, x1, y1, x2, y2, x3, y3, x0, y0, a):
        self.line1.set_xdata([x1, x2, x3, x1])
        self.line1.set_ydata([y1, y2, y3, y1])

        A = np.array([[x1, y1, 1],
                      [x2, y2, 1],
                      [x3, y3, 1]])

        A = A.dot([[1, 0, 0],
                   [0, 1, 0],
                   [-x0, -y0, 1]])

        A = A.dot([[np.cos(a*np.pi/180), np.sin(a*np.pi/180), 0],
                   [-np.sin(a*np.pi/180), np.cos(a*np.pi/180), 0],
                   [0, 0, 1]])

        A = A.dot([[1, 0, 0],
                   [0, 1, 0],
                   [x0, y0, 1]])

        self.point.set_xdata(x0)
        self.point.set_ydata(y0)

        self.line2.set_xdata([A[i%3, 0] for i in range(0, 4)])
        self.line2.set_ydata([A[i%3, 1] for i in range(0, 4)])

        self.figure.canvas.draw()
        self.figure.canvas.flush_events()