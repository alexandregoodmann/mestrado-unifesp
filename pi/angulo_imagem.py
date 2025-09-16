import cv2
import numpy as np

# Carregar imagem e binarizar
img = cv2.imread("lights.jpg", 0)
_, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# Encontrar contornos
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print(contours)
cnt = contours[0]

# Calcular momentos
M = cv2.moments(cnt)
angle = 0.5 * np.arctan2(2*M['mu11'], (M['mu20'] - M['mu02']))
angle_deg = np.degrees(angle)

print("Ângulo de rotação:", angle_deg)

cv2.imshow('Imagem Original', img)
cv2.waitKey(0)
cv2.destroyAllWindows()