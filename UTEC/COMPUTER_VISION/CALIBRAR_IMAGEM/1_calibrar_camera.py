# ---------------------------------------------------------------------------------------------
# UTEC - Pós Graduação em Robótica e Inteligência Artificial
# Disciplina: Visão Computacional
# Aluno: Alexandre Ferreira e Silva
# TAREFA 2 - CALIBRAÇÃO DE IMAGEM
# ---------------------------------------------------------------------------------------------

import cv2
import numpy as np
import glob
import os

os.system('cls') # limpar console

# Parâmetros do tabuleiro de xadrez
chessboard_size = (9,6)  # Número de cantos internos no tabuleiro (largura x altura)

# Preparar pontos do objeto 3D
objp = np.zeros((np.prod(chessboard_size), 3), dtype=np.float32)
objp[:, :2] = np.indices(chessboard_size).T.reshape(-1, 2)

# Listas para armazenar pontos do objeto 3D e pontos da imagem 2D
object_points = []
image_points = []

BASE_DIR = 'C:\\projetos\\mestrado-unifesp\\UTEC\\COMPUTER_VISION\\CALIBRAR_IMAGEM\\img_calibrar_camera_weg\\'
list_of_image_files = glob.glob(BASE_DIR + '*.jpeg')

if len(list_of_image_files) == 0:
    raise Exception('ERROR - VERIFIQUE O CAMINHO DAS IMAGENS E EXTENSAO DOS ARQUIVOS')

# Carregar e processar cada imagem
for image_file in list_of_image_files:
    image = cv2.imread(image_file)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detectar cantos do tabuleiro de xadrez
    ret, corners = cv2.findChessboardCorners(gray, chessboard_size, None)
    print('ret', ret)

    # Se os cantos forem encontrados, adicione os pontos do objeto e da imagem
    if ret:
        object_points.append(objp)
        image_points.append(corners)

        # Desenhar e exibir os cantos
        cv2.drawChessboardCorners(image, chessboard_size, corners, ret)
        cv2.imshow('Imagem', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

cv2.destroyAllWindows()

# Calibrar a câmera
ret, K, dist, rvecs, tvecs = cv2.calibrateCamera(
    object_points, image_points, gray.shape[::-1], None, None
)

print("\n===== MATRIZ INTRÍNSECA =====")
print(K)

print("\n===== COEFICIENTES DE DISTORÇÃO =====")
print(dist)

print("\n===== VETORES EXTRÍNSECOS =====")
print("Rotação:")
print(rvecs)

print("\nTranslação:")
print(tvecs)

print("\n===== ERRO DE REPROJEÇÃO =====")
print(ret)

# salvar matrizes de calibração
np.savez('B.npz', K, dist)

# Carregar uma imagem de teste
FOTO = '3831ac803c5c 10.1.79.41_2025-08-1_15-51-2-5667.jpeg'
test_image = cv2.imread(BASE_DIR + FOTO)

# Corrigir a distorção da imagem
undistorted_image = cv2.undistort(test_image, K, dist, None, K)

cv2.imwrite(BASE_DIR + 'CORRIGIDO_' + FOTO, undistorted_image)

# Exibir a imagem original e a imagem corrigida lado a lado
combined_image = np.hstack((test_image, undistorted_image))
cv2.imshow('Original vs Undistorted', combined_image)
cv2.waitKey(0)
cv2.destroyAllWindows()