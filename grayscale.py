import cv2
import matplotlib.pyplot as plt
import matplotlib.image as img

image1 = cv2.imread(".\\image1.jpg", 0)
image = img.imread(".\\image1.jpg")

plt.subplot(221), plt.imshow(image)
plt.subplot(222), plt.imshow(image1, 'gray')
plt.subplot(223), plt.imshow(image1.ravel(), 256, [0, 255])
plt.xlim([0, 256])
plt.show()

