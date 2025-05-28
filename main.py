import yfinance as yf
import pandas as pd
import numpy as np


class RollSpreadCalculator:

    def __init__(self, ticker: str):
        self.ticker = ticker

    def calculate_returns(self, price_type: str = 'Close'):
        ticker = yf.Ticker(self.ticker)
        prices = ticker.history(period='2mo', interval='1d')[price_type]
        prices = prices.dropna()
        return np.log(prices / prices.shift(1)).dropna()

    def spread_calculate(self):
        autocov = np.cov(self.calculate_returns()[1:], self.calculate_returns()[:-1])[0, 1]
        return 2 * np.sqrt(-autocov)


if __name__ == '__main__':
    roll_spread = RollSpreadCalculator('MSFT')
    print(roll_spread.spread_calculate())


