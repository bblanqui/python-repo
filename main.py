#ejemplo de estaciones

mes = input("dijita un mes del año: ").lower()
print(f"el mes dijitado fue {mes}")

#caminos para clasificar el mes

if(mes== "diciembre" or mes== "enero" or mes== "febrero" or mes== "marzo"):
    print("invierno")
elif(mes== "junio" or mes== "julio" or mes== "mayo"):
    print("verano")
elif(mes== "abril" or mes== "mayo"):
    print("primaver")
elif(mes== "septiembre" or mes== "octubre" or mes=="noviembre"):
    print("otoño")

else:
    print(" no existe")