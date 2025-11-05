import cv2
import matplotlib.pyplot as plt 
import numpy as np 
import random as rd

#Construyendo un grafico de barras
ejesx = ['A','B','C','D']
ejesy = []

for i in range(1,5):
    ejesy.append(rd.randint(1,100))
    # print(i)
print(ejesy)

figura, ax = plt.subplots()
grafico = ax.bar(ejesx,ejesy,color="#C5144C")
# ax.bar(ejesx,ejesy,color="#C5144C")

#para que sirve zip() y busca documentacion de matplotlib

for grafico, ejesy in zip(grafico,ejesy):
    ax.text(grafico.get_x() + grafico.get_width() /2,
                  ejesy + 1, str(ejesy), ha="center",va="bottom",fontsize=10,color="black")

ax.set_xlabel('Ejes X')
ax.set_ylabel('Ejes y')
ax.set_title('Grafico de barras con OpenCV')

figura.canvas.draw()
imagen = np.array(figura.canvas.buffer_rgba())
imagen = cv2.cvtColor(imagen,cv2.COLOR_RGBA2BGRA)
cv2.imshow('Grafico con OpenCV',imagen)

cv2.waitKey(0)
cv2.destroyAllWindows()