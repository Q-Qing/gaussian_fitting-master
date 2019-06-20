'''

input:
    real list and peak index
output:
    picture of gaussian fitting and parameters
'''
import numpy as np
import math
import matplotlib.pyplot as plt
from itertools import product

class multi_gaussian_model():

    def __init__(self, real_list, peak_index):
        self.real_list = real_list
        self.peak_index = peak_index
        self.n = len(peak_index)
        self.N = len(real_list)
        self.best_loss = 99999999999
        self.best_parameters = []


    def loss_calculating(self,f):
        # calculate absolute difference between estimated values and real values
        # loss = sum (|f-y|)
        loss = 0
        for i in range(self.N):
            loss += (f[i]-self.real_list[i])**2
        return loss

    def initialize_parameter(self, sigma2_list):
        # initialize alpha, miu and sigma^2
        # alpha = height of peak, miu = index of peak, sigma^2 = 1
        parameter_list = np.zeros(3 * self.n)
        for i in range(self.n):
            # alpha
            parameter_list[i * 3 + 0] = self.real_list[self.peak_index[i]]
            # miu
            parameter_list[i * 3 + 1] = self.peak_index[i]
            # sigma^2
            parameter_list[i * 3 + 2] = sigma2_list[i]
        return parameter_list

    def fvalue_calculate(self, parameter_list):
        # calculate estimated values according parameters
        f_list = []
        for j in range(self.N):
            f = 0
            for i in range(self.n):
                alpha = parameter_list[i*3+0]
                miu = parameter_list[i*3+1]
                sigma2 = parameter_list[i*3+2]
                f += alpha * math.exp((-(j - miu) ** 2) / (2*sigma2))
            f_list.append(f)
        return f_list


    def gradient_calculate(self, f_list, parameter_list):
        # calculate gradients for each parameter
        gradient_list = []
        for i in range(self.n):
            grad_alpha = 0
            grad_miu = 0
            grad_sigma2 = 0
            for j in range(self.N):
                alpha = parameter_list[i * 3 + 0]
                miu = parameter_list[i * 3 + 1]
                sigma2 = parameter_list[i * 3 + 2]
                grad_alpha += 2*(f_list[j]-self.real_list[j])*math.exp((-(j-miu)**2)/(2*sigma2))
                grad_miu += 2*(alpha*(j-miu)/sigma2)*(f_list[j]-self.real_list[j])*math.exp((-(j-miu)**2)/(2*sigma2))
                grad_sigma2 += 2*(alpha*(j-miu)/(2*(sigma2**2)))*(f_list[j]-self.real_list[j])*math.exp((-(j-miu)**2)/(2*sigma2))
            gradient_list.append(grad_alpha)
            gradient_list.append(grad_miu)
            gradient_list.append(grad_sigma2)
        return gradient_list

    def gradient_descent(self, sigma2_list):
        # init
        best_loss = 0
        best_parameter = []
        parameter_list = self.initialize_parameter(sigma2_list)
        f_list = self.fvalue_calculate(parameter_list)
        loss = self.loss_calculating(f_list)
        print("original loss:",loss)
        gradient_list = self.gradient_calculate(f_list, parameter_list)
        # print("gradient:",gradient_list)
        a = 0.001
        m = len(parameter_list)
        for times in range(1000):
            new_parameters = []
            for i in range(m):
                new_parameter = parameter_list[i] - a*gradient_list[i]
                new_parameters.append(new_parameter)
            # parameter_list = new_parameters
            f_list = self.fvalue_calculate(new_parameters)
            loss_new = self.loss_calculating(f_list)
            if loss_new > loss:
                best_loss = loss
                best_parameter = parameter_list
                break
            loss = loss_new
            parameter_list = new_parameters
            gradient_list = self.gradient_calculate(f_list, parameter_list)
            best_loss = loss
            best_parameter = parameter_list
        print("best loss:", best_loss)
        return best_loss, best_parameter

    def cartesian_produce(self):
        # sigma2_range = np.linspace(5,10,6)
        sigma2_lists = []
        # for i in product(sigma2_range,repeat=self.n):
        #     sigma2_lists.append(i)

        a = [4]
        b = [220,225,230,235,240,250,260]
        c = [3]
        d = [40,45,50]
        for i in product(a,b,c,d):
            sigma2_lists.append(i)
        return sigma2_lists

    def almost_global_minimum(self):
        sigma2_lists = self.cartesian_produce()
        for sigma2_list in sigma2_lists:
            print(sigma2_list)
            local_min_loss, local_optimal_parameters = self.gradient_descent(sigma2_list)
            if local_min_loss < self.best_loss:
                self.best_loss = local_min_loss
                self.best_parameters = local_optimal_parameters
        return self.best_loss, self.best_parameters

test_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 2, 2, 1, 1, 3, 4, 4, 4, 4, 2, 3, 4, 9, 19, 38, 52, 54, 50, 30, 17, 9, 5, 3, 2, 2, 1, 1, 2, 2, 2, 2, 1, 3, 3, 5, 4, 4, 5, 4, 5, 5, 5, 4, 2, 2, 5, 4, 4, 5, 4, 5, 9, 10, 10, 10, 7, 6, 9, 11, 12, 14, 13, 12, 8, 9, 10, 14, 13, 12, 12, 8, 8, 7, 10, 9, 10, 13, 10, 8, 5, 5, 3, 2, 3, 4, 3, 4, 4, 4, 6, 7, 8, 7, 7, 6, 4, 3, 2, 3, 3, 4, 2, 3, 2, 4, 5, 4, 4, 2, 5, 6, 8, 9, 5, 5, 4, 3, 3, 2, 5, 20, 36, 39, 36, 25, 8, 3, 3, 4, 4, 3, 4, 4, 4, 4, 4, 4, 14, 19, 27, 32, 35, 41, 45, 48, 55, 56, 61, 65, 63, 65, 65, 62, 60, 53, 51, 44, 36, 31, 25, 21, 19, 12, 9, 5, 4, 3, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 220]
peak_index = [100,150,206,234]
reallist = test_list[0:288]

gm = multi_gaussian_model(reallist, peak_index)
best_loss, best_parameter = gm.almost_global_minimum()
print("global minimal loss is ", best_loss)
print("global best parameter is ", best_parameter)
f = gm.fvalue_calculate(best_parameter)

x = range(1,289)
fig = plt.figure()
plt.plot(x,reallist,x,f)
plt.show()









