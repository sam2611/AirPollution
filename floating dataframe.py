import pandas as pd
import numpy as np

ser = pd.Series(np.random.rand(34))  # to print series
print(ser)
d_f = pd.DataFrame(np.random.rand(10, 5), index=np.arange(10))  # to make a dataframe of floating values
print(d_f)
d_f.to_csv('floating dataframe.csv')  # creating a csv file for the floating valuse
d_f[0][0] = 0.111111

print("\n", type(d_f))  # object type data frame
print(type(ser))  # object type series
print(d_f.dtypes)  # all are float

# d_f[0][0] = 'sakshi'  # [0][0] index becomes of object type
print("\n", d_f.dtypes)
print(d_f.index)

print("\n", d_f.columns)  # tells about columns
print(d_f.to_numpy())  # convert to an array
print(d_f.T)  # gives the transpose
# print(d_f.sort_index(axis=0, ascending=False))  # sort rows(axis=0) in descending order
# print(d_f.sort_index(axis=1, ascending=False))  # sort columns(axis=1) in descending order
print(d_f[0])
print(type(d_f[0]))
# d_f2 = d_f  # this does not copy it only makes d_f2 to point at the same location where d_f points
# d_f2[0][0] = 'mishra'  # changing value of d_f2 will change the  value of d_f to avoid this **
# print(d_f)  # printing d_f will also show changed value of [0][0] because d_f2 points to same memory
# d_f2 = d_f.copy()  # this copies the value of d_f into d_f2
# d_f2[0][0] = 'mishra'  # now when we change value in d_f2 it doesn't changes d_f
# print(d_f)
d_f.columns = list("ABCDE")
print(d_f)
d_f.loc[0, 0] = 'mishra'
print(d_f)
# d_f.loc[0, 'A'] = 'mishra'
# print(d_f)
d_f = d_f.drop(0, axis=1)  # removes 0 from column i.e (axis=1)
print(d_f)
print(d_f.loc[[1, 2], ['C', 'D']])  # this doesn't changes the d_f only prints a part of it
print(d_f.loc[:, ['C', 'D']])  # for all rows and C D column
print(d_f.loc[[1, 2], :])  # for all column and 1 2 rows
print(d_f.loc[(d_f['A'] < 0.3)])  # returns all the rows in which in column A the value is less then 0.3
print("\n", d_f.iloc[0, 4])  # prints value at index 0,4
print("\n", d_f.iloc[[0, 1], [1, 2]])  # with iloc we can use index numbers but with loc we need to give name of rows
# or column if any
# d_f.drop(['A', 'B'], axis=1, inplace=True)  # inplace replaces the d_f with the mentioned columns
# print(d_f)  # original is modified
d_f.drop([0, 2, 4], axis=0, inplace=True)
print("\n", d_f)
# Now to reset the index of rows we need to do this:-
print("\n", d_f.reset_index())  # but it adds other column named index if we don't want that
d_f.reset_index(drop=True, inplace=True) # we can do this
print("\n", d_f)
