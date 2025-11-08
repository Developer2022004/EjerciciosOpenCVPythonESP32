import cv2
import socket
import numpy as np
import matplotlib.pyplot as plt 

ancho, alto= 800, 600
fondo = np.ones((alto,ancho,3), dtype=np.uint8) * 255 

ipesp32 = "192.168.100.38"
puerto = 8888
servidor= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.connect((ipesp32,puerto))
lista =[]
while True:
    try:
        dato = servidor.recv(1024).decode().strip()
        if not dato:
            continue
        
        dato = int(dato)
        
        #print(dato)
        fondo = np.ones((alto,ancho,3), dtype=np.uint8) * 255
        cv2.putText(fondo, str(dato), (ancho//2,(alto//2)-100),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,0),2) 
        lista.append(dato)
        
        #Construccion del grafico de barras
        figura, ax = plt.subplots()
        grafico = ax.bar(range(len(lista)),lista,color="#C5144C")
        ax.set_ylim(0,255)
        
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
        
        cv2.imshow("Valores desde ESPROA", imagen)
        #if len(lista)>=10:
            #break
        key = cv2.waitKey(25) & 0xFF 
        if  key == ord('q'):
            break
    
    except Exception as e:
        print("Error",e)
        
servidor.close()
cv2.destroyAllWindows()