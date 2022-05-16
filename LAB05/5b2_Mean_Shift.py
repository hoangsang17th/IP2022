import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from sklearn.mixture import GaussianMixture

# Download image  
img = cv2.imread('test1.tif', 0)
# Gray convert COLOR_RGB2GRAY
X = img.reshape(-1, 3)


em = GaussianMixture(n_components=3,
              covariance_type='full', max_iter=20, random_state=0).fit(X)

pred_label = em.predict(X)

# Reshape pred_label
X_img = pred_label.reshape(img.shape[:2])

# Display image clustering
fg, ax = plt.subplots(1, 2, figsize = (8, 4))
for i, image in enumerate([img, X_img]):
  ax[i].imshow(image)
  if i == 0:
    ax[i].set_title('Origin Image')
  else:
    ax[i].set_title('EM  clustering Image')