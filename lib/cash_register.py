#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
      self.total = 0
      self.items = []
      self.discount = discount

    def add_item(self, title, price, quantity=1):
      self.total += price * quantity
      self.items.extend([title] * quantity)

    def apply_discount(self):
        if self.discount > 0:
          self.total -= (self.total * self.discount) / 100
          print(f"After the discount, the total comes to ${self.total:.0f}.")
        else:
          print("There is no discount to apply.")

    def void_last_transaction(self):
        if self.items:
          last_item_price = self._get_last_item_price()
          self.total -= last_item_price
          self.items.pop()

    def _get_last_item_price(self):
        title = self.items.pop()
        return self._get_price_by_title(title)

    def _get_price_by_title(self, title):
        item_prices = {}
        return item_prices.get(title, 0)

   




