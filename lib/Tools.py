# -*- coding: UTF-8 -*-
'''
@Time    : 2023/3/21 14:47
@Author  : 魏林栋
@Site    : 
@File    : Tools.py
@Software: PyCharm
'''
import os
import pydicom
import cv2
import numpy as np
import nibabel as nib
from concurrent.futures import ThreadPoolExecutor


class Tools:
    def __init__(self):
        pass

    def dcmToPng(self, address, save_path):
        data = pydicom.read_file(address)
        image = self.normaliza(data.pixel_array)
        cv2.imwrite(save_path, image * 255)

    def deleteTemp(self, path_file):
        ls = os.listdir(path_file)
        for i in ls:
            f_path = os.path.join(path_file, i)
            # 判断是否是一个目录,若是,则递归删除
            if os.path.isdir(f_path):
                self.deleteTemp(f_path)
            else:
                os.remove(f_path)

    def niigzToPng(self, filePath, targetPath):
        self.images = []
        image_arr = nib.load(filePath).get_fdata()
        with ThreadPoolExecutor(max_workers=5) as pool:
            for index in range(image_arr.shape[2]):
                pool.submit(lambda cxp: self.saveImage(*cxp),
                            (image_arr[:, :, index], index, targetPath.replace('\\', '/')))
        return self.images

    def saveImage(self, image, index, targetPath):
        address = f'{targetPath}/{index}.png'
        image = self.normaliza(image)
        image = cv2.resize(image, (512, 512))
        cv2.imwrite(address, image * 255.0)
        self.images.append(address)

    def normaliza(self, x):
        '''
        :param x: 输入ndarray矩阵
        :return: 归一化矩阵数据
        '''
        np.seterr(divide='ignore', invalid='ignore')
        return (x - np.min(x)) / (np.max(x) - np.min(x))
