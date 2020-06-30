# Python Program to Get IP Address 
import socket
import re, uuid
import os
import subprocess
import psutil
import string
import os.path
import shutil


#obtencion de la MacAddres de la tarjeta de red
macAdd = (':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff) for ele in range(0,8*6,8)][::-1]))
#obtencion del nombre
hostname = socket.gethostname()
#obtencion de la IP
IPAddr = socket.gethostbyname(hostname)

#Funcion para obtener el uso del disco
disk_usage = psutil.disk_usage("C:\\")

def to_gb(bytes):
    "Convierte bytes a gigabytes."
    return bytes / 1024**3
        

# verificacion, creacion y escaneo
if os.path.isdir("C:/Users/Keymera/INv/"):
    print('La carpeta existe.')
else:
    print('La carpeta no existe.')
    os.mkdir("C:/Users/Keymera/INv")
    file = open("C:/Users/Keymera/INv/scan.txt", "w")
    
    file.write("Hotname:" + hostname + "\n")
    file.write("IP_Address:" + IPAddr + "\n")
    file.write("MAC_address :" + macAdd + "\n")

    file.write("Espacio total: {:.2f} GB.".format(to_gb(disk_usage.total)) + "\n")
    file.write("Espacio libre: {:.2f} GB.".format(to_gb(disk_usage.free)) + "\n")
    file.write("Espacio usado: {:.2f} GB.".format(to_gb(disk_usage.used)) + "\n")
    file.write("Porcentaje de espacio usado: {}%.".format(disk_usage.percent) + "\n")
    
    file.write("discos y numero de serie encontrados" + "\n")
    file.close()
    # captacion del serial del disco HDD o SDD
    os.system("wmic diskdrive get caption,serialnumber >> C:/Users/Keymera/INv/scan.txt")
    #os.system("wmic diskdrive get caption,serialnumber")
    # obtencion del estado del disco
    os.system("wmic diskdrive get status >> C:/Users/Keymera/INv/scan.txt")
    #os.system("wmic diskdrive get status")

if os.path.isfile("C:/Users/Keymera/INv/scan.txt"):
    print('El archivo existe.')
else:
    print('El no archivo existe.')
    file = open("C:/Users/Keymera/INv/scan.txt", "w")
    file.write("Hotname:" + hostname + "\n")
    file.write("IP_Address:" + IPAddr + "\n")
    file.write("MAC_address :" + macAdd + "\n")
    
    file.write("Espacio total: {:.2f} GB.".format(to_gb(disk_usage.total)) + "\n")
    file.write("Espacio libre: {:.2f} GB.".format(to_gb(disk_usage.free)) + "\n")
    file.write("Espacio usado: {:.2f} GB.".format(to_gb(disk_usage.used)) + "\n")
    file.write("Porcentaje de espacio usado: {}%.".format(disk_usage.percent) + "\n")
    
    file.close()
    # captacion del serial del disco HDD o SDD
    os.system("wmic diskdrive get caption,serialnumber >> C:/Users/Keymera/INv/scan.txt")
    #os.system("wmic diskdrive get caption,serialnumber")
    # obtencion del estado del disco
    os.system("wmic diskdrive get status >> C:/Users/Keymera/INv/scan.txt")
    #os.system("wmic diskdrive get status")


if os.path.isdir("C:/scan"):
    print('La carpeta existe.')
    if os.path.isfile("C:/scan/scan.py"):
        print('El archivo existe.')
    else:
        print('El no archivo existe.')
        shutil.move("D:/Escitorio/login2/login/app/scan.py", "C:/scan")
else:
    print('La carpeta no existe.')
    os.mkdir("C:/scan")
    shutil.move("D:/Escitorio/login2/login/app/scan.py", "C:/scan")