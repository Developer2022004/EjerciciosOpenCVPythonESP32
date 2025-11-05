import cv2
import matplotlib.pyplot as plt 
import numpy as np 
import random as rd

lista_1 = []
lista_2 = []

#Se crea el contenido de la listas de manera dinamica mediante el uso de for in range asi como de random.
for i in range(1,5):
    lista_1.append(rd.randint(1,100))
    lista_2.append(rd.randint(1,100))

figura, auxiliar = plt.subplots()
auxiliar.plot(lista_1,lista_2,marker="o",linestyle='--')
figura.canvas.draw()

#numpy se utiliza para inicializar un objeto del tipo matriz en una lista
img = np.array(figura.canvas.buffer_rgba())

#Indicamos la colorimetria que empleara la grafica de los datos.
img = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
cv2.imshow('Grafico',img)

#Se activa la captura de tecla de la interfaz de openCV, misma que desencadenara el evento de cerrar y destruir la ventana.
cv2.waitKey(0)
cv2.destroyAllWindows()