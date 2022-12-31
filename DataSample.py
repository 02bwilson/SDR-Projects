from rtlsdr import *

class sample:
    _VERSION_ = "1.0"

    def __init__(self, sdr=None):

        # Set SDR Obj
        self.sdr = sdr

        # Set Sample size
        self.size = 9046

    def size(self, size):
        self.size = size

    def get(self, size):
        if size is None:
            return self.sdr.read_samples(self.size)
        else:
            return self.sdr.read_samples(size)
