from abc import ABC, abstractmethod

class MenuItem(ABC):
    def __init__(self, name, base_price):
        self.name = name
        self.base_price = base_price

    @abstractmethod

    def calculatePrice(self):
        pass

# class Meet(MenuItem):
#     def calculatePrice(self):
#         return self.base_price


class Order():
    def __init__(self):
        self.__items = []
        self.__status = 'new'

    def nextStep(self):
        if self.__status == 'new':
            self.__status = 'in process'
        elif self.__status == 'in process':
            self.__status = 'delivery'
        elif self.__status == 'delivery':
            self.__status = 'done'
        else:
            print('order_done')

    def addItem(self, item):
        if self.__status not in ['in process', 'delivery', 'done']:
            self.__items.append(item)
            print('добавил')
        else:
            print('нельзя добавить блюдо в уже готовящийся заказ')

    def getTotalCost(self):
        receipt = 0
        for item in self.__items:
            receipt += item.calculatePrice()
        return receipt

    def pay(self, payment_method):
        itog = self.getTotalCost()
        print(f'К оплате {itog}')
        payment_method.collectPayment(itog)



class Pizza(MenuItem):
    def __init__(self, name, base_price, size):
        super().__init__(name, base_price)
        self.size = size

    def calculatePrice(self):
        price = 0
        if self.size == 'large':
            price = self.base_price * 1.3
        else:
            price = self.base_price
        return price

class Drink(MenuItem):
    def __init__(self, name, base_price, isIce):
        super().__init__(name, base_price)
        self.isIce = isIce

    def calculatePrice(self):
        return self.base_price
    
    def __str__(self):
        if self.isIce == 'Со льдом':
            return f'{self.name} со льдом'
        else:
            return self.name


class ComboSet(MenuItem):
    def __init__(self, name, base_price):
        super().__init__(name, 0)
        self.__items = []

    def addItem(self, item):
        self.__items.append(item)

    def calculatePrice(self):
        cash = 0

        for item in self.__items:
            cash += item.calculatePrice()
        return cash * 0.85

class PaymentStrategy(ABC):
    @abstractmethod
    def collectPayment(self, amount: float):
        pass

class CardPayment(PaymentStrategy):
    def __init__(self, data):
        super().__init__()
        self.data = data

    def collectPayment(self, amount):
        if self.data >= 2026:
            print(f'списано {amount} с карты')
        else:
            return (f'перевыпустите карту, сейчас 2026, ваша карта {self.data} года')

class CashPayment(PaymentStrategy):
    def collectPayment(self, amount):
        return 'Все четко, оплата'
