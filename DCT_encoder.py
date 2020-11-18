import cv
import cv2
import numpy as np


def image2dct(input_image):
    img1 = cv2.imread(input_image, cv2.IMREAD_GRAYSCALE)  # read the image
    h, w = img1.shape[:2]  # to know the size
    vis0 = np.zeros((h, w), np.float32)
    vis0[:h, :w] = img1
    vis1 = cv2.dct(vis0)  # dct
    # print(vis1)
    vis2 = cv2.idct(vis1)  # inverse dct
    img2 = cv2.cvtColor(vis2, cv2.COLOR_GRAY2BGR)  # color space convertion
    cv2.imwrite('output_Lenna.jpg', img2)

# MAIN


image2dct('Lenna_jpg.jpg')


