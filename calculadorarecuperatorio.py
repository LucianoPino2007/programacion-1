def menu():
    opciones = '''
    ****************************
    ***   1 SUMA             ***
    ***   2 RESTA            ***
    ***   3 MULTIPLICACION   ***
    ***   4 DIVISION         ***
    ***   5 SALIR            ***
    ****************************
    '''
    print(opciones)
    opcion = input("Seleccione una opción: ")
    return(opcion)

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

while True:    
    opcion = menu()
       
    if opcion == "5":
        break
    
    if opcion not in ["1", "2", "3", "4"]:
        print("Opción inválida")
        continue
    
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    
    if opcion == "1":
        resultadosuma = sumar(num1, num2)
        print("El resultado de la suma es:", resultadoresta)
    elif opcion == "2":
        resultadoresta = restar(num1, num2)
        print("El resultado de la resta es:", resultadoresta)
    elif opcion == "3":
        resultadomultiplicacion = multiplicar(num1, num2)
        print("El resultado de la multiplicación es:", resultadomultiplicacion)
    elif opcion == "4":
        if num2 == 0:
            print("Error: No se puede dividir entre cero")
        else:
            resultadodivicion = dividir(num1, num2)
            print("El resultado de la división es:", resultadodivicion)
    
    print