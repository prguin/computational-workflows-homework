# wallet.py

class InsufficientAmount(Exception):
    pass


class Wallet(object):
    def __init__(self, initial_amount=0):
        raise InsufficientAmount


    def spend_cash(self, amount):
        raise InsufficientAmount


    def add_cash(self, amount):
        raise InsufficientAmount
        

