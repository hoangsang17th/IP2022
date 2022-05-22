import numpy as np
import cv2 as cv
from PIL import Image, ImageFilter


class Noises:
    def maxFilter(self, img):
        maxf = img.filter(ImageFilter.MinFilter(size=3))
        return maxf

    def minFilter(self, img):
        minf = img.filter(ImageFilter.MaxFilter(size=3))
        return minf

    def midpoint(self, img):
        minf = img.filter(ImageFilter.MaxFilter(size=3))
        maxf = img.filter(ImageFilter.MinFilter(size=3))
        midpoint = (maxf + minf) / 2

        return midpoint

    def contraharmonicMean(self, img, Q):
        print("hello")
        num = np.power(img, Q/10 + 1)
        denom = np.power(img, Q/10)

        kernel = np.full((9, 9), 1.0)

        result = cv.filter2D(num, -1, kernel) / cv.filter2D(denom, -1, kernel)

        return result
