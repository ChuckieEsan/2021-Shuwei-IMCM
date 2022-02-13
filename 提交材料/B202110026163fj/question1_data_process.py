import pandas as pd
from datetime import datetime

'''
    本代码文件的目的是计算年降水量
    注意：气象站不监视降雨时，会将降水量记为99.99
    同时，降水量的单位是英寸
    1 inch = 25.4mm
'''

station1 = pd.read_excel(io='data_zhengzhou.xlsx', sheet_name='beijing', index_col=0, skiprows=0)
station2 = pd.read_excel(io='data_zhengzhou.xlsx', sheet_name='station2', index_col=0, skiprows=0)
station3 = pd.read_excel(io='data_zhengzhou.xlsx', sheet_name='station3', index_col=0, skiprows=0)
size1 = station1.shape
size2 = station2.shape
size3 = station3.shape
# beijing 采集1958年开始的信息
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
for i in range(0, size1[0]):
    cur_row = station1.iloc[i, :]
    cur_date = cur_row[0].to_pydatetime()
    if last_year < cur_date.year:
        year_array.append(cur_date.year)
        last_year = cur_date.year
    if last_year == 2020:
        break
for i in range(0, size1[0]):
    cur_row = station1.iloc[i, :]
    cur_date = cur_row[0].to_pydatetime()
    year = cur_date.year
    cur_dewp = cur_row[1]  # missing is = 9999.9
    cur_max = cur_row[4]  # missing is = 9999.9
    cur_min = cur_row[5]  # missing is = 9999.9
    cur_mxspd = cur_row[6]  # missing is = 999.9
    cur_prcp = cur_row[7]  # missing is = 99.99
    cur_slp = cur_row[8]  # missing is = 9999.9
    cur_temp = cur_row[11]  # missing is = 9999.9
    cur_visib = cur_row[12]  # missing is = 999.9
    cur_wdsp = cur_row[13]  # missing is = 999.9
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
station1_data = pd.DataFrame(data, index=index_label,
                             columns=year_array).T

# station2 采集1984年开始的信息
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
last_year = 1983
for i in range(0, size2[0]):
    cur_row = station2.iloc[i, :]
    cur_date = cur_row[0].to_pydatetime()
    if last_year < cur_date.year:
        year_array.append(cur_date.year)
        last_year = cur_date.year
    if last_year == 2020:
        break
for i in range(0, size2[0]):
    cur_row = station2.iloc[i, :]
    cur_date = cur_row[0].to_pydatetime()
    year = cur_date.year
    cur_dewp = cur_row[1]  # missing is = 9999.9
    cur_max = cur_row[4]  # missing is = 9999.9
    cur_min = cur_row[5]  # missing is = 9999.9
    cur_mxspd = cur_row[6]  # missing is = 999.9
    cur_prcp = cur_row[7]  # missing is = 99.99
    cur_slp = cur_row[8]  # missing is = 9999.9
    cur_temp = cur_row[11]  # missing is = 9999.9
    cur_visib = cur_row[12]  # missing is = 999.9
    cur_wdsp = cur_row[13]  # missing is = 999.9
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
station2_data = pd.DataFrame(data, index=index_label,
                             columns=year_array).T

# station3 采集1962年开始的信息
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
last_year = 1961
for i in range(0, size3[0]):
    cur_row = station3.iloc[i, :]
    cur_date = cur_row[0].to_pydatetime()
    if last_year < cur_date.year:
        year_array.append(cur_date.year)
        last_year = cur_date.year
    if last_year == 2020:
        break
for i in range(0, size3[0]):
    cur_row = station3.iloc[i, :]
    cur_date = cur_row[0].to_pydatetime()
    year = cur_date.year
    cur_dewp = cur_row[1]  # missing is = 9999.9
    cur_max = cur_row[4]  # missing is = 9999.9
    cur_min = cur_row[5]  # missing is = 9999.9
    cur_mxspd = cur_row[6]  # missing is = 999.9
    cur_prcp = cur_row[7]  # missing is = 99.99
    cur_slp = cur_row[8]  # missing is = 9999.9
    cur_temp = cur_row[11]  # missing is = 9999.9
    cur_visib = cur_row[12]  # missing is = 999.9
    cur_wdsp = cur_row[13]  # missing is = 999.9
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
station3_data = pd.DataFrame(data, index=index_label,
                             columns=year_array).T

station1_data.to_excel(r'.\data\station1.xlsx')
station2_data.to_excel(r'.\data\station2.xlsx')
station3_data.to_excel(r'.\data\station3.xlsx')