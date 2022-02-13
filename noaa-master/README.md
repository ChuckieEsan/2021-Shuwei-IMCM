# 获取NOAA开放数据

#### 介绍
使用Python脚本批量获取NOAA开放数据并做简单归并处理

#### 目录结构
```
├── LICENSE             开源协议
├── README.md           帮助文档
├── config.py           配置文件
├── noaa.db             数据库文件，因超重而未直接出现在仓库中
├── noaa.py             主程序，功能入口
├── noaa_doc            下载自NOAA官方网站的数据说明文档
│   ├── readme.pdf      提供了所有变量的英文名，与数据库字段名相同
│   ├── readme.txt
│   └── sample.csv
├── requirements.txt    正常运行该脚本需要安装的依赖库
└── toolbox.py          为实现主程序功能而撰写的辅助函数
```

#### 使用说明
1. 首先需要安装所有依赖项，让脚本能够跑起来。
   ```bash
   pip install -r requirements.txt
   ```
1. 受限于gitee的5G存储上限，我无法将数据库文件直接放在仓库当中，所以需要从百度网盘上下载我处理好的db文件。
    ```
   链接：https://pan.baidu.com/s/1Svf7vA2h0VvzpWj6s1o-mQ 
   提取码：1htq
   ```
   
   <font color=#FF0000>温馨提示：压缩包比较大，切割成了若干个卷，下载的时候要把所有的卷都下载下来哈。</font>
   
1. 使用老铁们学到的SQL语句尽情地探索该数据库文件吧（基于SQLite），推荐大家使用[Navicat](https://www.navicat.com.cn/)。

#### 数据库表结构
数据库包含有两个表，名别是命名为`info`的站点信息表和命名为`data`的数据表，两个表的表结构概括如下：
- info表（地理位置信息是根据经纬度计算的，部分气象站未提供经纬度，则不会出现在info表中。）
  ```sql
  CREATE TABLE IF NOT EXISTS info(
                   station_id CHAR(12) NOT NULL,
                   name       VARCHAR(50),
                   latitude   FLOAT,
                   longitude  FLOAT,
                   country    VARCHAR(20),
                   province   VARCHAR(20),
                   city       VARCHAR(20),
                   district   VARCHAR(20),
                   PRIMARY KEY (station_id)
               );  
  ```

- data表
    ```sql
    CREATE TABLE IF NOT EXISTS data(
                   station    CHAR(12) NOT NULL,
                   date       DATE NOT NULL,
                   temp       FLOAT,
                   dewp       FLOAT,
                   slp        FLOAT,
                   stp        FLOAT,
                   visib      FLOAT,
                   wdsp       FLOAT,
                   mxspd      FLOAT,
                   gust       FLOAT,
                   max        FLOAT,
                   min        FLOAT,
                   prcp       FLOAT,
                   sndp       FLOAT,
                   frshtt     int,
                   PRIMARY KEY (station, date)
               );  
  ```

#### 常用功能
1. 检索气象站id为`99999954777`的所有历史数据，该气象站id未提供经纬度信息。
    ```python
    from noaa import NOAA
    app = NOAA()
    df = app.fetch_station_data('99999954777', start_date='2005-06-07', end_date='2005-11-30')
    print(df)
    ```
   `start_date`和`end_date`可以留空或设置为`None`，表示不限制气象数据的起始日期或结束日期，
   函数的返回值为pandas.DataFrame类型数据。
   
1. 检索气象站的地理位置信息，部分气象站无数据，将会返回空字典。
    ```python
    from noaa import NOAA
    app = NOAA()
    location = app.fetch_station_location('A5125600451')
    print(location)
    ```

1. 检索我国甘肃省所有气象站在2019年全年的观测数据。
   ```python
   from noaa import NOAA
   app = NOAA()
   df = app.fetch_chinese_data('甘肃', start_date='2002-10-04', end_date=None)
   df.to_csv('gansu.csv', index=False)
   ```
   函数的第一个参数取值为`None`可以拿到全国的数据。

#### 更多说明
老铁们可以在[我的知乎](https://zhuanlan.zhihu.com/p/362808034)上查阅到有关NOAA的更多说明。