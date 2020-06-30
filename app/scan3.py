import socket
import re, uuid
import os
import subprocess
import psutil


disk_usage = psutil.disk_usage("C:\\")

def to_gb(bytes):
    "Convierte bytes a gigabytes."
    return bytes / 1024**3

"""macAdd = (':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff) for ele in range(0,8*6,8)][::-1]))
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

print("Hotname:" + hostname)
print("IP_Address:" + IPAddr)
print ("MAC_address :" + macAdd)
os.system("systeminfo")

print("discos y numero de serie encontrados")
os.system("wmic diskdrive get caption,serialnumber")
#sn=os.system("wmic diskdrive get caption,serialnumber")

os.system("wmic diskdrive get status")
#sts = os.system("wmic diskdrive get status")"""
print ("Estado del disco C:")


os.mkdir("C:/Users/Keymera/INv")
file = open("C:/Users/Keymera/INv/scan.txt", "w")
#obtencion de la MacAddres de la tarjeta de red
macAdd = (':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff) for ele in range(0,8*6,8)][::-1]))
#obtencion del nombre
hostname = socket.gethostname()
#obtencion de la IP
IPAddr = socket.gethostbyname(hostname)
#escritura al doc
file.write("Hotname:" + hostname + "\n")
file.write("IP_Address:" + IPAddr + "\n")
file.write("MAC_address :" + macAdd + "\n")

file.write("Espacio total: {:.2f} GB.".format(to_gb(disk_usage.total)) + "\n")
file.write("Espacio libre: {:.2f} GB.".format(to_gb(disk_usage.free)) + "\n")
file.write("Espacio usado: {:.2f} GB.".format(to_gb(disk_usage.used)) + "\n")
file.write("Porcentaje de espacio usado: {}%.".format(disk_usage.percent) + "\n")

file.close()