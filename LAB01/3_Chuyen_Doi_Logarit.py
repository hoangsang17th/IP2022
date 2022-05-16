import cv2 as cv
import matplotlib.pyplot as plt

def logarit_convert(img, c):
    # Là thao tác xử lý điểm ảnh trên ảnh có dạng s = c * log(1+ r) 
    # Với s là điểm ảnh đã xử lý, r >= 0 là điểm ảnh đầu vào, c hằng số
    # Xem chi tiết tại IP3/Tr16
    return float(c) * cv.log(1.0 + img)


fig = plt.figure(figsize=(7, 4))
ax1, ax2 = fig.subplots(1, 2)

img = cv.imread('Loga.tif')
ax1.imshow(img, cmap='gray')
ax1.set_title("Ảnh gốc")

# IP3/Tr17 Cô lấy c = 2
y = logarit_convert(img, 2)
ax2.imshow(y, cmap='gray')
ax2.set_title("Chuyển đổi bằng hàm Logarit")
plt.show()

