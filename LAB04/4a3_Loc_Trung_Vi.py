import cv2  # import thư viện OpenCV
import numpy as np #import thư viện numpy để làm việc với dữ liệu kiểu mảng
import matplotlib.pyplot as plt # import thư viện matplotlib để vẽ ảnh


# Định nghĩa hàm lọc trung vị
def loc_trung_vi(img):
    m, n = img.shape
    img_new = np.zeros([m, n])
    for i in range(1, m-1): 
        for j in range(1, n-1): 
            temp = [img[i-1, j-1], 
                   img[i-1, j], 
                   img[i-1, j + 1], 
                   img[i, j-1], 
                   img[i, j], 
                   img[i, j + 1], 
                   img[i + 1, j-1], 
                   img[i + 1, j], 
                   img[i + 1, j + 1]] 
          
            temp = sorted(temp) 
            img_new[i, j]= temp[4] 
    img_new = img_new.astype(np.uint8)
    return img_new

fig = plt.figure(figsize=(7, 4)) # Tạo vùng vẽ tỷ lệ 16:9
ax1, ax2 = fig.subplots(1, 2) # Tạo 2 vùng vẽ con

# Đọc và hiển thị ảnh gốc
image = cv2.imread('test2.tif', 0)
ax1.imshow(image, cmap='gray')
ax1.set_title("ảnh gốc")

# Lọc trung vị 3 x 3 và hiển thị ảnh
imagenew = loc_trung_vi(image) #Gọi hàm lọc
ax2.imshow(imagenew, cmap='gray')
ax2.set_title("ảnh lọc trung vị")
plt.show()
