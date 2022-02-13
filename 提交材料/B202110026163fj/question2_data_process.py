import pandas as pd
from datetime import datetime

beijing = pd.read_excel(io=r'.\data\Beijing.xlsx', index_col=0, skiprows=0)
dalian = pd.read_excel(io=r'.\data\Dalian.xlsx', index_col=0, skiprows=0)
guangzhou = pd.read_excel(io=r'.\data\Guangzhou.xlsx', index_col=0, skiprows=0)
jinan = pd.read_excel(io=r'.\data\Jinan.xlsx', index_col=0, skiprows=0)
yinchuan = pd.read_excel(io=r'.\data\Yinchuan.xlsx', index_col=0, skiprows=0)


# beijing 采集1958年开始的信息
def data_process(data):
    prcp = 0
    dewp = 0
    max_ = 0
    min_ = 0
    mxspd = 0
    slp = 0
    temp = 0
    visib = 0
    wdsp = 0
    prcp_array = []
    dewp_array = []
    max_array = []
    min_array = []
    mxspd_array = []
    slp_array = []
    temp_array = []
    visib_array = []
    wdsp_array = []
    available_days = []
    count = 0
    year_array = []
    year_count = 0
    last_year = 1957
    for i in range(0, data.shape[0]):
        cur_row = data.iloc[i, :]
        cur_date = cur_row['DATE'].to_pydatetime()
        if last_year < cur_date.year:
            year_array.append(cur_date.year)
            last_year = cur_date.year
        if last_year == 2020:
            break
    for i in range(0, data.shape[0]):
        cur_row = data.iloc[i, :]
        cur_date = cur_row['DATE'].to_pydatetime()
        year = cur_date.year
        cur_dewp = cur_row['DEWP']  # missing is = 9999.9
        cur_max = cur_row['MAX']  # missing is = 9999.9
        cur_min = cur_row['MIN']  # missing is = 9999.9
        cur_mxspd = cur_row['MXSPD']  # missing is = 999.9
        cur_prcp = cur_row['PRCP']  # missing is = 99.99
        cur_slp = cur_row['SLP']  # missing is = 9999.9
        cur_temp = cur_row['TEMP']  # missing is = 9999.9
        cur_visib = cur_row['VISIB']  # missing is = 999.9
        cur_wdsp = cur_row['WDSP']  # missing is = 999.9
        start_date = datetime(year, 1, 1)
        end_date = datetime(year, 12, 31)
        if start_date <= cur_date <= end_date:
            if cur_prcp < 90:
                prcp += cur_prcp
                count += 1
            if cur_dewp < 9000:
                dewp += cur_dewp
            if cur_max < 9000:
                max_ += cur_max
            if cur_min < 9000:
                min_ += cur_min
            if cur_mxspd < 900:
                mxspd += cur_mxspd
            if cur_slp < 9000:
                slp += cur_slp
            if cur_temp < 9000:
                temp += cur_temp
            if cur_visib < 900:
                visib += cur_visib
            if cur_wdsp < 900:
                wdsp += cur_wdsp
        if year_count >= year_array.__len__():
            break
        if cur_date.year > year_array[year_count]:
            year_count += 1
            prcp_array.append(prcp * 25.4)
            dewp_array.append(dewp / count)
            max_array.append(max_ / count)
            min_array.append(min_ / count)
            mxspd_array.append(mxspd / count)
            slp_array.append(slp / count)
            temp_array.append(temp / count)
            visib_array.append(visib / count)
            wdsp_array.append(wdsp / count)
            available_days.append(count)
            prcp = 0
            dewp = 0
            max_ = 0
            min_ = 0
            mxspd = 0
            slp = 0
            temp = 0
            visib = 0
            wdsp = 0
            count = 0
    index_label = ['PRCP', 'available_days', 'DEWP', 'MAX', 'MIN', 'MXSPD', 'SLP', 'TEMP', 'VISIB', 'WDSP']
    data = [prcp_array, available_days,
            dewp_array, max_array, min_array, mxspd_array, slp_array, temp_array, visib_array, wdsp_array]
    station_data = pd.DataFrame(data, index=index_label,
                                columns=year_array).T
    return station_data


beijing_data = data_process(beijing)
dalian_data = data_process(dalian)
guangzhou_data = data_process(guangzhou)
jinan_data = data_process(jinan)
yinchuan_data = data_process(yinchuan)

beijing_data.to_excel(r'.\data\processed_beijing.xlsx')
dalian_data.to_excel(r'.\data\processed_dalian.xlsx')
guangzhou_data.to_excel(r'.\data\processed_guangzhou.xlsx')
jinan_data.to_excel(r'.\data\processed_jinan.xlsx')
yinchuan_data.to_excel(r'.\data\processed_yinchuan.xlsx')