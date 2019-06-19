'''

input:
    real list and peak index
output:
    picture of gaussian fitting and parameters
'''
import numpy as np
import math
import matplotlib.pyplot as plt

def loss_calculating(f,real_list):
    # calculate absolute difference between estimated values and real values
    # loss = sum (|f-y|)
    loss = 0
    N = len(real_list)
    for i in range(N):
        loss += abs(f[i]-real_list[i])
    return loss

def initialize_parameter(peak_index, real_list, sigma2_list):
    # initialize alpha, miu and sigma^2
    # alpha = height of peak, miu = index of peak, sigma^2 = 1
    n = len(peak_index)
    parameter_list = np.zeros(3 * n)
    for i in range(n):
        # alpha
        parameter_list[i * 3 + 0] = real_list[peak_index[i]]
        # miu
        parameter_list[i * 3 + 1] = peak_index[i]
        # sigma^2
        parameter_list[i * 3 + 2] = sigma2_list[i]
    return parameter_list

def fvalue_calculate(real_list, parameter_list):
    # calculate estimated values according parameters
    n = int(len(parameter_list)/3)
    N = len(real_list)
    f_list = []
    for j in range(N):
        f = 0
        for i in range(n):
            alpha = parameter_list[i*3+0]
            miu = parameter_list[i*3+1]
            sigma2 = parameter_list[i*3+2]
            f += alpha * math.exp((-(j - miu) ** 2) / (2*sigma2))
        f_list.append(f)
    return f_list


def gradient_calculate(f_list, real_list, parameter_list):
    # calculate gradients for each parameter
    n = int(len(parameter_list)/3)
    N = len(real_list)
    gradient_list = []
    for i in range(n):
        grad_alpha = 0
        grad_miu = 0
        grad_sigma2 = 0
        for j in range(N):
            alpha = parameter_list[i * 3 + 0]
            miu = parameter_list[i * 3 + 1]
            sigma2 = parameter_list[i * 3 + 2]
            grad_alpha += 2*(f_list[j]-real_list[j])*math.exp((-(j-miu)**2)/(2*sigma2))
            grad_miu += 2*(alpha*(j-miu)/sigma2)*(f_list[j]-real_list[j])*math.exp((-(j-miu)**2)/(2*sigma2))
            grad_sigma2 += 2*(alpha*(j-miu)/(2*(sigma2**2)))*(f_list[j]-real_list[j])*math.exp((-(j-miu)**2)/(2*sigma2))
        gradient_list.append(grad_alpha)
        gradient_list.append(grad_miu)
        gradient_list.append(grad_sigma2)
    return gradient_list

def gaussian_model(real_list, peak_index, sigma2):
    # init
    parameter_list = initialize_parameter(peak_index, real_list, sigma2)
    print(len(parameter_list)/3)
    f_list = fvalue_calculate(real_list, parameter_list)
    loss = loss_calculating(f_list, real_list)
    print(loss)
    gradient_list = gradient_calculate(f_list, real_list, parameter_list)
    print("gradient:",gradient_list)
    a = 0.00001
    min_loss = loss
    best_parameter = []
    for times in range(1000):
        new_parameters = []
        for i in range(len(parameter_list)):
            new_parameter = parameter_list[i] + a*gradient_list[i]
            new_parameters.append(new_parameter)
        parameter_list = new_parameters
        f_list = fvalue_calculate(real_list, parameter_list)
        loss_new = loss_calculating(f_list, real_list)
        print("iteration:",times)
        print("loss is ",loss_new)
        if loss_new < min_loss:
            min_loss = loss_new
            best_parameter = parameter_list

        loss = loss_new
        gradient_list = gradient_calculate(f_list, real_list, parameter_list)
        print(gradient_list)
    return min_loss, best_parameter

test_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 2, 2, 1, 1, 3, 4, 4, 4, 4, 2, 3, 4, 9, 19, 38, 52, 54, 50, 30, 17, 9, 5, 3, 2, 2, 1, 1, 2, 2, 2, 2, 1, 3, 3, 5, 4, 4, 5, 4, 5, 5, 5, 4, 2, 2, 5, 4, 4, 5, 4, 5, 9, 10, 10, 10, 7, 6, 9, 11, 12, 14, 13, 12, 8, 9, 10, 14, 13, 12, 12, 8, 8, 7, 10, 9, 10, 13, 10, 8, 5, 5, 3, 2, 3, 4, 3, 4, 4, 4, 6, 7, 8, 7, 7, 6, 4, 3, 2, 3, 3, 4, 2, 3, 2, 4, 5, 4, 4, 2, 5, 6, 8, 9, 5, 5, 4, 3, 3, 2, 5, 20, 36, 39, 36, 25, 8, 3, 3, 4, 4, 3, 4, 4, 4, 4, 4, 4, 14, 19, 27, 32, 35, 41, 45, 48, 55, 56, 61, 65, 63, 65, 65, 62, 60, 53, 51, 44, 36, 31, 25, 21, 19, 12, 9, 5, 4, 3, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 220]
peak_index = [100,144,206,234]
reallist = test_list[0:288]
print(len(reallist))
minloss, p_list = gaussian_model(reallist, peak_index)
f = fvalue_calculate(reallist, p_list)
print(len(f))
print(minloss)

x = range(1,289)
fig = plt.figure()
plt.plot(x,reallist,x,f)
plt.show()









