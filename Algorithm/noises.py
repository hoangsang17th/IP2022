import numpy as np
import cv2 as cv
from PIL import Image, ImageFilter
import matplotlib.pyplot as plt


class Noises:
    def maxFilter(self, img):
        maxf = np.uint8(img.filter(ImageFilter.MinFilter(size=3)))
        return maxf

    def minFilter(self, img):
        minf = np.uint8(img.filter(ImageFilter.MaxFilter(size=3)))
        return minf

    def midpoint(self, img):
        # mask33
        mask = np.ones((3, 3), dtype="float") * (1.0 / (3 * 3))
        m = img.shape[0]
        n = img.shape[1]
        img_new = np.zeros([m, n])
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                temp = img[i - 1, j - 1] * mask[0, 0] + img[i - 1, j] * mask[0, 1] + img[i - 1, j + 1] * mask[0, 2] + img[
                    i, j - 1] * mask[1, 0] + img[i, j] * mask[1, 1] + img[i, j + 1] * mask[1, 2] + img[i + 1, j - 1] * mask[
                    2, 0] + img[i + 1, j] * mask[2, 1] + img[i + 1, j + 1] * mask[2, 2]
                img_new[i, j] = temp
        img = img_new.astype(np.uint8)
        return img

    def contraharmonicMean(self, img, Q):
        Q = Q/10
        ksize = 3
        m = img.shape[0]
        n = img.shape[1]
        img_ket_qua_anh_loc = np.zeros([m, n])

        h = (ksize - 1) // 2
        padded_img = np.pad(img, (h, h), mode='reflect')
        padded_img_bac_Q_cong_1 = np.power(padded_img, Q+1)
        padded_img_bac_Q = np.power(padded_img, Q)

        for i in range(m):
            for j in range(n):
                vung_anh_kich_thuoc_k_bac_Q_cong_1 = padded_img_bac_Q_cong_1[i:i+ksize, j:j+ksize]
                vung_anh_kich_thuoc_k_bac_Q = padded_img_bac_Q[i:i +
                                                               ksize, j:j + ksize]
                img_bac_Q_1 = np.sum(vung_anh_kich_thuoc_k_bac_Q_cong_1)
                img_bac_Q = np.sum(vung_anh_kich_thuoc_k_bac_Q)
                gia_tri_loc = img_bac_Q_1/img_bac_Q
                img_ket_qua_anh_loc[i, j] = gia_tri_loc
        return np.uint8(img_ket_qua_anh_loc)
