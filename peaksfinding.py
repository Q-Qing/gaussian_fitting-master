'''
input:
    a list of 289 columns, the first 288 items are steps or times.
    the last one is total days.
output:
    index of peaks
'''
import matplotlib.pyplot as plt
import statsmodels.api as sm

def peaksfinding(prior_list):

    original_list = prior_list[0:288]
    cycle_list, trend_list = sm.tsa.filters.hpfilter(original_list, 100)
    intermediate_list = []
    for i in trend_list:
        if i < 1:
            i = 0
        else:
            i = round(i, 3)
        intermediate_list.append(i)
    peak_list = []
    valley_list = []
    # algorithm 2
    n = len(trend_list)
    for i in range(1, n-1):
        a = intermediate_list[i]
        if a > intermediate_list[i-1] and a > intermediate_list[i+1]:
            peak_list.append(i)
        if a < intermediate_list[i-1] and a < intermediate_list[i+1]:
            valley_list.append(i)
    return trend_list, intermediate_list, peak_list, valley_list

    """
    # algorithm 1 dropped
    for i in range(288):
        if i-15 < 0:
            low_bound = 0
        else:
            low_bound = i-12
        if i+15 > 287:
            high_bound = 287
        else:
            high_bound = i+12
        sublist = trend_list[low_bound:high_bound]
        print(i)
        print(sublist)
        print(trend_list[i])
        print('-----------------------------------')
        if trend_list[i] == max(sublist) and trend_list[i]>0:
            result_list.append(i)
    return result_list, trend_list
    """




test_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 2, 2, 1, 1, 3, 4, 4, 4, 4, 2, 3, 4, 9, 19, 38, 52, 54, 50, 30, 17, 9, 5, 3, 2, 2, 1, 1, 2, 2, 2, 2, 1, 3, 3, 5, 4, 4, 5, 4, 5, 5, 5, 4, 2, 2, 5, 4, 4, 5, 4, 5, 9, 10, 10, 10, 7, 6, 9, 11, 12, 14, 13, 12, 8, 9, 10, 14, 13, 12, 12, 8, 8, 7, 10, 9, 10, 13, 10, 8, 5, 5, 3, 2, 3, 4, 3, 4, 4, 4, 6, 7, 8, 7, 7, 6, 4, 3, 2, 3, 3, 4, 2, 3, 2, 4, 5, 4, 4, 2, 5, 6, 8, 9, 5, 5, 4, 3, 3, 2, 5, 20, 36, 39, 36, 25, 8, 3, 3, 4, 4, 3, 4, 4, 4, 4, 4, 4, 14, 19, 27, 32, 35, 41, 45, 48, 55, 56, 61, 65, 63, 65, 65, 62, 60, 53, 51, 44, 36, 31, 25, 21, 19, 12, 9, 5, 4, 3, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 220]
t_list2 = [1, 0, 20, 160, 95, 0, 0, 0, 13, 0, 0, 0, 0, 0, 0, 14, 9, 0, 34, 1, 0, 0, 11, 0, 1, 0, 0, 0, 27, 13, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 18, 8, 0, 0, 27, 12, 0, 71, 92, 1, 64, 22, 201, 51, 206, 483, 205, 83, 39, 79, 465, 418, 209, 332, 216, 824, 1142, 1296, 979, 2246, 2941, 2928, 2625, 2823, 3499, 4591, 4798, 4058, 2378, 3514, 3844, 7461, 17228, 29997, 41453, 44592, 43251, 29790, 17137, 10059, 7971, 7464, 6361, 4615, 6822, 6444, 7816, 7986, 8934, 7703, 8849, 11480, 11114, 10245, 10702, 10486, 10539, 10891, 11308, 11816, 10353, 7502, 8144, 8739, 9084, 10232, 10881, 9168, 12875, 18030, 17772, 16021, 13636, 14370, 13112, 12494, 13606, 17510, 20533, 18574, 16158, 16249, 15921, 16994, 15254, 18761, 20886, 23353, 26426, 22675, 21652, 23004, 22451, 19809, 15552, 15622, 12855, 12664, 9414, 9507, 10003, 10257, 9894, 11622, 11012, 12686, 12091, 12540, 10127, 11419, 12540, 12662, 14599, 10508, 8793, 7904, 6868, 8536, 9276, 9986, 8710, 8912, 6224, 7611, 9181, 7042, 7405, 6401, 8598, 8326, 9162, 7810, 7757, 8768, 9484, 8211, 7242, 5446, 8490, 24310, 35665, 43720, 40296, 29736, 12163, 7152, 5821, 7826, 6663, 4169, 4874, 3937, 4323, 5702, 4950, 7440, 11974, 16161, 20627, 23242, 22500, 25885, 28407, 32164, 38526, 39942, 42897, 44139, 43207, 43769, 43795, 43978, 41610, 37563, 34044, 29948, 24196, 20674, 16281, 14721, 12616, 11465, 8648, 4741, 3335, 3801, 3348, 2621, 2615, 2220, 3088, 1893, 1094, 1713, 823, 1186, 642, 293, 545, 967, 794, 645, 381, 135, 487, 358, 300, 324, 202, 0, 162, 268, 238, 63, 0, 4, 0, 20, 74, 8, 0, 0, 0, 220]

ol, t, p, v = peaksfinding(test_list)
print("trend list:", t)
print("peak list:", p)
print("valley list:", v)
plt.plot(ol)
plt.plot(t)
plt.show()

ol2, t2, p2, v2 = peaksfinding(t_list2)
print("trend list:", t2)
print("peak list:", p2)
print("valley list:", v2)
plt.plot(ol2)
plt.plot(t2)
plt.show()

cycle_list, trend_list = sm.tsa.filters.hpfilter(test_list[0:288], 100)
cycle_list2, trend_list2 = sm.tsa.filters.hpfilter(t_list2[0:288], 100)
plt.subplot(211)
plt.plot(test_list[0:288])
plt.plot(trend_list)
plt.subplot(212)
plt.plot(t_list2[0:288])
plt.plot(trend_list2)
plt.show()
