import cv2
import numpy as np


class Channels:

    def change_Color(self, img, red, green, blue, alpha):

        img = cv2.convertScaleAbs(img, alpha=alpha*0.01)
        b, g, r = cv2.split(img)

        for r_value in r:
            cv2.add(r_value, red, r_value)

        for g_value in g:
            cv2.add(g_value, green, g_value)

        for b_value in b:
            cv2.add(b_value, blue, b_value)

        img = cv2.merge((b, g, r))
        return img

    def change_Gamma(self, img, value):
        print("Gamma: " + str(value))
        img = np.uint8(float(1) * pow(img, float(value * 0.03)))
        return img

    def change_Logarit(self, img, value):
        # Là thao tác xử lý điểm ảnh trên ảnh có dạng s = c * log(1+ r)
        # Với s là điểm ảnh đã xử lý, r >= 0 là điểm ảnh đầu vào, c hằng số
        # Xem chi tiết tại IP3/Tr16
        if(value != 0):
            img = np.uint8(float(value) * cv2.log(1.0 + img))
        return img

    def change_Island(self, img, imgNotIsland, value):
        # Đảo ảnh với ảnh có các giá trị mức xám trong vùng [0, L – 1]
        # Là thao tác xử lý điểm ảnh trên ảnh có dạng s = (L – 1) – r
        if(value == 1):
            img = imgNotIsland
        else:
            img = 255 - img
        return img
