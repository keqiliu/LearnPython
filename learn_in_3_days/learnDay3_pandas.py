import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like  # to fix panda_datareader is_list_like error
import pandas_datareader.data as web
import datetime
import os.path
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as statsm
import scipy.stats as scs

# it's all about pandas!
# data frame

df = pd.DataFrame(list(map(list, zip(*[[10, 20, 30, 40], [1, 2, 3, 4]]))),
                  columns=['Numbers', 'another'],
                  index=['a', 'b', 'c', 'd'])
print(df.index)
print(df.columns)
print(df.ix['c'])
print(df.ix[['a', 'c']])  # must use [] to include multi columns
print(df.ix[df.index[1:3]])
print(df.sum())
ts = df ** 2
print(ts)

df['floats'] = (1.5, 2., 3.1, 4.3)  # add new column
df['names'] = pd.DataFrame(['Dan', 'Ban', 'Bu', 'Noo'],
                           index=['d', 'c', 'a', 'b'])  # add according to index
print(df)
df = df.append(pd.DataFrame({'numbers': 666, 'floats': 5.5, 'names': 'aha'},
                            index=['y']))
print(df)
df = df.drop(columns=['numbers'])
print(df)
df.set_value('y', 'Numbers', 666)  # update value
print(df)

# df.append or drop, does not change original value, has to be df = df.something

df.join(pd.DataFrame([1, 5, 8, 13, 15],
                     index=['a', 'b', 'c', 'd', 'e'],
                     columns=['not_square']), how='outer')  # inner, left, right


# stock price!
temp_file = 'apple.pkl'
if not os.path.isfile(temp_file):
    # start = datetime.datetime(2017, 1, 1)
    end = datetime.datetime.now()
    f = web.DataReader('AAPL', 'robinhood')
    f.to_pickle(temp_file)
else:
    f = pd.read_pickle(temp_file)

print(f.info())
print(f.head())
print(f.tail())
print(f.columns)

# convert string to numerical!!!
f = f.drop(columns=['session'])
f = f.astype(float)

# f.plot(y=['open_price','close_price'], grid=True, figsize=(8, 6), kind='line')
f['close_price'].plot(grid=True, figsize=(8, 6))
plt.show()

f['log_return'] = np.log(f['close_price']/f['close_price'].shift(1))
f['log_return'].plot(grid=True, figsize=(8, 6))
plt.show()

f[['close_price', 'log_return']].plot(subplots=True, style='b-',
                                      figsize=(8, 6), grid=True)
plt.show()

f['ma_1month'] = f['close_price'].rolling(21).mean()
f['ma_1qtr'] = f['close_price'].rolling(63).mean()
f[['close_price', 'ma_1month', 'ma_1qtr']].plot(figsize=(8, 6), grid=True)
plt.show()

f['vol_monthly'] = f['log_return'].rolling(21).std()
f['vol_monthly'].plot(grid=True, figsize=(8, 6))
plt.show()

f['log_return'].hist(bins=20, figsize=(8, 6))
plt.show()

statsm.qqplot(f['log_return'].dropna(), line='s')
plt.grid(True)
plt.xlabel('Theoretical quantiles')
plt.ylabel('Sample quantiles')
plt.show()

# skew and kurtosis
data = f['log_return'].dropna()
print('Skew is', scs.skew(data))
print('Skew test p-value is', scs.skewtest(data)[1])

print('Kurt is', scs.kurtosis(data))
print('Kurt test p-value is', scs.kurtosistest(data)[1])


# best-possible profit
l = list(f['close_price'])
l1 = l.copy()
l1.reverse()
l += l1
plt.plot(l)
plt.show()

low = l[0]
high = l[0]
profit = high - low
for i in range(1, len(l)):
    if l[i] < low:
        low = l[i]
        print('new low at idx = ', i)
    elif l[i] > high:
        high = l[i]
        print('new high at idx = ', i)
    if l.index(high) > l.index(low) and high - low > profit:
        profit = high - low
        print('new chance:', profit)
