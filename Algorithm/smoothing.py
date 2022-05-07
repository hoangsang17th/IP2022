import cv2


class Smoothings:

    def change_Blur(self, img, value):
        kernel_size = (value + 1, value + 1)
        img = cv2.blur(img, kernel_size)
        return img
    # %2 ==1 => Số lẻ và là yêu cầu đầu vào của mấy hàm bên dưới này

    def change_Gaussian(self, img, value):
        if (value % 2 == 1):
            kernel_size = (value, value)
            img = cv2.GaussianBlur(img, kernel_size, cv2.BORDER_DEFAULT)
        else:
            kernel_size = (value + 1, value + 1)
            img = cv2.GaussianBlur(img, kernel_size, cv2.BORDER_DEFAULT)
        return img

    def change_Median(self, img, value):
        if (value % 2 == 1):
            img = cv2.medianBlur(img, value)
        else:
            img = cv2.medianBlur(img, value + 1)
        return img

    def change_Bilateral(self, img, value):
        # bilateralFilter(img, d, sigmaColor, sigmaSpace)
        # sigmaColor <10 không có thay đổi, >150 nhìn hơi giống vẽ
        # d = 5 < Nhanh, d = 9 Lâu
        img = cv2.bilateralFilter(img, 9, value, 75)
        return img
