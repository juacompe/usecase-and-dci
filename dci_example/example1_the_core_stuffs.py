from roles import RoleType
from roles.context import context

# Models
class Account(object):

    def __init__(self, amount):
        print "Creating a new account with balance of " + str(amount)
        self.balance = amount
        super(Account, self).__init__()

    def withdraw(self, amount):
        print "Withdraw " + str(amount) + " from " + str(self)
        self.balance -= amount

    def deposit(self, amount):
        print "Deposit " + str(amount) + " in " + str(self)
        self.balance += amount

# Roles
class MoneySource(object):
    __metaclass__ = RoleType

    def transfer(self, amount):
        if self.balance >= amount:
            self.withdraw(amount)
            context.sink.receive(amount)

class MoneySink(object):
    __metaclass__ = RoleType

    def receive(self, amount):
        self.deposit(amount)

# Context
class TransferMoney(object):

    def __init__(self, source, sink):
        self.source = source
        self.sink = sink
        roles = {
            'source': MoneySource,
            'sink': MoneySink,
        }
        self.transfer_context = context(self, **roles)

    def perform_transfer(self, amount):
        with self.transfer_context as ctx:
            ctx.source.transfer(amount)


src = Account(1000)
dst = Account(0)

t = TransferMoney(src, dst)
t.perform_transfer(100)

print src, src.balance
assert src.balance == 900
print dst, dst.balance
assert dst.balance == 100

