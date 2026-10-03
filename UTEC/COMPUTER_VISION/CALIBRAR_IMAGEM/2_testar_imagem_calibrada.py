import cv2
import numpy as np
import glob

'''
Matriz de calibração K:\n [[ 2.58500350e+03  0.00000000e+00  6.15331663e+02]
 [ 0.00000000e+00  2.74172063e+03 -1.75197739e+02]
 [ 0.00000000e+00  0.00000000e+00  1.00000000e+00]]
Distorção: [ -0.34256418   8.96617195  -0.11993818  -0.03751211 -35.88274689]
'''

# Carregar uma imagem de teste
test_image = cv2.imread(BASE_DIR +'3831ac803c5c 10.1.79.41_2025-08-1_15-51-20-4848.jpeg')

# Corrigir a distorção da imagem
K = cv2.Mat(np.array([[2.58500350e+03,0.00000000e+00,6.15331663e+02], [0.00000000e+00,2.74172063e+03,-1.75197739e+02], [0.00000000e+00, 0.00000000e+00, 1.00000000e+00]]))
dist = cv2.Mat(np.array([ -0.34256418,   8.96617195,  -0.11993818,  -0.03751211, -35.88274689]))

undistorted_image = cv2.undistort(test_image, K, dist, None, K)

#cv2.imwrite('C:\\Users\\e-alexandres\\projetos\\sinterizacao\\python_pixel_mm\\img3\\3831ac803c5c 10.1.79.41_2025-08-1_15-51-34-1857_CORRIGIDO.jpeg', undistorted_image)
cv2.imwrite('C:\\Users\\e-alexandres\\projetos\\sinterizacao\\python_pixel_mm\\visao\\webcam\\imagem_teste_corrigido.jpg', undistorted_image)

# Exibir a imagem original e a imagem corrigida lado a lado
combined_image = np.hstack((test_image, undistorted_image))
cv2.imshow('Original vs Undistorted', combined_image)
cv2.waitKey(0)
cv2.destroyAllWindows()