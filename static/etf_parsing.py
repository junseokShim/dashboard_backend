import yfinance as yf
import datetime as dt
import pandas as pd
import numpy as np

def yf_to_df(df, x):
    # S&P 500 2년간 데이터
    stock_data = pd.DataFrame(df.history(start=f"{x.year-5}-{x.month}-{x.day}", end=f"{x.year}-{x.month}-{x.day}"))

    new_stock_df = pd.DataFrame(stock_data.iloc[0:,:].values, columns = stock_data.columns)
    days = np.array(stock_data.index, dtype=np.datetime64)
    new_stock_df.index = [days[i].astype('str')[:10] for i in range(len(days))]
    new_stock_df["MA20"] = new_stock_df['Close'].rolling(window=20).mean()
    new_stock_df["MA60"] = new_stock_df['Close'].rolling(window=60).mean()
    new_stock_df["MA90"] = new_stock_df['Close'].rolling(window=90).mean()
    new_stock_df["MA120"] = new_stock_df['Close'].rolling(window=120).mean()

    data = [{'date': new_stock_df.index[i], \
            'price':new_stock_df['Close'][i], \
            'MA20':new_stock_df["MA20"][i], \
            'MA60':new_stock_df["MA60"][i], \
            'MA90':new_stock_df["MA90"][i], \
            'MA120':new_stock_df["MA120"][i]} \
            for i in range(len(new_stock_df.index))]

    return data


def stock_df(tag):
    x = dt.datetime.now()
    
    # define으로 관리하고 싶은데...
    stock = yf.Ticker(tag)

    df_stock = yf_to_df(stock, x)

    return df_stock