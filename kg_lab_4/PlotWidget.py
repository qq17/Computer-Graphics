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

        self.ax = self.figure.add_subplot(111)

        self.window, = self.ax.plot([], [], 'k')

        self.ax.set_xlim([-100, 100])
        self.ax.set_ylim([-100, 100])

    def plot(self, Pi, window):
        for p in Pi:
            self.ax.plot([p[0], p[1]], [p[2], p[3]], 'b')

        print(window[0]+window[0][::-1]+[window[0][0]])
        print(2*[window[1][0]]+2*[window[1][1]]+[window[1][0]])

        self.window.set_xdata(window[0]+window[0][::-1]+[window[0][0]])
        self.window.set_ydata(2*[window[1][0]]+2*[window[1][1]]+[window[1][0]])

        xl = min(window[0])
        xp = max(window[0])
        yn = min(window[1])
        yv = max(window[1])
        print(xl, xp, yn, yv)

        for p in Pi:
            # print(p[0], [p[1]])
            if (p[0]<xl and p[1]<xl) or (p[0]>xp and p[1]>xp) or (p[2]<yn and p[3]<yn) or (p[2]>yv and p[3]>yv):
                self.ax.plot([p[0], p[1]], [p[2], p[3]], 'r')

            if not ((p[0]<=xl or p[0]>=xp) or (p[1]<=xl or p[1]>=xp) or (p[2]<=yn or p[2]>=yv) or (p[3]<=yn or p[3]>=yv)):
                self.ax.plot([p[0], p[1]], [p[2], p[3]], 'g')

        self.figure.canvas.draw()
        self.figure.canvas.flush_events()


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.initUi()
        self.connectUi()

    def initUi(self):
        self.centralWidget = QWidget(self)

        self.l = QVBoxLayout(self.centralWidget)
        # self.bl = QHBoxLayout(self.centralWidget)

        self.plotWidget = PlotWidget()

        self.plotButton = QPushButton('Plot')
        self.clearButton = QPushButton('Clear')

        self.plotButton.setStyleSheet('font-size: 12pt; font-weight: 530;')
        self.clearButton.setStyleSheet('font-size: 12pt; font-weight: 530;')

        self.l.addWidget(self.plotButton)
        self.l.addWidget(self.clearButton)

        # self.l.addLayout(self.bl)
        self.l.addWidget(self.plotWidget)

        self.setCentralWidget(self.centralWidget)

    def connectUi(self):
        self.plotButton.clicked.connect(self.plot)
        self.clearButton.clicked.connect(self.clear)

    def clear(self):
        # # self.plotWidget.figure.clear()
        # self.plotWidget.plot(0, 1, 2, 3, 4, 5)
        # self.plotWidget.canvas.draw()
        pass

    def plot(self):
        Pi = np.random.randint(-100, 100, size=(10, 4))
        window = [[-35, 30],[90, -10]]
        self.plotWidget.plot(Pi, window)


if __name__ == '__main__':
    app = QApplication([])
    p = MainWindow()
    p.show()

    sys.exit(app.exec_())