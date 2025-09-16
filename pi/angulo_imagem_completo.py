import cv2
import numpy as np

# --- 1. Carregar imagem ---
imagem1 = "./exercicios/Unifesp_secundaria_verde_negativo_RGB.png"
imagem2 = 'lights.jpg'
imagem3 = './imgs/Lenna.png'
img = cv2.imread(imagem3, 0)  # carregar em escala de cinza
_, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)  # binarizar

# Encontrar contornos
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnt = max(contours, key=cv2.contourArea)  # pega o maior objeto

# Criar uma imagem colorida para desenhar
output = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

# ================================
# MÉTODO 1: ORIENTAÇÃO PELOS MOMENTOS
# ================================
M = cv2.moments(cnt)
angle_moments = 0.5 * np.arctan2(2*M['mu11'], (M['mu20'] - M['mu02']))
angle_moments_deg = np.degrees(angle_moments)

print("Ângulo de rotação (Momentos):", angle_moments_deg)

# ================================
# MÉTODO 2: ORIENTAÇÃO COM PCA
# ================================
# Converter contorno em array 2D
data = cnt.reshape(-1, 2).astype(np.float32)

# Aplicar PCA
mean, eigenvectors = cv2.PCACompute(data, mean=np.array([]))

# O vetor principal (eigenvector[0]) indica a orientação
vx, vy = eigenvectors[0]
angle_pca = np.arctan2(vy, vx)
angle_pca_deg = np.degrees(angle_pca)

print("Ângulo de rotação (PCA):", angle_pca_deg)

# ================================
# DESENHAR RESULTADOS
# ================================
# Centro do objeto
cx, cy = mean[0]

# Vetor principal (em vermelho)
cv2.line(output, (int(cx), int(cy)), (int(cx + 100*vx), int(cy + 100*vy)), (0,0,255), 2)

# Mostrar resultados
cv2.imshow("Objeto e Orientação", output)
cv2.waitKey(0)
cv2.destroyAllWindows()
