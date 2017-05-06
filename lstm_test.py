# -*- coding:utf-8 -*-
# carete by steve at  2017 / 05 / 06　17:49


import numpy as np


import scipy as sp

import matplotlib.pyplot as plt


class DataGenerator:
    def __init__(self,range_file,real_file):
        self.uwb_data = np.loadtxt(range_file)
        self.real_data = np.loadtxt(real_file)

        print(self.uwb_data,self.real_data)


if __name__ == '__main__':
    dg = DataGenerator("./small_data/uwb_range","./small_data/real_range")
    # uwb_range =
