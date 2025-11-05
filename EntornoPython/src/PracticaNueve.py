import serial
import numpy as np
import cv2
import matplotlib.pyplot as plt 

import json

puerto = serial.Serial("COM11",115200)
plt.ion() #Lo habilitamos en modo interactivo
contador_lista = 0

while(True):
    try:
        linea = puerto.readline().decode().strip()
        if not linea:
            continue
        
        objeto = json.loads(linea)
        print(objeto)
        
        valor = objeto["values"]
        
        figura, ax = plt.subplots()
        ax.set_ylim(0,200) # el 200 es el valor al cual se mapea el potenciometro
        valor_nuevo = 200 - valor
        ax.pie([valor,valor_nuevo],labels=["Potenciometro","Restante"],autopct="%1.1f%%") #Grafica de Tipo Pie
        ax.set_xlabel('Sensor')
        ax.set_ylabel('Valores')
        ax.set_title('Grafico de Pie con OpenCV')

        figura.canvas.draw()
        imagen = np.array(figura.canvas.buffer_rgba())
        imagen = cv2.cvtColor(imagen,cv2.COLOR_RGBA2BGRA)
        cv2.imshow('Grafico con OpenCV',imagen)
        
        cv2.waitKey(1) #Captura la tecla mediante la interfas de openCV
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
    
puerto.close()
cv2.destroyAllWindows()

