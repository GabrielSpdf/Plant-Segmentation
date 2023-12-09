#Importacao das bibliotecas utilizadas
import numpy as np
import cv2

#Definicao da fonte
font = cv2.FONT_HERSHEY_COMPLEX

#Leitura de cada imagem
img_cropped = cv2.imread("plantImage.jpg")

img_gray = cv2.cvtColor(img_cropped, cv2.COLOR_BGR2GRAY) #Transformar a imagem de BGR para GRAY
img_blurred = cv2.GaussianBlur(img_gray, (5,5), 0) #Aplicar um filtro de blur

canny = cv2.Canny(image=img_blurred, threshold1=146, threshold2=340) #Aplicar filtro de deteccao de borda Canny 146 340

kernel = np.ones((5, 5), np.uint8) #Kernel para aplicar na dilatacao da imagem
img_dilate = cv2.dilate(canny, kernel, iterations=1) #Dilatacao da imagem

contoursImg = cv2.bitwise_and(img_cropped, img_cropped, mask=img_dilate) #Unir a imagem original com a mascara criada usando o operador AND

contours, hierarchy = cv2.findContours(img_dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) #Encontrar os contornos da imagem

areas = [] #Criar um vetor para armazenar a area de cada objeto encontrado

indice = 1 #Criar uma variavel para corrigir erro de indice devido a problemas com a area


#Looping para encontrar a area de cada objeto e enumerar cada um
for i, contorno in enumerate(contours):
    contorno_aproximado = cv2.approxPolyDP(contorno, 0.01 * cv2.arcLength(contorno, True), True) #Aproximacao do contorno usando o algoritmo de Douglas-Peucker

    #Para cada x e y encontrado no contorno aproximado, atribuir ao x e y do objeto atual
    for ponto in contorno_aproximado:
        x, y = ponto[0]

    area = cv2.contourArea(contorno) #Area do objeto atual
    real_area = area*(12.5664/79) #Aproximacao da area real
    areas.append(real_area) #Adicionar a area real ao vetor de armazenamento de area

    #Manualmente, corrigir um erro encontrado na imagem analisada
    if indice == 38 or indice == 42:
        indice+=1

    #Caso nao estejamos tratando do erro, adicionar o indice de cada objeto na imagem
    else:
        cv2.putText(img_cropped, str(indice), (x, y), font, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
        indice+=1

#Manualmente, corrigir um erro encontrado na imagem analisada
areas[28] += areas[37] #objeto29+objeto38
areas[36] += areas[41] #objeto37+objeto42

#Para todas as areas, mostrar no terminal qual o valor da area e qual o objeto que estamos tratando
for i, area in enumerate(areas):
    print(f"Objeto: {i+1} - Area: {round(area, 2)}mm2")

#Mostragem de cada imagem
cv2.imshow("Imagem", img_cropped)
cv2.imshow("Imagem2", contoursImg)

cv2.waitKey()