import cv2
import serial
import numpy as np
import matplotlib.pyplot as plt

# Configuración del puerto serial
puerto = serial.Serial("COM13", 115200, timeout=1)
lista = []

# Habilitamos el modo interactivo
plt.ion()

while True:
    # Leer valor desde el puerto serial
    valor = puerto.readline().decode().strip()
    if not valor:
        continue

    #valor lo convertimos a entero para lograr hacer la sumatoria dinamica del grafico de barras
    valor = int(valor)

    lista.append(valor)
    if len(lista) > 10:
        lista.pop(0)

    # Crear la figura con dos subgráficos
    figura, (gr_lineas, gr_barras) = plt.subplots(2, 1, figsize=(10, 5))
    figura.subplots_adjust(hspace=0.4)

    # Grafico de lineas
    gr_lineas.plot(range(len(lista)), lista, marker='o', color='b', linewidth=2)
    gr_lineas.set_xlabel('Microcontrolador')
    gr_lineas.set_ylabel('Valores')
    gr_lineas.set_title('Gráfico de Líneas')
    gr_lineas.set_ylim(0,100)
    gr_lineas.set_xlim(0,9)
    gr_lineas.grid(True)

    # Grafico de barras
    grafico = gr_barras.bar(range(len(lista)), lista, color="#C5144C")
    gr_barras.set_xlabel('Sensor')
    gr_barras.set_ylabel('Valores')
    gr_barras.set_ylim(0,100)
    gr_barras.set_xlim(0,9)
    gr_barras.set_title('Gráfico de Barras con OpenCV')
    gr_barras.grid(True)

    # Etiquetas sobre las barras
    for barra, valor_barra in zip(grafico, lista):
        gr_barras.text(
            barra.get_x() + barra.get_width() / 2,
            valor_barra + 1,  # desplazamiento proporcional
            f"{valor_barra:.1f}",
            ha="center",
            va="bottom",
            fontsize=9,
            color="black"
        )

    # Convertir figura a imagen para OpenCV
    figura.canvas.draw()
    imagen = np.array(figura.canvas.buffer_rgba())
    imagen = cv2.cvtColor(imagen, cv2.COLOR_RGBA2BGRA)

    # Mostrar en ventana de OpenCV
    cv2.imshow("Valores desde ESPMane", imagen)

    # Esperar tecla y refrescar
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

    # Cerrar la figura actual para evitar sobrecarga de memoria
    plt.close(figura)

puerto.close()
cv2.destroyAllWindows()
