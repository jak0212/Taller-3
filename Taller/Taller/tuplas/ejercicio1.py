def sumar_tupla(tupla): #funcion  
    suma = sum(tupla)
    return suma

mi_tupla = (int(input("Ingrese  un numero: ")),int(input("Ingrese un numero: ")),int(input("Ingrese un numero: ")),int(input("Ingrese un numero: ")),int(input("Ingrese  un numero: ")))  #argumento
resultado = sumar_tupla(mi_tupla)
print(resultado) 
