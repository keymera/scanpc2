import datetime
import os.path, time

today = datetime.datetime.now()
day_of_year = (today - datetime.datetime(today.year, 1, 1)).days + 1

#print day_of_year
ruta = ("C:/Users/Keymera/test/filename"+str(day_of_year)+".txt")
print ("Ultima Modificacion: %s" % time.ctime(os.path.getmtime(ruta)))
print ("Creado: %s" % time.ctime(os.path.getctime(ruta)))
scan = day_of_year
da = day_of_year + 1
ds = day_of_year - scan
if str (da) == str(scan):
    print("el archivo se creo hoy")
    print ("Ultima Modificacion: %s" % time.ctime(os.path.getmtime(ruta)))
    print ("Creado: %s" % time.ctime(os.path.getctime(ruta)))
elif (ds < 0):
    print ("error")
else:
    print('el archivos tiene:'+ str (ds) +' dias de creado')
    print ("Ultima Modificacion: %s" % time.ctime(os.path.getmtime(ruta)))
    print ("Creado: %s" % time.ctime(os.path.getctime(ruta)))