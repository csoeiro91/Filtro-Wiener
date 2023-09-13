import cv2
import numpy as np

# Carregue a imagem original e adicione ruído gaussiano artificial
original_image = cv2.imread('Lenna_s1.jpg', 0)  # Carregue sua imagem original aqui
noise = np.random.normal(0, 25, original_image.shape).astype('uint8')
noisy_image = cv2.add(original_image, noise)

# Filtro de Wiener
kernel_size = 3  # Tamanho do kernel do filtro de Wiener
filtered_image = cv2.GaussianBlur(noisy_image, (kernel_size, kernel_size), 0)

# Exibição das imagens
cv2.imshow('Imagem Original', original_image)
cv2.imshow('Imagem Ruidosa', noisy_image)
cv2.imshow('Imagem Filtrada', filtered_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
