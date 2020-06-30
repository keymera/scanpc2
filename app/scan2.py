import psutil
import os
import string
# detecta cantodad de unidades
#uni = os.system("fsutil fsinfo drives")


#SN = os.system("wmic diskdrive C: get caption,serialnumber")
#print(" " + SN)
#lo siguiente me indica indica la info de la unidad especifica
# Indicamos la ruta del disco.
disk_usage = psutil.disk_usage("C:\\")

def to_gb(bytes):
    "Convierte bytes a gigabytes."
    return bytes / 1024**3

print("Espacio total: {:.2f} GB.".format(to_gb(disk_usage.total)))
print("Espacio libre: {:.2f} GB.".format(to_gb(disk_usage.free)))
print("Espacio usado: {:.2f} GB.".format(to_gb(disk_usage.used)))
print("Porcentaje de espacio usado: {}%.".format(disk_usage.percent))