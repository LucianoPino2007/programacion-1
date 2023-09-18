#recuperatorio actividad 1. Pino Luciano y Ceballos Gustavo
print (" GENERACIONES ")
def generacion(numero):
    asteriscos = "*"
    for i in range(numero):
        print (asteriscos)
        asteriscos = asteriscos*2
numero = int(input("Ingresa el numero de generaciones que deseas: "))
generacion(numero)