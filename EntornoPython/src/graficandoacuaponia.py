import serial
import numpy as np
import cv2
import matplotlib.pyplot as plt
import time
import json

lista_temperatura = []
lista_solidos = []
lista_conductividad = []

# Configurar la conexión serial
puerto = serial.Serial('COM12', 115200)
plt.ion()  # Modo interactivo de matplotlib

while True:
    try:
        linea = puerto.readline().decode('utf-8').strip()
        if not linea:
            continue
        objeto = json.loads(linea)
        print(objeto)
        
        foto_celda = objeto['foto_celda']
        
        lista_temperatura.append(objeto['temp'])
        ejerx = objeto['labels']
        ejery= objeto['temp']
        if len(lista_temperatura) > 5:
            lista_temperatura.pop(0)
            
        lista_solidos.append(objeto['tds'])
        ejerx = objeto['labels']
        ejery= objeto['tds']
        
        lista_conductividad.append(objeto['conductividad'])
        ejerx = objeto['labels']
        ejery= objeto['conductividad']
        if len(lista_conductividad) > 10:
            lista_conductividad.pop(0)
            
        fig, graf = plt.subplots(2,2, figsize=(10,5))
        ax = graf[0,0]
        bx = graf[0,1]
        cx = graf[1,0]
        dx = graf[1,1]
        
        # # GRAFICA DE PASTEL
        foto_celda_nuevo = 400 - foto_celda
        bx.set_title('Grafica de Pastel Foto Celda')
        bx.pie([foto_celda_nuevo, foto_celda], labels=['Valor restante', 'Valor actual'], colors=['#C5144C', '#14C57F'],
               autopct='%1.1f%%')
        

        # GRAFICA DE BARRAS
        grafica = ax.bar(range(len(lista_temperatura)),lista_temperatura, color="#C5144C")
        # grafica = ax.plot(lista, color="#C5144C") 
        ax.set_ylim(0,100)
        for barra, valor in zip(grafica, lista_temperatura):
            ax.text(barra.get_x() + barra.get_width() / 2, valor,
                    str(valor), ha='center', va='bottom', color='black', fontsize=10)
        
        ax.set_xlabel('Intento_captura')
        ax.set_ylabel('Temperatura')
        ax.set_title('Grafica de Barras')

        # # GRAFICA DE lineas
        grafica_lineas = cx.plot(lista_solidos, color="#C5144C") 
        cx.set_ylim(0,1200)
        cx.set_xlabel('Captura')
        cx.set_ylabel('ppm')
        cx.set_title('Grafica de Lineas')

        # # GRAFICA DE puntos
        grafica_puntos = dx.scatter(range(len(lista_conductividad)), lista_conductividad, color="#C5144C")
        dx.set_ylim(0,1800)
        dx.set_xlabel('Sensor')
        dx.set_ylabel('uS/CM')
        dx.set_title('Grafica de Puntos Conductividad')

        fig.canvas.draw()
        img = np.array(fig.canvas.buffer_rgba())
        img = cv2.cvtColor(img, cv2.COLOR_RGBA2BGRA)
        cv2.imshow("Grafica de Barras", img)
        cv2.waitKey(1)
        plt.close(fig)


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    except json.JSONDecodeError:
        print("Error al decodificar JSON:", linea)
    except Exception as e:
        print("Error:", e)
        break
puerto.close()
cv2.destroyAllWindows()