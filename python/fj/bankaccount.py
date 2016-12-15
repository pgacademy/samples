class BankAccount(object):

  def __init__(self):
    self._balance = 0

  @property
  def balance(self):
    return self._balance

  def deposit(self, amount):
    self._balance += amount

  def withdraw(self, amount):
    self._balance -= amount


account = BankAccount()

account.balance

account.deposit(10000)
print account.balance()

