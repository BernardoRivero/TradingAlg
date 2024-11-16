from __future__ import (absolute_import, division, print_function, unicode_literals)
import datetime
from GoldenCross import GoldenCross
import backtrader as bt 
from GoldenCrossWithRSI import GoldenCrossWithRSI
from StochRSI import StochRSIStrategy
from BuyOnHammer import BuyOnHammer

if __name__ == '__main__':
    cerebro = bt.Cerebro()

dataMSFT = bt.feeds.YahooFinanceCSVData(
    dataname = 'MSFT.csv',
    #do not pass values before this date
    fromdate = datetime.datetime(2020,11,11),
    #do not pass values after this date
    todate= datetime.datetime(2024,11,11),
    reverse = False
)

dataMETA = bt.feeds.YahooFinanceCSVData(
    dataname = 'META.csv',
    #do not pass values before this date
    fromdate = datetime.datetime(2020,11,11),
    #do not pass values after this date
    todate= datetime.datetime(2024,11,11),
    reverse = False
)

dataIBM = bt.feeds.YahooFinanceCSVData(
    dataname = 'IBM.csv',
    #do not pass values before this date
    fromdate = datetime.datetime(2020,11,11),
    #do not pass values after this date
    todate= datetime.datetime(2024,11,11),
    reverse = False
)


dataGOOGL = bt.feeds.YahooFinanceCSVData(
    dataname = 'GOOGL.csv',
    #do not pass values before this date
    fromdate = datetime.datetime(2020,11,11),
    #do not pass values after this date
    todate= datetime.datetime(2024,11,11),
    reverse = False
)

dataAAPL = bt.feeds.YahooFinanceCSVData(
    dataname = 'AAPL.csv',
    #do not pass values before this date
    fromdate = datetime.datetime(2020,11,11),
    #do not pass values after this date
    todate= datetime.datetime(2024,11,11),
    reverse = False
)

dataORCL = bt.feeds.YahooFinanceCSVData(
    dataname = 'ORCL.csv',
    #do not pass values before this date
    fromdate = datetime.datetime(2020,11,11),
    #do not pass values after this date
    todate= datetime.datetime(2024,11,11),
    reverse = False
)


def run():
    cerebro = bt.Cerebro()
    cerebro.broker.setcash(10000.0)
    saldoInicial = cerebro.broker.getvalue()
    print('Saldo Inicial: %.2f' % saldoInicial)

    cerebro.adddata(dataORCL)
    cerebro.addstrategy(GoldenCrossWithRSI)


    cerebro.broker.setcommission(commission=0.001)
    cerebro.run()

    saldoFinal= cerebro.broker.getvalue()
    print('Saldo Final: %.2f' % saldoFinal)

    saldoFinal=  (saldoFinal*100/saldoInicial)-100
    print('Porcentaje de ganancias: %.2f' % saldoFinal)
    cerebro.plot()

    

run()