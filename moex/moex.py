import os
import re

import settings


class MOEXBase:
    url = ''

    def __init__(self, url):
        if not self.url:
            raise ValueError('url is need to be fit')
        self.url = os.path.join(url, self.url)

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


class Shares(MOEXBase):
    url = 'shares'


class Bonds(MOEXBase):
    url = 'bonds'


class Index(MOEXBase):
    url = 'index'


class Markets(MOEXBase):
    url = 'markets'

    def __init__(self, url):
        super().__init__(url)
        self.shares = Shares(self.url)
        self.bonds = Bonds(self.url)
        self.index = Index(self.url)


class Futures(MOEXBase):
    url = 'futures'

    def __init__(self, url):
        super().__init__(url)
        self.markets = Markets(self.url)


class Currency(MOEXBase):
    url = 'currency'

    def __init__(self, url):
        super().__init__(url)
        self.markets = Markets(self.url)


class Stock(MOEXBase):
    url = 'stock'

    def __init__(self, url):
        super().__init__(url)
        self.markets = Markets(self.url)


class Engine(MOEXBase):
    url = 'engines'

    def __init__(self, url):
        super().__init__(url)
        self.stock = Stock(self.url)
        self.currency = Currency(self.url)


class History(MOEXBase):
    url = 'history'

    def __init__(self, url):
        super().__init__(url)
        self.engines = Engine(self.url)


class MOEX:
    url = 'https://iss.moex.com/iss'
    engines = Engine(url)
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

