import numpy as np


def rgb2yuv(rgb_values):  # funcio rgb a yuv

    if len(rgb_values) == 3:  # comprobem que hi hagui 3 canals
        R = rgb_values[0]
        G = rgb_values[1]
        B = rgb_values[2]

        Y = round(0.299*R + 0.587*G + 0.114*B)  # fem la conversio
        U = round(-0.168736*R - 0.331264*G + 0.5*B +128)
        V = round(0.5*R - 0.418688*G - 0.081312*B +128)
        yuv = [Y, U, V]

        for i in range(0, len(yuv)):  # reajustem el valors que han superat els llindars 0 i 255
            if yuv[i]>255:
                yuv[i] = 255
            elif yuv[i]<0:
                yuv[i] = 0

        return yuv

    else:
       print("Input values are not as expected")
       return


def yuv2rgb(yuv_values):

    if len(yuv_values) == 3:

        Y = yuv_values[0]
        U = yuv_values[1]
        V = yuv_values[2]

        R = round(Y + 1.4075 * (V-128))
        G = round(Y - 0.3455 * (U-128) - (0.7169 * (V-128)))
        B = round(Y + 1.7790 * (U-128))
        rgb = [R, G, B]
        for i in range(0,len(rgb)):
            if rgb[i]>255:
                rgb[i] = 255
            elif rgb[i]<0:
                rgb[i] = 0
        return rgb

    else:
        print("Input values are not as expected")
        return


# MAIN
rgb_matrix = [0, 0, 255]
print(rgb_matrix)
yuv = rgb2yuv(rgb_matrix)
print(yuv)
rgb = yuv2rgb(yuv)
print(rgb)
