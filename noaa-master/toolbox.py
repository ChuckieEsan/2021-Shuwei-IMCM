# -*- coding: utf-8 -*-
# @Time        : 2021/4/7 15:58
# @Author      : DouHua
# @Email       : feng@dongfa.pro
# @File        : toolbox.py
# @Project     : noaa
# @Description : 辅助函数库
import os
import tarfile
import requests


class BaiduMap:
    """
    处理与百度地图API相关的所有操作
    """
    def __init__(self, ak: str):
        """
        初始化类
        :param ak: 从百度地图API控制台处获取到的AK
        """
        self.ak = ak
        self.reverse_geocoding_url = 'http://api.map.baidu.com/reverse_geocoding/v3/'
        self.s = requests.Session()

    def get_location(self, lat: float, lng: float) -> dict:
        """
        根据提供的经纬度坐标获取地理位置信息
        :param lat: 纬度
        :param lng: 经度
        :return:
        """
        params = {
            'ak':        self.ak,
            'output':    'json',
            'coordtype': 'wgs84ll',
            'location':  f'{lat},{lng}',
        }
        resp = self.s.get(url=self.reverse_geocoding_url, params=params).json()
        address = resp['result']['addressComponent']

        # 仅返回其中的省市县信息
        return {
           item: address[item] for item in ['country', 'province', 'city', 'district']
        }


def extract_tar(file_path: str) -> None:
    """
    解压tar.gz压缩文件，使用压缩文件名新建同名文件夹，压缩包当中的内容全部解压到其中
    :param file_path: tar.gz压缩文件的路径
    :return: 直接解压文件，无需返回值
    """
    # 读取压缩包文件
    tar = tarfile.open(file_path)

    # 根据路径名新建文件夹
    folder_path, file_path = os.path.split(file_path)
    target_folder = os.path.join(folder_path, file_path.split('.')[0])
    if os.path.exists(target_folder) or os.path.isfile(target_folder):
        # 如果文件夹已经存在，就认为解压缩任务已经完成了，不再重复执行
        return
    else:
        os.mkdir(target_folder)

    # 将压缩包当中的所有内容解压到目标文件夹
    tar.extractall(target_folder)

    # 添加一条提示信息，防止自己以为电脑卡了
    print(f'文件 {file_path} 处理完毕！')
