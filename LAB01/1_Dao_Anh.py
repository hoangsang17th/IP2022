import cv2 as cv
import matplotlib.pyplot as plt

def photo_island(img):
    # Đảo ảnh với ảnh có các giá trị mức xám trong vùng [0, L – 1]
    # Là thao tác xử lý điểm ảnh trên ảnh có dạng s = (L – 1) – r
    return 255-img


fig = plt.figure(figsize=(7, 4))
ax1, ax2 = fig.subplots(1, 2)

img = cv.imread('Image.tif',0)
ax1.imshow(img, cmap='gray')
ax1.set_title("Ảnh gốc")

y = photo_island(img)
ax2.imshow(y, cmap='gray')
ax2.set_title("Ảnh đảo")
plt.show()
