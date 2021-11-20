import random
from numba import jit

class ValueE:
    def __init__(self):
        self.n_array = []

    def n_values(self, nn):
        self.n_array = self.n_values_static(nn)

    @staticmethod
    @jit(nopython=True, nogil=True)
    def n_values_static(nn):
        n_array = []
        for _ in range(nn):
            i = 0
            count = 0
            while(i<1):
                x = random.uniform(0, 1)
                i += x
                count += 1
            n_array.append(count)
        return n_array







