def Nombre(nombre):
    print("----------------------------------------------------------------")
    if len(nombre) >= 6 and len(nombre) <= 12 and nombre.isalnum() == True:
       print("Nombre de usuario valido: ")
    elif len(nombre) < 6:
        print("El nombre de usuario debe teber al menos 6 caracteres: ")
    elif len(nombre) > 12:
        print("El nombre de usuario no debe tener más de 12 caracteres: ")
    elif nombre.isalnum() == False:
        print("El nombre solo puede tener letras y numeros: ")
    return nombre

    