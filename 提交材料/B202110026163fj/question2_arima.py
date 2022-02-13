import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from scipy import stats
from statsmodels.graphics.api import qqplot
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from pmdarima.arima import auto_arima
from sklearn.metrics import mean_squared_error

beijing_data = pd.read_excel(r'.\data\processed_beijing.xlsx', index_col=0, skiprows=0)
dalian_data = pd.read_excel(r'.\data\processed_dalian.xlsx', index_col=0, skiprows=0)
guangzhou_data = pd.read_excel(r'.\data\processed_guangzhou.xlsx', index_col=0, skiprows=0)
jinan_data = pd.read_excel(r'.\data\processed_jinan.xlsx', index_col=0, skiprows=0)
yinchuan_data = pd.read_excel(r'.\data\processed_yinchuan.xlsx', index_col=0, skiprows=0)

beijing_prcp = beijing_data.get('PRCP')
dalian_prcp = dalian_data.get('PRCP')
guangzhou_prcp = guangzhou_data.get('PRCP')
jinan_prcp = jinan_data.get('PRCP')
yinchuan_prcp = yinchuan_data.get('PRCP')


def adf_check(prcp):
    t = adfuller(prcp)  # ADF test
    output = pd.DataFrame(
        index=['Test Statistic Value', "p-value", "Lags Used", "Number of Observations Used", "Critical Value(1%)",
               "Critical Value(5%)", "Critical Value(10%)"], columns=['value'])
    output['value']['Test Statistic Value'] = t[0]
    output['value']['p-value'] = t[1]
    output['value']['Lags Used'] = t[2]
    output['value']['Number of Observations Used'] = t[3]
    output['value']['Critical Value(1%)'] = t[4]['1%']
    output['value']['Critical Value(5%)'] = t[4]['5%']
    output['value']['Critical Value(10%)'] = t[4]['10%']
    return output
    # if ADF test value < {1%}, then stable


def plot_acf_pacf(prcp):
    plot_acf(prcp)
    plot_pacf(prcp, method='ywm')
    plt.show()


def inverse_diff(original, diff):
    lag = len(original)
    origin_s = list(original)
    for i in range(len(diff)):
        o = diff[i] + origin_s[i]
        origin_s.append(o)


def auto_arima_model(data):
    train_size = 45
    test_size = data.size - train_size
    train, test = data[0:train_size], data[train_size:]
    fig = plt.figure(dpi=256)
    fig.add_subplot()
    plt.plot(train, 'r-', label='train_data')
    plt.plot(test, 'y-', label='test_data')
    model = auto_arima(train, start_p=0, start_q=0, max_p=8, max_q=8, max_d=2,
                       seasonal=True, test='adf',
                       error_action='ignore',
                       information_criterion='aic',
                       njob=-1, trace=True, suppress_warnings=True)
    model.fit(train)
    return model


def manual_arima_model(data, p, d, q, test_ratio=0.8):
    test_size = int(data.shape[0] * test_ratio)
    train_size = data.shape[0] - test_size
    train_set = data[:train_size].values
    test_set = data[train_size:].values

    history = list(train_set)
    predictions = list()

    for t in range(len(test_set)):
        model = ARIMA(history, order=(p, d, q))
        model_fit = model.fit()
        forecast_value = model_fit.forecast()
        yhat = forecast_value[0]
        predictions.append(yhat)
        obs = test_set[t]
        history.append(obs)

    plt.figure(dpi=256)
    plt.plot(test_set)
    plt.plot(predictions, color='darkviolet')
    plt.xlabel('Series Number')
    plt.ylabel('Precipitation(mm)')
    plt.show()