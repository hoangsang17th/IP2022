import cv2 as cv
import matplotlib.pyplot as plt

def threshold_cut(img, th):
    return img > th


fig = plt.figure(figsize=(7, 4))
ax1, ax2 = fig.subplots(1, 2)
 
img = cv.imread('Image.tif',0)
ax1.imshow(img,cmap='gray')
ax1.set_title("Ảnh gốc")

y = threshold_cut(img, th=117)
ax2.imshow(y, cmap='gray')
ax2.set_title("Ảnh cắt ngưỡng")
plt.show()

