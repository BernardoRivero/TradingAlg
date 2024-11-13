from __future__ import (absolute_import, division, print_function, unicode_literals)
import datetime
from GoldenCross import GoldenCross
import backtrader as bt 
from StochRSI import StochRSI
from BuyOnHammer import BuyOnHammer

if __name__ == '__main__':
    cerebro = bt.Cerebro()

dataCAKE = bt.feeds.YahooFinanceCSVData(
    dataname = 'MSFT_data.csv',
    #do not pass values before this date
    fromdate = datetime.datetime(2023,11,13),
    #do not pass values after this date
    todate= datetime.datetime(2024,11,11),
    reverse = False
)

dataORCL = bt.feeds.YahooFinanceCSVData(
    dataname = 'ORCL_data.csv',
    #do not pass values before this date
    fromdate = datetime.datetime(2023,11,13),
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
    #cerebro.addstrategy(StochRSI)
    #cerebro.addstrategy(GoldenCross)
    cerebro.addstrategy(BuyOnHammer)


    cerebro.broker.setcommission(commission=0.001)
    cerebro.run()

    saldoFinal= cerebro.broker.getvalue()
    print('Saldo Final: %.2f' % saldoFinal)

    saldoFinal=  (saldoFinal*100/saldoInicial)-100
    print('Porcentaje de ganancias: %.2f' % saldoFinal)
    cerebro.plot()

    

run()