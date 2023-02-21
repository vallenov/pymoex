import os

import settings


class MOEXMultiObject:

    def __init__(self, url: str, name: str = ''):
        self.url = os.path.join(url, name)

    def securities(self, return_type=settings.RETURN_TYPE):
        return os.path.join(self.url, f'securities.{return_type}')


class MOEXObject:
    url = ''
    valid_items = []

    def __init__(self, url, child_item_cls: type):
        if not self.url or not self.valid_items:
            raise NotImplementedError
        self.url = os.path.join(url, self.url)
        for item in self.valid_items:
            setattr(self, item, child_item_cls(self.url, item))

    def securities(self, return_type=settings.RETURN_TYPE):
        return os.path.join(self.url, f'securities.{return_type}')


class MultiMarketItem(MOEXMultiObject):
    ...


class Market(MOEXObject):
    url = 'markets'
    valid_items = ['shares', 'bonds', 'index']


class MultiEngineItem(MOEXMultiObject):

    def __init__(self, url, name):
        super().__init__(url, name)
        self.markets = Market(self.url, child_item_cls=MultiMarketItem)


class Engine(MOEXObject):
    url = 'engines'
    valid_items = ['stock', 'currency', 'futures']


class MOEX:
    url = 'https://iss.moex.com/iss'
    engines = Engine(url, child_item_cls=MultiEngineItem)


m = MOEX()
print(m.engines.securities(return_type='json'))
print(m.engines.stock.securities(return_type='json'))
print(m.engines.stock.markets.securities(return_type='json'))
print(m.engines.stock.markets.shares.securities(return_type='json'))

