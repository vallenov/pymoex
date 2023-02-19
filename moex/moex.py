import os


class MultiMarketItem:

    def __init__(self, url, name):
        self.url = os.path.join(url, name)

    def securities(self, return_type):
        return os.path.join(self.url, f'securities.{return_type}')


class Market:
    url = 'markets'
    valid_markets = ['shares', 'bonds', 'index']

    def __init__(self, url):
        self.url = os.path.join(url, Market.url)
        for market in Market.valid_markets:
            setattr(self, market, MultiMarketItem(self.url, market))

    def securities(self, return_type):
        return os.path.join(self.url, f'securities.{return_type}')


class MultiEngineItem:

    def __init__(self, url, name):
        self.url = os.path.join(url, name)
        self.markets = Market(self.url)

    def securities(self, return_type):
        return os.path.join(self.url, f'securities.{return_type}')


class Engine:
    url = 'engines'
    valid_engines = ['stock', 'currency', 'futures']

    def __init__(self, url):
        self.url = os.path.join(url, Engine.url)
        for engine in Engine.valid_engines:
            setattr(self, engine, MultiEngineItem(self.url, engine))

    def securities(self, return_type):
        return os.path.join(self.url, f'securities.{return_type}')


class MOEX:
    url = 'https://iss.moex.com/iss'
    engines = Engine(url)


m = MOEX()
print(m.engines.securities(return_type='json'))
print(m.engines.stock.securities(return_type='json'))
print(m.engines.stock.markets.securities(return_type='json'))
print(m.engines.stock.markets.shares.securities(return_type='json'))

