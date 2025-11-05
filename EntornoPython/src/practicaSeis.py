import serial
import numpy as np
import cv2
import matplotlib.pyplot as plt 

import json

puerto = serial.Serial("COM11",115200)
plt.ion() #Lo habilitamos en modo interactivo

while(True):
    try:
        linea = puerto.readline().decode().strip()
        if not linea:
            continue
        
        objeto = json.loads(linea)
        print(objeto)
        
        ejesx = objeto['labels']
        ejesy = objeto['values']
    
        figura, ax = plt.subplots()
        grafico = ax.bar(ejesx,ejesy,color="#C5144C")
        
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
        cv2.waitKey(1)
        plt.close(figura)
        
        #para deterner la ejecucion de lectura del serial y kernel de python
        #waitKey retorna el codigo asccii de la tecla presionada o indicada
        if cv2.waitKey(25) & 0xFF == ord('q'): 
            break
            
    except json.JSONDecodeError as e:
        print("Error de json ",e)
    except Exception as e:
        print("Error",e)
        break
    
cv2.destroyAllWindows()

