import talib as ta
import numpy as np

class TechnicalIndicators:
    def __init__(self, data):
        self.DATA = np.array(data[::-1])  # Reverse the data once during initialization

    # get the last value from the 'DATA' variable
    def get_last_value(self):
        return self.DATA[-1]

    # Indicators
    def moving_average(self, period):
        return ta.SMA(self.DATA, timeperiod=period)

    def exponential_moving_average(self, period):
        return ta.EMA(self.DATA, timeperiod=period)

    def bollinger_bands(self, period, nbdevup, nbdevdn):
        upper, middle, lower = ta.BBANDS(self.DATA, timeperiod=period, nbdevup=nbdevup, nbdevdn=nbdevdn)
        return upper, middle, lower

    def relative_strength_index(self, period):
        return ta.RSI(self.DATA, timeperiod=period)

    def moving_average_convergence_divergence(self, fast_period, slow_period, signal_period):
        macd, signal, _ = ta.MACD(self.DATA, fastperiod=fast_period, slowperiod=slow_period, signalperiod=signal_period)
        return macd, signal

    def stochastic_oscillator(self, k_period, d_period):
        slowk, slowd = ta.STOCH(self.DATA, fastk_period=k_period, slowk_period=d_period, slowd_period=d_period)
        return slowk, slowd

    def average_true_range(self, period):
        return ta.ATR(self.DATA, timeperiod=period)

    def commodity_channel_index(self, period):
        return ta.CCI(self.DATA, timeperiod=period)

    def parabolic_sar(self, acceleration, maximum):
        return ta.SAR(self.DATA, acceleration=acceleration, maximum=maximum)

    def average_directional_index(self, period):
        return ta.ADX(self.DATA, timeperiod=period)

    def on_balance_volume(self):
        return ta.OBV(self.DATA)

    def chaikin_money_flow(self, period):
        return ta.ADOSC(self.DATA, fastperiod=period)

    def williams_percent_range(self, period):
        return ta.WILLR(self.DATA, timeperiod=period)

    def average_price(self):
        return ta.AVGPRICE(self.DATA)

    def triple_exponential_moving_average(self, period):
        return ta.TEMA(self.DATA, timeperiod=period)

    def rate_of_change(self, period):
        return ta.ROC(self.DATA, timeperiod=period)



if __name__ == "__main__":

    # Your dataset, maybe it can come from an API, or .csv file.
    DATASET=None

    tech_indicators = TechnicalIndicators(DATASET)

    # MA 10
    ma_value = tech_indicators.moving_average(10)
    print(f"Moving Average {ma_value=}")

    # RSI 14
    rsi_value = tech_indicators.relative_strength_index(14)
    print(f"RSI {rsi_value=}")

    # Bollinger Bands 20,2,2
    upper_band, middle_band, lower_band = tech_indicators.bollinger_bands(20, 2, 2)
    print(f"Bollinger Bands (20, 2, 2): {upper_band=}, {middle_band=}, {lower_band=}")


