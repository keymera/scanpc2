import socket
import subprocess
import sys
import platform
import csv

puertos = open("puertos.csv","r")
puertos_csv = csv.reader(puertos)

if (platform.system()=="Windows"):
    subprocess.call('cls',shell=True)
else:
    subprocess.call('clear',shell=True)
print '-' * 60

ip = raw_input('Ingrese Host/IP en especifico: ')
host_name = socket.gethostbyaddr(ip)

try:
    inicio = int(input("Ingrese el puerto de inicio: "))
    fin = int(input("Ingrese el puerto final: "))
except:
    print("[!] Error")
    sys.exit(1)

print '-' * 60
print 'Pro favor espere, escaneando host remoto', ip
print "Escaneando desde el puerto %s al %s" %(inicio,fin)
print '-' * 60
print "***************** "+host_name[0]+" *****************"
print "\n"