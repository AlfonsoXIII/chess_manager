import cv2

img = cv2.imread("images/chess_pieces_1.png")
crop_img = img[0:136, 0:136]
crop_img = cv2.resize(crop_img, (100, 100), interpolation = cv2.INTER_NEAREST)
cv2.imshow("cropped", crop_img)
cv2.waitKey(0)