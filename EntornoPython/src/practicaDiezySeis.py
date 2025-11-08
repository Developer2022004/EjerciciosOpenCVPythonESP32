import cv2
import socket
import numpy as np
import json

lista = []

#Habilitamos la captura de informacion en canal de broadcast
host = "0.0.0.0"
puerto = 5000

servidor= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((host,puerto))
servidor.listen(1)

#Para verificar si alguien se conecto
conexion, direccion_ip = servidor.accept()
print(f"Se conecto {direccion_ip}")

while True:
    try:
        dato = conexion.recv(1024).decode("utf-8").strip()
        if not dato:
            continue
        
        print(dato)
        #Guardamos en la lista
        lista.append(dato)
        if len(lista) > 5:
            break
        
    except Exception as e:
        print(f"Error {e}")

conexion.close()
servidor.close()