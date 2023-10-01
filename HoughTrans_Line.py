import cv2
import numpy as np

# Load image and convert to grayscale
img = cv2.imread('C:/Users/NHI658/Desktop/HoughTrans/image3.jpg', 0)
#cv2.imshow('img',img)
#gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply edge detection
edges = cv2.Canny(img, 50, 150, apertureSize=3)

# Apply Hough transform
lines = cv2.HoughLines(edges, rho=1, theta=np.pi/180, threshold=100)

if lines is not None and len(lines) > 0:
#if lines:
# Draw detected lines on the original image
    for line in lines:
        rho, theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))
        cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

# Display the result
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

