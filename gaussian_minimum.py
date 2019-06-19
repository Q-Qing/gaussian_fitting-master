import numpy as np
from scipy.optimize import shgo

class global_minimum():

    def __init__(self, real_list,peak_index):
        self.real_list = real_list
        self.peak_index = peak_index
        self.n = len(peak_index)
        self.N = len(real_list)

    def objective_func(self,parameters):
        f = 0
        for j in range(self.N):
            for i in range(self.n):
                alpha = parameters[i * 3 + 0]
                miu = parameters[i * 3 + 1]
                sigma2 = parameters[i * 3 + 2]
                f += alpha * np.exp((-(j - miu) ** 2) / (2 * sigma2))
            f += (f-self.real_list[j])**2
        return f

    def bound(self):
        bound = []
        for i in range(self.n):
            alpha = self.real_list[self.peak_index[i]]
            alpha_bound = (max(alpha-5,0),alpha+5)
            miu = self.peak_index[i]
            miu_bound = (max(miu-5,0), min(miu+5,(self.N-1)))
            sigma2_bound = (1,5)
            bound.append(alpha_bound)
            bound.append(miu_bound)
            bound.append(sigma2_bound)
        return bound

    def get_global_minimum(self):
        bound = self.bound()
        result = shgo(self.objective_func,bounds=bound)
        print(result)

test_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 2, 2, 1, 1, 3, 4, 4, 4, 4, 2, 3, 4, 9, 19, 38, 52, 54, 50, 30, 17, 9, 5, 3, 2, 2, 1, 1, 2, 2, 2, 2, 1, 3, 3, 5, 4, 4, 5, 4, 5, 5, 5, 4, 2, 2, 5, 4, 4, 5, 4, 5, 9, 10, 10, 10, 7, 6, 9, 11, 12, 14, 13, 12, 8, 9, 10, 14, 13, 12, 12, 8, 8, 7, 10, 9, 10, 13, 10, 8, 5, 5, 3, 2, 3, 4, 3, 4, 4, 4, 6, 7, 8, 7, 7, 6, 4, 3, 2, 3, 3, 4, 2, 3, 2, 4, 5, 4, 4, 2, 5, 6, 8, 9, 5, 5, 4, 3, 3, 2, 5, 20, 36, 39, 36, 25, 8, 3, 3, 4, 4, 3, 4, 4, 4, 4, 4, 4, 14, 19, 27, 32, 35, 41, 45, 48, 55, 56, 61, 65, 63, 65, 65, 62, 60, 53, 51, 44, 36, 31, 25, 21, 19, 12, 9, 5, 4, 3, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 220]
real_list = test_list[0:288]
peak_index = [100,144,206,234]
gm = global_minimum(real_list,peak_index)
gm.get_global_minimum()