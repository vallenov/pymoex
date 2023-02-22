import os
import re
import json

import settings
from helpers import regular_request


class MOEXBase:
    url = ''

    def __init__(self, url=''):
        if not self.url:
            raise ValueError('url is empty')
        self.url = os.path.join(url, self.url)

    def __repr__(self):
        return f'{self.__class__}'

    @staticmethod
    def _for_normal_dict(text: str) -> dict:
        normal_dict = {}
        raw_dict: dict = json.loads(text)
        for key, val in raw_dict.items():
            if key == 'metadata':
                continue
            low_vals = [low.lower() for low in val['columns']]
            normal_dict[key] = []
            for data in val['data']:
                row = dict(zip(low_vals, data))
                normal_dict[key].append(row)
        return normal_dict

    def _make_request(self, url):
        result = regular_request(url)
        if result.status_code == 200:
            data = self._for_normal_dict(result.text)
        else:
            data = {}
        return {
            'data': data,
            'metadata': {
                'code': result.status_code,
                'message': result.reason
            }
        }

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
        return self._make_request(url)


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


class MOEX(MOEXBase):
    url = 'https://iss.moex.com/iss'
    engines = Engines(url)
    history = History(url)

    def index(self, return_type='json'):
        url = os.path.join(self.url, f'index.{return_type}')
        return self._make_request(url)


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

