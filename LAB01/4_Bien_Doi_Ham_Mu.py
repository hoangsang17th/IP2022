import cv2 as cv
import matplotlib.pyplot as plt

def Gamma_Convert(img, gamma, c):
    # s = c * r mũ gamma
    return float(c) * pow(img, float(gamma))

fig = plt.figure(figsize=(7, 7))
(ax1, ax2), (ax3, ax4) = fig.subplots(2, 2)

img = cv.imread('Image.tif',0)
ax1.imshow(img, cmap='gray')
ax1.set_title("ảnh gốc")
# IP3/Tr20 Sử dụng ảnh này với các thoong số bên dưới
y1 = Gamma_Convert(img, 3.0, 1.0)
ax2.imshow(y1, cmap='gray')
ax2.set_title("gamma=3")

y2 = Gamma_Convert(img, 4.0, 1.0)
ax3.imshow(y2, cmap='gray')
ax3.set_title("gamma=4")

y3 = Gamma_Convert(img, 5.0, 1.0)
ax4.imshow(y3, cmap='gray')
ax4.set_title("gamma=5")
plt.show()
