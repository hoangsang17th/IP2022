# Phân đoạn ảnh bằng cắt ngưỡng thích nghi dựa trên Thuộc tính vùng ảnh cục bộ
import numpy as np
import cv2
import matplotlib.pyplot as plt

def Phan_doan_lan_can(img, ksize):
    m, n = img.shape
    img_ket_qua_phan_doan = np.zeros([m, n])
    h=(ksize -1) // 2
    a=20
    b=1
    padded_img = np.pad(img, (h, h), mode='reflect')
    mG = np.mean(padded_img)   # Bước 1. Tính trung bình mức xám ảnh
    for i in range(m):
        for j in range(n):
            vung_anh_kich_thuoc_k = padded_img[i:i+ksize,j:j+ksize]
            Do_lech_chuan = np.std(vung_anh_kich_thuoc_k) # Bước 1. Tính độ lệch chuẩn cục bộ
            T= a*Do_lech_chuan + b*mG   # Bước 2. Tính ngưỡng theo công thức 11
            if padded_img[i, j] > T:    # Bước 3. Cắt ngưỡng theo công thức 12
                img_ket_qua_phan_doan[i, j] = 255
            else:
                img_ket_qua_phan_doan[i, j] = 0
    return img_ket_qua_phan_doan

if __name__ == "__main__":
    img_goc = cv2.imread('test1.tif', 0)
    ksize =3
    img_ket_qua = Phan_doan_lan_can(img_goc, ksize)

    fig = plt.figure(figsize=(16, 9))     # Thiết lập vùng (cửa sổ) vẽ
    (ax1, ax2) = fig.subplots(1, 2)        # Thiết lập 2 vùng con ax1, ax2
    ax1.imshow(img_goc, cmap='gray')      # Hiển thị ảnh gốc vùng ax1
    ax1.set_title("ảnh gốc")  # Thiết lập tiêu đề vùng ax1
    ax1.axis("off")

    ax2.imshow(img_ket_qua, cmap='gray')  # Hiển thị ảnh sau khi lọc
    ax2.set_title("ảnh phân đoạn dựa vào tìm ngưỡng thích nghi lân cận") # Thiết lập tiêu đề vùng ax2
    ax2.axis("off")

    plt.show()