import numpy as np
from PySide2.QtWidgets import *

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import itertools


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
        self.point, = self.ax.plot([], [], 'g.')

        self.old_P = []
        self.segments = []

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

        self.Minv = np.linalg.inv(np.array([[r*r, r, 1] for r in [-0.5, 0, 0.5]]))


    def P(self, r, Pi):
        return (np.array([r*r, r, 1]).dot(self.Minv)).dot(Pi)

    def Q(self, s, Pi):
        return (np.array([s*s, s, 1]).dot(self.Minv)).dot(Pi)

    def C(self, t, Pi):
        r = 0.5*t
        s = 0.5*(t-1)
        return self.P(r, Pi[0:3])*(1-t) + self.Q(s, Pi[1:4])*t

    def plot(self, P):
        self.point.set_xdata(P[:, 0].tolist())
        self.point.set_ydata(P[:, 1].tolist())

        if self.old_P == []:
            self.segments.append([self.P(t, P[0:3]) for t in np.arange(-0.5, 0, 0.01)])
            for i in range(1, len(P) - 2):
                self.segments.append([self.C(t, P[(i - 1):(i + 3)]) for t in np.arange(0, 1, 0.01)])
            self.segments.append([self.Q(t, P[-3::1]) for t in np.arange(0, 0.5, 0.01)])
        else:
            n = min(len(P), len(self.old_P))
            recalced = []

            for i in range(n):
                if not (P[i] == self.old_P[i]).all():
                    if i in [0, 1, 2]:
                        if 0 not in recalced:
                            self.segments[0] = [self.P(t, P[0:3]) for t in np.arange(-0.5, 0, 0.01)]
                            recalced = recalced + [0]
                    for j in range(max(1,i-2), min(i+2, n-2)):
                        if j not in recalced:
                            self.segments[j] = [self.C(t, P[(j - 1):(j + 3)]) for t in np.arange(0, 1, 0.01)]
                            recalced = recalced + [j]
                    if i in [(n-3), (n-2), (n-1)]:
                        if (n-2) not in recalced:
                            self.segments[n - 2]=[self.Q(t, P[-3::1]) for t in np.arange(0, 0.5, 0.01)]
                            recalced = recalced + [(n-2)]

            if len(P)<len(self.old_P):
                self.segments[n - 2]=[self.Q(t, P[-3::1]) for t in np.arange(0, 0.5, 0.01)]
                del self.segments[n-1:]

            if len(P)>len(self.old_P):
                self.segments[n-2] = [self.C(t, P[(n - 3):(n + 1)]) for t in np.arange(0, 1, 0.01)]
                for i in range(n-1, len(P)-2):
                    self.segments.append([self.C(t, P[(i - 1):(i + 3)]) for t in np.arange(0, 1, 0.01)])
                self.segments.append([self.Q(t, P[-3::1]) for t in np.arange(0, 0.5, 0.01)])

        self.line1.set_xdata([i[0] for i in list(itertools.chain.from_iterable(self.segments))])
        self.line1.set_ydata([i[1] for i in list(itertools.chain.from_iterable(self.segments))])

        self.figure.canvas.draw()
        self.figure.canvas.flush_events()

        self.old_P = P