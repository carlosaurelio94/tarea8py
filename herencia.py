class Vehiculo():
    color = 'Negro'
    print(color)
    ruedas = 4
    print(ruedas)
    puertas = 5
    print(puertas)


class Coche(Vehiculo):
    velocidad = '60 km/h'
    print(velocidad)
    cilindrada = '4100 cc'
    print(cilindrada)

Auto = Coche
print(Auto)

