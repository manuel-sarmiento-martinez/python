import datetime

ahora = datetime.datetime.now()

print("Dia: " + ahora.strftime("%d"))
print("Mes: " + ahora.strftime("%B"))
print("Año: " + ahora.strftime("%Y"))
print("Hora: " + ahora.strftime("%H") + " minuto: " + ahora.strftime("%M"))
