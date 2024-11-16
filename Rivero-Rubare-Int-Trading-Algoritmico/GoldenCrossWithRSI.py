import math
import backtrader as bt

# Definición del indicador RSI Estocástico
class StochRSI(bt.Indicator):
    lines = ('stochrsi',)
    params = {
        'period': 20
    }

    def __init__(self):
        period = self.params.period
        rsi = bt.indicators.RSI(self.data, period=period)
        maxrsi = bt.indicators.Highest(rsi, period=period)
        minrsi = bt.indicators.Lowest(rsi, period=period)
        self.lines.stochrsi = (rsi - minrsi) / (maxrsi - minrsi)

# Estrategia Golden Cross con RSI Estocástico
class GoldenCrossWithRSI(bt.Strategy):
    params = (('fast', 50), ('slow', 200), ('order_porcentage', 0.95), ('ticker', 'ORCL'), ('rsi_period', 20))

    def __init__(self):
        # Medias móviles para Golden Cross
        self.fast_moving_average = bt.indicators.SMA(
            self.data.close, period=self.params.fast, plotname='SMA 50 Periodos'
        )
        self.slow_moving_average = bt.indicators.SMA(
            self.data.close, period=self.params.slow, plotname='SMA 200 Periodos'
        )
        self.crossover = bt.indicators.CrossOver(self.fast_moving_average, self.slow_moving_average)

        # Indicador RSI Estocástico
        self.stochrsi = StochRSI(self.data, period=self.params.rsi_period)

    def next(self):
        # Condiciones de compra
        if self.position.size == 0: 
            if self.crossover > 0:
                # Condición adicional: verificar RSI Estocástico
                current_stochrsi = self.stochrsi.lines.stochrsi[0]
                if current_stochrsi < 0.3:  # Condición RSI Estocástico para sobreventa
                    amount_to_invest = self.params.order_porcentage * self.broker.cash
                    self.size = math.floor(amount_to_invest / self.data.close)
                    print("Buy {} shares of {} at {}, StochRSI: {}".format(
                        self.size, self.params.ticker, self.data.close[0], current_stochrsi))
                    self.buy(size=self.size)

        # Condiciones de venta
        if self.position.size > 0:
            if self.crossover < 0:
                current_stochrsi = self.stochrsi.lines.stochrsi[0]
                if current_stochrsi > 0.7:  # Condición RSI Estocástico para sobrecompra
                    print("Sell {} shares of {} at {}, StochRSI: {}".format(
                        self.size, self.params.ticker, self.data.close[0], current_stochrsi))
                    self.close()
