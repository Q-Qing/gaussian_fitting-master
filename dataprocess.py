'''
1. drop the duplications
2. clear data which is less than s-3*sigma or larger than s+3*sigma
3. calculate total days of user
4. if total days < 100, return none. (we can not have a good result with little data)
5. the sums of prior are calculated every 100 days
6. return a 2-dimensional list of prior sum

input parameters:
    flag:
        whether to extract 0,1 feature of original data
        if flag = True, we use 0,1 data
        else we use original data
    input_df:
        dataframe of one user
'''
import pandas as pd

class DataProcess():

    def __init__(self, flag, input_df):
        self.flag = flag
        self.dfuser = input_df

    def data_clearning(self, df_clearing):
        print('******************************')
        print('         data clearning       ')
        print('before clearning there are {} rows'.format(df_clearing.shape[0]))
        mean = df_clearing['steps'].mean()
        std = df_clearing['steps'].std()
        step_up = mean + 3 * std
        step_low = mean - 3 * std
        # if step_low < 0:
        #     step_low = 1000
        print(step_low)
        print(step_up)
        df_clearing['steps'].where((df_clearing['steps'] > step_low) & (df_clearing['steps'] < step_up), inplace=True)
        print('mean + 3*sigma = ', step_up)
        print('mean - 3*sigma=', step_low)
        print('after clearning there are {} rows'.format(df_clearing.shape[0]))
        return df_clearing

    def walkingOrNot20minSlot_forclustering(self,df_original):
        rows = df_original.shape[0]
        print(rows)
        df_feature = df_original.copy()
        df_feature.iloc[:, 5:293] = 0
        for i in range(0, rows):
            for j in range(5, 290):  # 20minSlot，四格，最后要预留三位
                Steps20min = (int(df_original.iloc[i, j]) + int(df_original.iloc[i, j + 1])
                              + int(df_original.iloc[i, j + 2]) + int(df_original.iloc[i, j + 3]))

                if (Steps20min > 2000) and (Steps20min < 5000):
                    df_feature.iloc[i, j] = 1
                    df_feature.iloc[i, j + 1] = 1
                    df_feature.iloc[i, j + 2] = 1
                    df_feature.iloc[i, j + 3] = 1
        return df_feature

    def setup(self):
        df_prior = []
        df_user = self.dfuser
        # drop duplicate rows
        df_user = df_user.drop_duplicates(subset=[' date'], keep='first')
        df_user_clearing = self.data_clearning(df_user)
        total_days = df_user_clearing.shape[0]
        if total_days < 100:
            return df_prior
        else:
            peroids = total_days//100
            for index,i in enumerate(range(1,peroids+1)):
                if index == len(range(1,peroids+1))-1:
                    days = total_days
                else:
                    days = i*100
                df_user_days = df_user_clearing.tail(days)

                if self.flag == True:
                    df_user_feature = self.walkingOrNot20minSlot_forclustering(df_user_days)
                    # print(df_user_feature)
                    df_sum = df_user_feature.iloc[:, 5:293].sum()
                else:
                    df_sum = df_user_clearing.iloc[:, 5:293].sum()
                prior_list = df_sum.values.tolist()
                prior_list.append(days)
                print(prior_list)
                df_prior.append(prior_list)

        return df_prior


