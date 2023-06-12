class Account:

  def __init__(self, client, balance):
    self.client = client
    self.balance = balance

  def withdraw(self, value):
    if (self.balance < value or self.balance - value < 0):
      print('Sorry, you dont have enough balance in your account.')
      return

    self.balance -= value
    print(f'New balance: {self.balance}')

  def deposit(self, value):
    self.balance += value
    print(f'New balance: {self.balance}')

  def __str__(self):
    return f'Current balance: {self.balance}'


account = Account('Brook', 0)
account.deposit(200)
account.deposit(200)
account.withdraw(100)
account.withdraw(50)
print(account)
