import cv2

# PEGANDO A IMAGEM ORIGINAL E MOSTRANDO ELA
imageOriginal = cv2.imread("img/praia_invertida.png")
cv2.imshow("Original", imageOriginal)

# DIMINUINDO O TAMANHO DA IMAGEM EM 30% DO TAMANHO.
imageResized = cv2.resize(imageOriginal, None, fx = 0.3, fy = 0.3)
cv2.imshow("ImgResized", imageResized)

# EIXOS
height = imageResized.shape[0]
width = imageResized.shape[1]
middle = (width/2, height/2)

# CENTRO, ANGULO E ESCALA
matrix = cv2.getRotationMatrix2D(middle, 180,1)

# ROTACIONANDO A IMAGEM
imageRotate = cv2.warpAffine(imageResized, matrix,(width, height)) 
cv2.imshow("ImgRotate", imageRotate)

cv2.waitKey()