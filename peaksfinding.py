'''
input:
    a list of 289 columns, the first 288 items are steps or times.
    the last one is total days.
output:
    index of peaks
'''
import matplotlib.pyplot as plt
def peaksfinding(prior_list):
    original_list = prior_list[0:288]
    print(original_list)
    result_list = []
    for i in range(288):
        if i-12 < 0:
            low_bound = 0
        else:
            low_bound = i-12
        if i+12 > 287:
            high_bound = 287
        else:
            high_bound = i+12
        sublist = original_list[low_bound:high_bound]
        print(i)
        print(sublist)
        print(original_list[i])
        print('-----------------------------------')
        if original_list[i] == max(sublist) and original_list[i]>0:
            result_list.append(i)
    return result_list

    # sort_list = sorted(original_list,reverse=True)
    # print(sort_list)
    # max10 = sort_list[0:10]
    # index_list = []
    # for i in max10:
    #     index_i = original_list.index(i)
    #     index_list.append(index_i)
    # # index_list store the index of max 10 values
    # # put the index of max value into result_list
    # result_list = [index_list[0]]
    # for j in range(1,10):
    #     for i in result_list:
    #         if abs(i - index_list[j]) <= 12:
    #             break
    #     result_list.append(index_list[j])
    # return result_list


test_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 2, 2, 1, 1, 3, 4, 4, 4, 4, 2, 3, 4, 9, 19, 38, 52, 54, 50, 30, 17, 9, 5, 3, 2, 2, 1, 1, 2, 2, 2, 2, 1, 3, 3, 5, 4, 4, 5, 4, 5, 5, 5, 4, 2, 2, 5, 4, 4, 5, 4, 5, 9, 10, 10, 10, 7, 6, 9, 11, 12, 14, 13, 12, 8, 9, 10, 14, 13, 12, 12, 8, 8, 7, 10, 9, 10, 13, 10, 8, 5, 5, 3, 2, 3, 4, 3, 4, 4, 4, 6, 7, 8, 7, 7, 6, 4, 3, 2, 3, 3, 4, 2, 3, 2, 4, 5, 4, 4, 2, 5, 6, 8, 9, 5, 5, 4, 3, 3, 2, 5, 20, 36, 39, 36, 25, 8, 3, 3, 4, 4, 3, 4, 4, 4, 4, 4, 4, 14, 19, 27, 32, 35, 41, 45, 48, 55, 56, 61, 65, 63, 65, 65, 62, 60, 53, 51, 44, 36, 31, 25, 21, 19, 12, 9, 5, 4, 3, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 220]
result = peaksfinding(test_list)
# plt.plot(test_list[0:288])
# plt.show()
print(result)
for i in result:
    print(test_list[i])