import os
import re

import settings


class MOEXBase:

    def securities(
            self,
            return_type=settings.RETURN_TYPE,
            date=None
    ):
        url = os.path.join(self.url, f'securities.{return_type}')
        if date:
            if not re.match(r'^\d{4}-\d{2}-\d{2}$', date):
                raise ValueError('The right format is: YYYY-MM-DD')
            url += f'?date={date}'
        return url


class MOEXMultiObject(MOEXBase):

    def __init__(self, url: str, name: str = ''):
        self.url = os.path.join(url, name)


class MOEXObject(MOEXBase):
    url = ''
    valid_items = []

    def __init__(self, url, child_item_cls: type = None):
        if not self.url:
            raise NotImplementedError
        self.url = os.path.join(url, self.url)
        for item in self.valid_items:
            setattr(self, item, child_item_cls(self.url, item))


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


class History(MOEXObject):
    url = 'history'

    def __init__(self, url):
        super().__init__(url)
        self.engines = Engine(self.url, child_item_cls=MultiEngineItem)


class MOEX:
    url = 'https://iss.moex.com/iss'
    engines = Engine(url, child_item_cls=MultiEngineItem)
    history = History(url)


m = MOEX()
print(m.engines.securities())
print(m.engines.stock.securities())
print(m.engines.stock.markets.securities(date='2022-03-12'))
print(m.engines.stock.markets.shares.securities())
print(m.history.engines.securities())
print(m.history.engines.stock.securities(return_type='xml'))
print(m.history.engines.stock.markets.securities())
print(m.history.engines.stock.markets.shares.securities(date='2022-03-12'))

