import pandas
import matplotlib.pyplot as plot
import numpy as np

from matplotlib.pyplot import scatter
from perceptron import Perceptron

frame = pandas.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', header=None)
print(frame.tail())

y = frame.iloc[0:100, 4].values
y = np.where(y == 'Iris-setosa', -1, 1)
X = frame.iloc[0:100, [0, 2]].values
plot.scatter(X[:50,0], X[:50,1], color='red', marker='o', label='setosa')
plot.scatter(X[50:100,0], X[50:100,1], color='blue', marker='x', label='versicolor')
plot.xlabel('sepal length [cm]')
plot.ylabel('petal length [cm]')
plot.legend(loc='upper left')
#plot.show()


ppn = Perceptron(eta=0.1, n_iter=10)
ppn.fit(X, y)

plot.plot(range(1, len(ppn.errors_) + 1), ppn.errors_, marker='o')
plot.xlabel('Epochs')
plot.ylabel('Number of misclassifications')
plot.show()
