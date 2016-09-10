import numpy as np

class Perceptron(object):

  """パーセプトロンの分類器

  パラメータ
  -----------
  eta: float 学習率（0.0より大きく1.0以下の値）
  n_iter: int トレーニングデータのトレーニング回数

  属性
  w_: 1次元配列 適用後の重み
  errors_: リスト 各エポックでの誤分類数

  """

  def __init__(self, eta=0.01, n_iter = 10):
    self.eta = eta
    self.n_iter = n_iter

  def fit(self, X, y):

    """
    トレーニングデータに適合させる
    ----------
    パラメータ
    X: {配列のようなデータ構造}, shape = [n_samples, n_features]
    トレーニングデータ。n_sampleはサンプルの個数、n_featuresは特徴量の個数
    y: {配列のようなデータ構造}, shape = [n_samples]
    目的変数

    戻り値
    ----------
    self: objct
    """

    # 特徴量の個数+1の長さの0埋めした配列
    # つまりこの場合長さ3
    self.w_ = np.zeros(1 + X.shape[1])

    self.errors_ = []

    # トレーニング回数分トレーニングデータを反復
    for _ in range(self.n_iter):
      errors = 0

      # 各サンプルで重みを更新
      # zipは2つのシーケンスから、タプルのシーケンスを作る
      # zip([1,2,3], ["a", "b", "c"]) => [(1,"a"),(2,"b"),(3,"c")]
      # そのタプルを xi, target で受けているのだから、Xとyを同時にループしてる
      for xi, target in zip(X, y):

        # 重み w1, ... wm の更新
        # Δwj = η(y(i) - y(i))xj(i)(j = 1, ..., m)
        update = self.eta * (target - self.predict(xi))
        self.w_[1:] += update * xi
        self.w_[0] += update

        errors += int(update != 0.0)

      self.errors_.append(errors)

    return self

  def net_input(self, X):
    #print("X={}, self.w_={}".format(X, self.w_))
    return np.dot(X, self.w_[1:]) + self.w_[0]

  def predict(self, X):
    return np.where(self.net_input(X) >= 0.0, 1, -1)







