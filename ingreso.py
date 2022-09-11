from nombreV import Nombre
from contraV import Contra
i = 1

while i == 1:
    print("-----------------------------LOGIN-----------------------------")
    print("1. Ingresar Usuario. ")
    print("2. Salir.")
    opcion = int(input())
    print("----------------------------------------------------------------")
    if opcion == 1:
        nombre = (input("Ingrese un nombre de usuario: "))
        print("----------------------------------------------------------------")
        contra = (input("Ingrese una contraseña: "))
        print("----------------------------------------------------------------") 
        print(Nombre(nombre))
        print(Contra(contra))
        print("----------------------------------------------------------------")
    elif opcion == 2:
        print("¡Hasta Pronto!")
        print("----------------------------------------------------------------")
        exit()
    else:
        print("¡OPCIÓN INVALIDA!")
        print("----------------------------------------------------------------")
    

    
