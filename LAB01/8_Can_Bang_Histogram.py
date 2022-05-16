import cv2
import matplotlib.pyplot as plt

img = cv2.imread('Image.tif',0)
img_equalized = cv2.equalizeHist(img)

fig = plt.figure(figsize=(7, 4))
ax1, ax3 = fig.subplots(1, 2)


ax1.imshow(img, cmap='gray')
ax1.set_title("ảnh gốc")

# Vẽ ảnh sau khi cân bằng Hist trong vùng ax3
ax3.imshow(img_equalized, cmap='gray')
ax3.set_title("ảnh cân bằng histogram")


plt.show() # Hiển thị vùng vẽ