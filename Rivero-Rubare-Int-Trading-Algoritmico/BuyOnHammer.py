import backtrader as bt

# Definir el patrón de martillo como un indicador
class HammerPattern(bt.Indicator):
    lines = ('hammer',)

    def __init__(self):
        pass

    def next(self):
        # Obtener precios de la vela actual
        open_price = self.data.open[0]
        close_price = self.data.close[0]
        low_price = self.data.low[0]
        high_price = self.data.high[0]

        # Calcular las longitudes del cuerpo y las mechas
        body = abs(close_price - open_price)
        candle_range = high_price - low_price
        lower_wick = low_price - min(open_price, close_price)
        
        # El cuerpo debe ser pequeño (menos del 30% del rango total)
        # La mecha inferior debe ser al menos dos veces el tamaño del cuerpo
        if body < candle_range * 0.3 and lower_wick > body * 2:
            self.lines.hammer[0] = 1  # Martillo detectado
        else:
            self.lines.hammer[0] = 0  # No es martillo

# Estrategia para comprar cuando aparece el patrón de martillo y el RSI está por debajo de 30
class BuyOnHammer(bt.Strategy):
    params = (
        ('rsi_period', 14),  # El período para el RSI
    )

    def __init__(self):
        # Inicializar el indicador de martillo
        self.hammer = HammerPattern(self.data)
        # Inicializar el indicador RSI
        self.rsi = bt.indicators.RSI(self.data, period=self.params.rsi_period)

    def next(self):
        # Comprobar si el RSI está por debajo de 30 (condición de sobreventa)
        # y si el patrón de martillo está presente
        if self.rsi[0] < 30 and self.hammer[0] == 1:
            self.buy()  # Comprar cuando ambas condiciones se cumplen
            print(f"Compra en {self.data.datetime.datetime(0)}")
