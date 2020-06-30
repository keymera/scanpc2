from datetime import datetime, date, time, timedelta
import calendar


ahora = datetime.now()  # Obtiene fecha y hora actual
print("Fecha y Hora:", ahora)  # Muestra fecha y hora
print("Fecha y Hora UTC:",ahora.utcnow())  # Muestra fecha/hora UTC
print("Día:",ahora.day)  # Muestra día
print("Mes:",ahora.month)  # Muestra mes
print("Año:",ahora.year)  # Muestra año
print("Hora:", ahora.hour)  # Muestra hora
print("Minutos:",ahora.minute)  # Muestra minuto
print("Segundos:", ahora.second)  # Muestra segundo
print("Microsegundos:",ahora.microsecond)  # Muestra microsegundo



print("Horas:")
hora1 = time(10, 5, 0)  # Asigna 10h 5m 0s
print("\tHora1:", hora1)
hora2 = time(23, 15, 0)  # Asigna 23h 15m 0s
print("\tHora2:", hora2)

# Compara horas
print("\tHora1 < Hora2:", hora1 < hora2)  # True

print("Fechas:")
fecha1 = date.today()  # Asigna fecha actual
print("\tFecha1:", fecha1)

# Suma a la fecha actual 2 días
fecha2 = date.today() + timedelta(days=2)
print("\tFecha2:", fecha2)
file = open("C:/scan"+ str (fecha2) +".txt", "w")

# Compara fechas
print("\tFecha1 > Fecha2:", fecha1 > fecha2)  # False