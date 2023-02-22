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


class MarketShares(MOEXBase):
    url = 'shares'


class MarketBonds(MOEXBase):
    url = 'bonds'


class MarketIndex(MOEXBase):
    url = 'index'


class Markets(MOEXBase):
    url = 'markets'

    def __init__(self, url):
        super().__init__(url)
        self.shares = MarketShares(self.url)
        self.bonds = MarketBonds(self.url)
        self.index = MarketIndex(self.url)


class EngineFutures(MOEXBase):
    url = 'futures'

    def __init__(self, url):
        super().__init__(url)
        self.markets = Markets(self.url)


class EngineCurrency(MOEXBase):
    url = 'currency'

    def __init__(self, url):
        super().__init__(url)
        self.markets = Markets(self.url)


class EngineStock(MOEXBase):
    url = 'stock'

    def __init__(self, url):
        super().__init__(url)
        self.markets = Markets(self.url)


class Engines(MOEXBase):
    url = 'engines'

    def __init__(self, url):
        super().__init__(url)
        self.stock = EngineStock(self.url)
        self.currency = EngineCurrency(self.url)
        self.futures = EngineFutures(self.url)


class History(MOEXBase):
    url = 'history'

    def __init__(self, url):
        super().__init__(url)
        self.engines = Engines(self.url)


class MOEX:
    url = 'https://iss.moex.com/iss'
    engines = Engines(url)
    history = History(url)

    def index(self, return_type='json'):
        return os.path.join(self.url, f'index.{return_type}')


moex = MOEX()
print(moex.index())
print(moex.engines.securities())
print(moex.engines.stock.securities())
print(moex.engines.stock.markets.securities(date='2022-03-12'))
print(moex.engines.stock.markets.shares.securities())
print(moex.history.engines.securities())
print(moex.history.engines.stock.securities(return_type='xml'))
print(moex.history.engines.stock.markets.securities())
print(moex.history.engines.stock.markets.shares.securities(date='2022-03-12'))

