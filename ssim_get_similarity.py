import cv2 as cv2
from skimage.measure import compare_ssim
import imutils

image1 = cv2.imread("D:\\SourceCode\\github\\image_similiarity_plus\\demo\\chen.jpg")
image2 = cv2.imread("D:\\SourceCode\\github\\image_similiarity_plus\\demo\\chen2.jpg")

gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

(score, diff) = compare_ssim(gray1, gray2, full=True)
diff = (diff * 255).astype("uint8")
print("SSIM: {}".format(score))



