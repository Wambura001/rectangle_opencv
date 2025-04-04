import cv2

path = r"C:\Users\USER\Pictures\Screenshots\Screenshot 2025-03-15 161038.png"
image = cv2.imread(path)
cv2.imshow('Original Image', image)

imageRect = image.copy()
imageRect = cv2.rectangle(imageRect, (500, 100), (700, 600), (255, 0, 255), thickness = 5, lineType = cv2.LINE_8)

cv2.imshow('Rectangle Image', imageRect )
cv2.waitKey(0)
cv2.destroyAllWindows()