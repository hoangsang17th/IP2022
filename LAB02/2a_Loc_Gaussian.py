import cv2
import numpy as np
import matplotlib.pyplot as plt

# Định nghĩa hàm lọc Gaussian


def Apply_Filter(img, mask):
    m, n = img.shape
    img_new = np.zeros([m, n])
    for i in range(1, m-1):
        for j in range(1, n-1):
            temp = img[i-1, j-1] * mask[0, 0] + img[i-1, j] * mask[0, 1] + img[i-1, j + 1] * mask[0, 2]\
                + img[i, j-1] * mask[1, 0] + img[i, j] * mask[1, 1] + img[i, j + 1] * mask[1, 2]\
                + img[i + 1, j-1] * mask[2, 0] + img[i + 1, j] * + \
                mask[2, 1] + img[i + 1, j + 1] * mask[2, 2]
            img_new[i, j] = temp
    img_new = img_new.astype(np.uint8)
    return img_new


# Định nghĩa bộ lọc Gaussian
gaussianFilter = np.array(([0.0751/4.8976, 0.1238/4.8976, 0.0751/4.8976],
                           [0.1238/4.8976, 0.2042/4.8976, 0.1238/4.8976],
                           [0.0751/4.8976, 0.1238/4.8976, 0.0751/4.8976]), dtype="float")

fig = plt.figure(figsize=(7, 4))
(ax1, ax4) = fig.subplots(1, 2)

# Đọc và hiển thị ảnh gốc
image = cv2.imread('Image.jpg', 0)
ax1.imshow(image, cmap='gray')
ax1.set_title("Ảnh gốc")

# Lọc Gaussian và hiển thị ảnh
imgGaussian_3x3 = Apply_Filter(image, gaussianFilter)  # Gọi hàm lọc
ax4.imshow(imgGaussian_3x3, cmap='gray')
ax4.set_title("Ảnh lọc Gaussian 3x3")
print(gaussianFilter[0, 1])
# Hiển thị vùng vẽ
plt.show()
