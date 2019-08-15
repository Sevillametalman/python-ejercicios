from math import pi

lado = float(input("Ingrese L: "))

vol_cubo = lado**3
r = lado / 2
vol_esfera = (4/3)*pi*(r**3)

espacio = vol_cubo - vol_esfera
print("El espacio vacio es de %.2f" % (espacio))