import cv2
import serial
import numpy as np
import matplotlib.pyplot as plt

# Para habilitar puertos
import socket

ipESP32 = "192.168.100.38"
puerto_servidor = 8888

#Habilitamos puertos del servidor
servidor = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#Luego buscamos el servidor para conectar
servidor.connect((ipESP32,puerto_servidor))

#Creamos la lista para guardar los valores
lista = []

while True:
    
    try:
        dato = servidor.recv(1024).decode("utf-8").strip()
    
        if not dato:
            continue
    
        print(dato)
        lista.append(dato)
        
        if len(lista) >= 10:
            break
        
    except Exception as e:
        print(f"Error: {e}")

#Cerramos la comunicacion
servidor.close()



