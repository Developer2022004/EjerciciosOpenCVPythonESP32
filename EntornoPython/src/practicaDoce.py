import cv2
import matplotlib.pyplot as plt
import json
import serial
import numpy as np

#deque permite crear listas de manera circular
from collections import deque

puerto = serial.Serial("COM11",115200,timeout=1)
transmitiendo = False
ancho, alto = 800, 600

valor_uno = deque(maxlen=100)
valor_dos = deque(maxlen=100)

#Desactivamos el modo interactivo
plt.ioff()
figura, (ax,bx) = plt.subplots(2,1,figsize=(8,6))
figura.subplots_adjust(hspace=0.4)

ax.set_title("valor uno")
ax.set_ylim(0,100)
ax.set_xlim(0,100)
ax.set_ylabel("Valores")
ax.grid(True)

bx.set_title("valor dos")
bx.set_ylim(0,100)
bx.set_xlim(0,100)
bx.set_ylabel("Valores")
bx.grid(True)

#Creamos el plot.   
linea_uno, = ax.plot([],[],color='red',linewidth=2)
linea_dos, = bx.plot([],[],color='blue',linewidth=2)

fondo = np.ones((alto,ancho,3),dtype=np.uint8) * 255

texto = "Presiona i inicia el grafico, con o se detiene el grafico y con q termino,"

cv2.putText(fondo,texto,(50,alto//2),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,0),2)

while True:
    #preparamos la lectura de teclas para cerrar la ventana
    key = cv2.waitKey(25) & 0xFF
    
    #validamos la tecla para habilitar el envio de datos
    if key == ord('i'):
        transmitiendo = True
        puerto.write(b'1')
        
    if key == ord('o'):
        transmitiendo = False
        puerto.write(b'1')
        
    if key == ord('q'):
        
        transmitiendo = False
        
        break
    
    if transmitiendo and puerto.in_waiting:
        try:
            dato = puerto.readline().decode('utf-8"').strip()
            #print(dato)
            if not dato:
                continue
            datos = json.loads(dato)
            #print(datos)
            #validamos que el json llegue de manera correcta esto a causa de que no siempre se envian valores
            if not isinstance(datos,dict) or "valores" not in datos:
                continue
            valores = datos.get("valores",[])
            if not isinstance(valores,(list,tuple)) or len(valores) != 2:
                continue
            
            #guardamos los datos
            v1,v2 = valores
            
            #cargamos a las listas deque estos son x,y
            valor_uno.append(v1)
            valor_dos.append(v2)
            
            # print(valor_uno)
            #cargamos los valores a las graficas con set_data()
            linea_uno.set_data(range(len(valor_uno)),list(valor_uno))
            linea_dos.set_data(range(len(valor_dos)),list(valor_dos))
            
            #cargamos las graficas
            figura.canvas.draw()
            
            img = np.array(figura.canvas.buffer_rgba())
            img = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
            img = cv2.resize(img,(ancho,alto))
            
            cv2.imshow("Graficas valores",img)
        except Exception as e:
            print(e)
            continue
    elif not transmitiendo:
        cv2.imshow("Graficas Valores",fondo)

#Cerramos la conexion
puerto.close()
cv2.destroyAllWindows()