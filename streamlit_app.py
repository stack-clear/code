import time
import streamlit as st
import numpy as np
import pandas as pd


from matplotlib.ticker import MultipleLocator
import datetime as dt
import math
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import mplfinance as mpf
import yfinance as yf

st.title("Stitch's World")

#st.write("My first dataframe")
#df = pd.DataFrame({
#    'first':[1, 2, 3, 4],
#    'second':[10, 20, 30, 40]
#    })
#df

#option = st.selectbox("What is your fav stock?", ["TSLA", "AAPL", "AMZN"])
#"Your choice", option

title1 = st.text_input('Stock name', 'SPY')
title2 = st.text_input('Date (YYMMDD)', 220815)

mc = mpf.make_marketcolors(up='g',down='r',
                           edge='inherit',
                           wick='inherit',
                           volume={'up':'#BFDDBF', 'down':'#FEBFBF'},
                           ohlc='inherit')

s  = mpf.make_mpf_style(marketcolors=mc, edgecolor='white')
wconfig = {'candle_linewidth': .9}


def prepare_chart(data, sd, ed, sma_lab, highlight_dates, plot_title, pic_name, date_lines = None):
    
    data = data.loc[sd:ed,:].copy()
    data['Volume'] = data['Volume']/1000000
    where_values = [True if date in highlight_dates else False for date in data.index]
    apdict = mpf.make_addplot(data[sma_lab])
    
    try:
        fig, axlist = mpf.plot(data, style=s, type='candle', volume=True, figratio=(20,10),
             fill_between=dict(y1=min(data['Low']), y2=max(data['High']), where = where_values,alpha=0,color='y'),
             tight_layout=True, datetime_format=' %Y-%m-%d', 
                               addplot=apdict, 
                               xrotation=90, returnfig=True,
                              figsize = (9,10), update_width_config=wconfig,
                               ylabel_lower='Volume in millions')
        # vlines = dict(vlines=date_lines, linestyle='dotted', alpha=.3)
        axlist[0].xaxis.set_major_locator(MultipleLocator(7))
        axlist[0].xaxis.set_minor_locator(mdates.DayLocator())
        axlist[0].legend(sma_lab,loc=2)
        axlist[0].set_title(plot_title)
        #axlist[1].set_ylabel('Volume in millions')

        #fig.savefig(pic_name, bbox_inches = "tight", dpi=600)
        st.pyplot(fig)
        plt.close()
        del data
    except:
        pass

def get_data(symbol, ed, ext_days = 0, sma = [20, 50, 200]):
    ticker = yf.Ticker(symbol)
    ed_one = ed + dt.timedelta(days = 1) # yahoo finance does not return data for the end date
    sd = ed_one - dt.timedelta(days = 250)
    adj_start = sd + dt.timedelta(days = ext_days)
    adj_end = ed_one + dt.timedelta(days = ext_days)
    
    data = ticker.history(interval='1d', start=sd - dt.timedelta(300), end=adj_end, actions=False, 
                              auto_adjust=True, prepost = False, back_adjust=False) # get another 300 days to plot 200 SMA
    
    if len(data) == 0:
        return None, None
    sma_lab = []
    for v in sma:
        lab = str(v) + ' SMA'; data[lab] = data['Close'].rolling(v).mean(); sma_lab.append(lab)

    highlight_dates = list(data[:ed].index)[-3:]

    plot_title = '\n{}, {} to {}'.format(symbol.upper(), sd.date(), ed.date())
    pic_name = 'pics/{}_{}{}{}'.format(symbol, ed.year, ed.month, ed.day)
    pic1 = prepare_chart(data, adj_start, adj_end, sma_lab, highlight_dates, plot_title, pic_name+'.jpg')
    
    del data
    return pic1


def name_gen(row):
    tic = row['ticker'].upper()
    year = int(row['year'])
    month = str(int(row['month'])).zfill(2)
    day = str(int(row['day'])).zfill(2)
    return '{} {}-{}-{}'.format(tic, year, month, day)

year = int(title2[:2])+2000
month = int(title2[2:4])
day = int(title2[-2:])
ed = dt.datetime(year,month,day)
get_data(title1, ed, ext_days = 0, sma = [10, 20, 50])
