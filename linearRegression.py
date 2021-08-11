# import packages
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_diabetes

# load dataset
d = load_diabetes()
# select features to use from data
d_X = d.data[:, np.newaxis, 2]
# Reserve the last 20 observations for testing and use the rest for training
dx_train = d_X[:-20]
dy_train = d.target[:-20]
dx_test = d_X[-20:]
dy_test = d.target[-20:]
# calculate gradient
m = (np.mean(dx_train.squeeze()) * np.mean(dy_train) - np.mean(dx_train.squeeze() * dy_train)) / \
    ((np.mean(dx_train.squeeze())) ** 2 - np.mean(dx_train.squeeze() ** 2))
# calculate y intercept
b = np.mean(dy_train) - m * np.mean(dx_train.squeeze())
# set x to array of x values
x = dx_train
# create a function for y
y = m * x + b
# plot training data, testing data and line of best-fit in set color with labels
plt.scatter(dx_train, dy_train, c='r', label='training data')
plt.scatter(dx_test, dy_test, c='g', label='testing data')
plt.plot(x, y, c='b', label='line of best-fit')
# get legend for graph
plt.legend()
# show graph
plt.show()
