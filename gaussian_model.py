'''

input:
    prior list and peak index
output:
    picture of gaussian fitting and parameters
'''
import numpy as np
import math

def loss_calculating(f,real_list):
    # calculate absolute difference between estimated values and real values
    # loss = sum (|f-y|)
    loss = 0
    for i in range(288):
        loss += abs(f[i]-real_list[i])
    return loss

def initialize_parameter(peak_index, real_list):
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
        parameter_list[i * 3 + 2] = 1
    return parameter_list

def fvalue_calculate(real_list, parameter_list):
    # calculate estimated values according parameters
    n = len(parameter_list)/3
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
    n = len(parameter_list)/3
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

def gaussian_model(real_list, peak_index):
    # init
    parameter_list = initialize_parameter(peak_index, real_list)
    f_list = fvalue_calculate(real_list, parameter_list)
    loss = loss_calculating(f_list, real_list)
    gradient_list = gradient_calculate(f_list, real_list, parameter_list)
    a = 0.001
    for times in range(1000):
        new_parameters = []
        for i in range(len(parameter_list)):
            new_parameter = parameter_list[i] - a*gradient_list[i]
            new_parameters.append(new_parameter)
        parameter_list = new_parameters
        f_list = fvalue_calculate(real_list, parameter_list)
        loss_new = loss_calculating(f_list, real_list)
        if loss_new > loss:
            return parameter_list
            break
        else:
            loss = loss_new
            gradient_list = gradient_calculate(f_list, real_list, parameter_list)
    return parameter_list









