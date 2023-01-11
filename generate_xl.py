import time
import datetime
import pandas as pd


def get_fx_xl(period1, period2, ticker):
    interval = '1d'

    query_string = f'https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={period1}&period2={period2}&interval={interval}&events=history&includeAdjustedClose=true'

    df = pd.read_csv(query_string)
    dt = pd.to_datetime(df['Date'], format='%Y/%m/%d')
    df['Date'] = (dt.apply(lambda x: x.strftime('%d/%m/%Y')))
    df.to_excel(f'{ticker} - Daily Share Price.xlsx', index=False)

    return None

ticker1 = 'HEIT.L'
ticker2 = 'HEIC.L'
period1 = int(time.mktime(datetime.datetime(2022, 12, 11, 23, 59).timetuple()))
period2 = int(time.mktime(datetime.datetime(2023, 1, 11, 23, 59).timetuple()))
# get_fx_xl(period1, period2, ticker1)
get_fx_xl(period1, period2, ticker2)



# sharepoint upload didnt work
# just upload manually after altering period