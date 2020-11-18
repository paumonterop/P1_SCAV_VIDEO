import cv
import cv2
import cv as cv
import numpy as np

img1 = cv2.imread('Lenna_jpg.jpg', cv2.IMREAD_GRAYSCALE)
h, w = img1.shape[:2]
vis0 = np.zeros((h, w), np.float32)
vis0[:h, :w] = img1
vis1 = cv2.dct(vis0)
#print(vis1)
img2 = np.zeros((vis1.shape[0], vis1.shape[1], 3), dtype=np.float32)
img2 = cv2.cvtColor(vis1, cv2.COLOR_GRAY2BGR)

cv2.imwrite('output_Lenna.jpg', img2)
