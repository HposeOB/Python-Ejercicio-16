import time

hora_actual = time.strftime("%H")
horas_restantes = 18 - int(hora_actual)
minuto_actual = time.strftime("%M")
minutos_restantes = 59 - int(minuto_actual)

if int(hora_actual) > 19:
    print("Deber'ias estar en casa")
else:
    print(f"Quedan {horas_restantes} horas y {minutos_restantes} minutos para irte para casa")
