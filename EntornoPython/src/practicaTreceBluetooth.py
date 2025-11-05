import cv2
import serial
import numpy as np

#TAREA AGREGAR 2 GRAFICOS (GRAFICO DE LINEAS EN LA PARTE SUPERIOR Y GRAFICO DE BARRAS EN LA PARTE INFERIOR)

lista = []
puerto = serial.Serial("COM13",115200,timeout=1)
ancho,alto = 800,600
fondo = np.ones((alto,ancho,3),dtype=np.uint8) * 255

while True:
    valor = puerto.readline().decode().strip()
    if not valor:
        continue
    lista.append(valor)
    if len(lista) > 10:
        lista.pop(0)
    
    cv2.putText(fondo,str(lista),(50,alto//2),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,0),2)
    cv2.imshow("Valores desde ESPMane",fondo)
    
    #preparamos la lectura de teclas para cerrar la ventana
    key = cv2.waitKey(25) & 0xFF
    
    if key == ord('q'):
        break

puerto.close()
cv2.destroyAllWindows()
    


