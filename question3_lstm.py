# -*- coding: utf-8 -*-
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.layers import Input, Dense, LSTM, GRU, BatchNormalization
from tensorflow.keras.layers import PReLU
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
from sklearn.metrics import mean_absolute_error as MAE
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd
import numpy as np
import os

data = pd.read_excel(r'.\data\beijing_lstm.xlsx', index_col=0)
X = data.iloc[:, 2:]
Y = data.iloc[:, 0:1]
xScaler = StandardScaler()
yScaler = StandardScaler()
X = xScaler.fit_transform(X)
Y = yScaler.fit_transform(Y)

outputCol = ['PRCP']
inputCol = ['DEWP', 'MAX', 'MIN', 'MXSPD', 'VISIB', 'WDSP', 'TEMP']
timeStep = 5
outStep = 1
xAll = list()
yAll = list()

for row in range(data.shape[0] - timeStep - outStep + 1):
    x = X[row:row + timeStep]
    y = Y[row + timeStep:row + timeStep + outStep]
    xAll.append(x)
    yAll.append(y)
xAll = np.array(xAll).reshape(-1, timeStep, len(inputCol))
yAll = np.array(yAll).reshape(-1, outStep)

testRate = 0.2
splitIndex = int(xAll.shape[0] * (1 - testRate))
xTrain = xAll[:splitIndex]
xTest = xAll[splitIndex:]
yTrain = yAll[:splitIndex]
yTest = yAll[splitIndex:]


def buildLSTM(timeStep, inputColNum, outStep, learnRate=1e-4):
    '''
    搭建LSTM网络，激活函数为tanh
    timeStep：输入时间步
    inputColNum：输入列数
    outStep：输出时间步
    learnRate：学习率
    '''
    # 输入层
    inputLayer = Input(shape=(timeStep, inputColNum))

    # 中间层
    middle = LSTM(100, activation='tanh')(inputLayer)
    middle = Dense(100, activation='tanh')(middle)

    # 输出层 全连接
    outputLayer = Dense(outStep)(middle)

    # 建模
    model = Model(inputs=inputLayer, outputs=outputLayer)
    optimizer = Adam(lr=learnRate)
    model.compile(optimizer=optimizer, loss='mse')
    model.summary()
    return model


# 搭建LSTM
lstm = buildLSTM(timeStep=timeStep, inputColNum=len(inputCol), outStep=outStep, learnRate=1e-4)
