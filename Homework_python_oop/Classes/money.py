import json
USD = 'USD'
GOLD = 'GOLD'

class Money(object):
    def __init__(self, code, amount):
        self.code = code
        self.amount = amount

    def money_as_dict(self):
        money_as_dict = {
            self.code: self.amount
        }
        return money_as_dict

    def save(self, file_object):
        json.dump(self.money_as_dict(), file_object)

    def load(self, file_object):
        object_as_dict = json.load(file_object)
        self.code = object_as_dict["code"]
        self.amount = object_as_dict["amount"]
        return object_as_dict

    def __str__(self):
        return '{}: {}'.format(self.code, self.amount)

    def __repr__(self):
        return '{}: {}'.format(self.code, self.amount)