import cv2


def clmap(v, k, upBound):  # mul and clamp
    val = v * k
    if val > upBound:
        return upBound
    else:
        return val

#inImage_1 = './tests/bathroom2-mmlt_m150_3503s.png'  #
#inImage_1 = './tests/bathroom2-pfmlt_m280_3805s.png'  #
#inImage_2 = './tests/reference/bathroom2-reference.png'  #

#inImage_1 = './tests/bidir_mmlt_m75_1441s.png'  #
#inImage_1 = './tests/bidir_pfmlt_m45_1448s.png'  #
#inImage_2 = './tests/reference/bidir-reference.png'  #

#inImage_1 = './tests/breakfast-lamps_mmlt_m150_7353s.png'  #
#inImage_1 = './tests/breakfast-lamps_pfmlt_m100_7166s.png'  #
#inImage_2 = './tests/reference/breakfast-lamps-reference.png'  #

#inImage_1 = './tests/living-room_mmlt_m670_6621s.png'  #
inImage_1 = './tests/living-room_pfmlt_m310_6629s.png'  #
inImage_2 = './tests/reference/living-room-reference.png'  #

#inImage_1 = './tests/villa-daylight_mmlt_m200_5580s.png'  #
#inImage_1 = './tests/villa-daylight_pfmlt_m80_5372s.png'  #
#inImage_2 = './tests/reference/villa-daylight-reference.png'  #


colourbar = './colourbar.jpg'  #

dif_img = 'dif_' + inImage_1

img_1 = cv2.imread(inImage_1)  # read as color image
img_2 = cv2.imread(inImage_2)

img_colourbar = cv2.imread(colourbar)

dif = img_1.copy()
show_dif = dif.copy()  # dif image for show only

width = img_1.shape[0]  # get width
height = img_1.shape[1]  # get height

cwidth = img_colourbar.shape[0]  # get width
cheight = img_colourbar.shape[1]  # get height

sum = 0

for i in range(width):
    for j in range(height):

        y1 = img_1[i, j][2] * 0.212671 + img_1[i, j][1] * 0.715160 + img_1[i, j][0] * 0.072169
        y2 = img_2[i, j][2] * 0.212671 + img_2[i, j][1] * 0.715160 + img_2[i, j][0] * 0.072169
        diff = y1 - y2
        diff0 = diff

        sum = sum + abs(diff) ** 2

        diff0 = clmap(abs(diff0), 5, 255)
        pos = int((abs(diff0) / 255.0) * (cheight - 10))
        show_dif[i, j] = img_colourbar[0, pos]

        dif[i, j] = abs(diff0)

mse = sum / (width * height)
print 'MSE: ', mse

print dif_img
print 'different data:'
print 'max : ', dif.max()
print 'min : ', dif.min()
print 'mean : ', dif.mean()

cv2.imwrite(dif_img, show_dif)

cv2.imshow('_dif', show_dif)
cv2.waitKey(0)
cv2.destroyAllWindows()
