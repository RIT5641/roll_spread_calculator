import yfinance as yf
import pandas as pd
import numpy as np

class RSC:
    def __init__(self, ticker:str) -> None:
        self.ticker = ticker

    def download_yf(self, price_style:str = 'Close') -> pd.DataFrame:
        data = yf.download(self.ticker, period = '1mo', interval = '1d')[price_style]

        #print(data.head())
        return data

    def returns_ticker(self, price_style:str = 'Close') -> pd.DataFrame:
        returns = np.log(self.download_yf()/
                         self.download_yf().shift(1))
        print(returns)
        return returns
    def roll_spread(self)-> float:
        # Actividad mañana
        spread = 1
        return spread
#Indicar lo que quiero que corra de este archivo
if __name__ == "__main__":
    ticker = 'MSFT'
    msft = RSC(ticker)
    msft.download_yf()
    msft.returns_ticker()

