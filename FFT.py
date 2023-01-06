import sys
import os
import threading
import time

from PyQt6 import QtCore

from configure import SDR
from DataSample import sample

from PyQt6.QtWidgets import *
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg


class FFT(QMainWindow):

    def __init__(self, sdr, dg):
        super().__init__()
        self.sdr = sdr
        self.dg = dg
        self.file = None

        self.setWindowTitle("FFT by Bryce W")

        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)

        self.timer = None

        self.thrd = threading.Thread(target=self.start_update)
        self.thrd.daemon = True
        self.thrd.start()

    def start_update(self):
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.get_data)
        self.timer.start(1)

    def get_data(self):
            self.graphWidget.clear()
            data = [data.real for data in self.dg.get(50)]
            self.graphWidget.plot(data)


if __name__ == "__main__":
    sdr = SDR(center_freq=106.9e6)
    dg = sample(sdr)
    app = QApplication(sys.argv)
    main = FFT(sdr, dg)
    main.show()
    app.exec()
