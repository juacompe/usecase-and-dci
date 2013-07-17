from lettuce import *
from example1_the_core_stuffs import Account, TransferMoney

@step('I have money (\d+) baths')
def i_have_money(step, amount):
    world.my_account = Account(int(amount))

@step('my friend have (\d+) baths')
def you_have_money(step, amount):
    world.friend_account = Account(int(amount))

@step('I transfer money (\d+) baths')
def transfer_money(step, amount):
    src = world.my_account
    dst = world.friend_account
    t = TransferMoney(src, dst)
    t.perform_transfer(int(amount))

@step('I should have (\d+) baths')
def assert_i_have(step, amount):
    msg = 'I have %s' % world.my_account.balance
    assert world.my_account.balance == int(amount), msg 

@step('Then my friend should have (\d+) baths')
def assert_my_friend_has(step, amount):
    msg = 'My friend has %s' % world.friend_account.balance
    assert world.friend_account.balance == int(amount), msg 

