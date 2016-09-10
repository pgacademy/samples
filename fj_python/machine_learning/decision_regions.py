import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap
from perceptron import Perceptron

def plot_decision_regions(X, y, classifier, resolution=0.02):

  markers = ('s', 'x', 'o', '^', 'v')
  colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')
  cmap = ListedColormap(colors[:len(np.unique(y))])

  # 最終的にx軸とy軸の範囲として使う
  # X[:, 0] は numpy.ndarrayのメソッドで、Xを2次元配列と想定し、
  # X配列全体（:が全体を表す）から、各要素の0番目の要素を抜き出して1次元配列とする
  x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
  x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1

  xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution), np.arange(x2_min, x2_max, resolution))
  Z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
  Z = Z.reshape(xx1.shape)
  #plt.contourf(xx1, xx2, Z, alpha=0.4, cmap=cmap)
  plt.xlim(xx1.min(), xx1.max())
  plt.ylim(xx2.min(), xx2.max())
  for idx, cl in enumerate(np.unique(y)):
    plt.scatter(x=X[y == cl, 0], y=X[y == cl, 1], alpha=0.8, c=cmap(idx), marker=markers[idx], label=cl)






df = pd.read_csv('https://archive.ics.uci.edu/ml/''machine-learning-databases/iris/iris.data',header=None)
print(df.tail())

y = df.iloc[0:100,4].values
y = np.where(y == 'Iris-setosa',-1,1)
X = df.iloc[0:100,[0,2]].values

# http://daemon.ice.uec.ac.jp/~shouno/2012.Programming/NumpyBasic.html
# X は numpy.ndarray オブジェクト

ppn = Perceptron(eta=0.1, n_iter=10)
ppn.fit(X, y)

plot_decision_regions(X, y, classifier=ppn)
plt.xlabel('sepal length [cm]')
plt.ylabel('petal length [cm]')
plt.legend(loc='upper left')
plt.show()

