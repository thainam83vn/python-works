from yahoo_finance import Share
import time
import matplotlib.pyplot as plt
from mylib import dataformat

yahoo = Share('GOOGL')
yahoo = Share('YHOO')

his = yahoo.get_historical('2016-09-27', '2016-09-30')
print(his[0])
matrix = dataformat.objToMatrix(his)
matrix = dataformat.matrixRotate(matrix)
print(matrix)
plt.plot(matrix[0])
#plt.show()


while True:
    data = {
        'code':'YHOO',
        'open':yahoo.get_open(),
        'price':yahoo.get_price(),
        'prev': yahoo.get_prev_close(),
        'volume': yahoo.get_volume(),
        'price_sales': yahoo.get_price_sales(),
        'price_earnings_ratio': yahoo.get_price_earnings_ratio(),
        'price_earnings_growth_ratio': yahoo.get_price_earnings_growth_ratio(),
        'price_book': yahoo.get_price_book(),
        'change': yahoo.get_change(),
        'day_avg':yahoo.get_avg_daily_volume(),
        'day_high':yahoo.get_days_high(),
        'day_low': yahoo.get_days_low(),
        'tradeDateTime':yahoo.get_trade_datetime()

    }
    print(data)
    time.sleep(5)

