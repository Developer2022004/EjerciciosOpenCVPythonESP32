import serial
import numpy as np
import cv2
import matplotlib.pyplot as plt 

import json

puerto = serial.Serial("COM11",115200)
plt.ion() #Lo habilitamos en modo interactivo
lista = []
contador_lista = 0

while(True):
    try:
        linea = puerto.readline().decode().strip()
        if not linea:
            continue
        
        objeto = json.loads(linea)
        print(objeto)
        
        valor = objeto["values"]
        #agregamos los elementos capaturados del json.loads
        lista.append(valor)
        
        if len(lista) > 5: # el 100 tiene relacion con el tamaño de StaticJsonDocument<100> de ArduinoJson ya que esto indica las graficas que debe colocar
            lista.pop(0)
            
    
        figura, ax = plt.subplots()
        # grafico = ax.plot(lista,color="#C5144C") #Grafica lineal
        # ax.set_ylim(0,200) #Establece los limite de las coordenadas Y
        grafico = ax.bar(range(len(lista)),lista,color="#C5144C")
        ax.set_ylim(0,200)
        
        # for grafico, lista in zip(grafico,lista):
        #     print(grafico.get_x())
        #     ax.text(grafico.get_x() + grafico.get_width() /2,
        #             lista + 1, str(lista), ha="center",va="bottom",fontsize=10,color="black")

        for _grafico_barra, _lista_objeto in zip(grafico,lista):
            print(_grafico_barra.get_x())
            ax.text(_grafico_barra.get_x() + _grafico_barra.get_width() /2,
                    _lista_objeto + 1, str(_lista_objeto), ha="center",va="bottom",fontsize=10,color="black")

        
        ax.set_xlabel('Sensor')
        ax.set_ylabel('Valores')
        ax.set_title('Grafico de barras con OpenCV')

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

