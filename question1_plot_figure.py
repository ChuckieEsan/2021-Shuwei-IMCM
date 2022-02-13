import pandas as pd

station1_data = pd.read_excel(r'.\data\station1.xlsx', index_col=0, skiprows=0)
station2_data = pd.read_excel(r'.\data\station2.xlsx', index_col=0, skiprows=0)
station3_data = pd.read_excel(r'.\data\station3.xlsx', index_col=0, skiprows=0)

prcp_array = []
dewp_array = []
max_array = []
min_array = []
mxspd_array = []
slp_array = []
temp_array = []
visib_array = []
wdsp_array = []

start_index = 1958
for i in range(start_index, 2021):
    count = 0
    prcp = 0
    dewp = 0
    max_ = 0
    min_ = 0
    mxspd = 0
    slp = 0
    slp = 0
    temp = 0
    visib = 0
    wdsp = 0
    if i in station1_data.index:
        count += 1
        prcp += station1_data.loc[i]['PRCP']
        dewp += station1_data.loc[i]['DEWP']
        max_ += station1_data.loc[i]['MAX']
        min_ += station1_data.loc[i]['MIN']
        mxspd += station1_data.loc[i]['MXSPD']
        slp += station1_data.loc[i]['SLP']
        temp += station1_data.loc[i]['TEMP']
        visib += station1_data.loc[i]['VISIB']
        wdsp += station1_data.loc[i]['WDSP']
    if i in station2_data.index:
        count += 1
        prcp += station2_data.loc[i]['PRCP']
        dewp += station2_data.loc[i]['DEWP']
        max_ += station2_data.loc[i]['MAX']
        min_ += station2_data.loc[i]['MIN']
        mxspd += station2_data.loc[i]['MXSPD']
        slp += station2_data.loc[i]['SLP']
        temp += station2_data.loc[i]['TEMP']
        visib += station2_data.loc[i]['VISIB']
        wdsp += station2_data.loc[i]['WDSP']
    if i in station3_data.index:
        count += 1
        prcp += station3_data.loc[i]['PRCP']
        dewp += station3_data.loc[i]['DEWP']
        max_ += station3_data.loc[i]['MAX']
        min_ += station3_data.loc[i]['MIN']
        mxspd += station3_data.loc[i]['MXSPD']
        slp += station3_data.loc[i]['SLP']
        temp += station3_data.loc[i]['TEMP']
        visib += station3_data.loc[i]['VISIB']
        wdsp += station3_data.loc[i]['WDSP']
    if count > 0:
        prcp = prcp / count
        dewp = dewp / count
        max_ = max_ / count
        min_ = min_ / count
        mxspd = mxspd / count
        slp = slp / count
        temp = temp / count
        visib = visib / count
        wdsp = wdsp / count
    prcp_array.append(prcp)
    dewp_array.append(dewp)
    max_array.append(max_)
    min_array.append(min_)
    mxspd_array.append(mxspd)
    slp_array.append(slp)
    temp_array.append(temp)
    visib_array.append(visib)
    wdsp_array.append(wdsp)

index_label = ['PRCP', 'DEWP', 'MAX', 'MIN', 'MXSPD', 'SLP', 'TEMP', 'VISIB', 'WDSP']
data = [prcp_array, dewp_array, max_array, min_array, mxspd_array, slp_array, temp_array, visib_array, wdsp_array]
station_data = pd.DataFrame(data, index=index_label,
                            columns=range(1958, 2021)).T
station_data.to_excel(r'.\data\data.xlsx')
