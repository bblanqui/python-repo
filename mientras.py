import math;

print("empanadas don brian")
print("**********************")
print("0. digita 0 para salir")
print("1 digita 1 para calcuular la raiz cuadrada de i¿un numero")
print("2. digita 2 para calcular la potencia  2 de un numero")
print("*********************")

opcion =1


while (opcion != 0):
    opcion =int(input("digita un numero"))

    if(opcion == 0):
        break
    elif(opcion==1):
        numero =int(input("dijita un número"))
        raiz = math.sqrt(numero)
        print(f"la raiz de {numero} es {raiz}")
    
    elif (opcion==2):
        numero =int(input("dijita un número"))
        potencia = math.pow(numero, 2)
        print(f"la potencia de {numero} es {raiz}")

    else:
        print("digita una valida omeee goonoonea ome")
    



    opcion=opcion + 1