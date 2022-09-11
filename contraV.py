def Contra(contra):
    print("----------------------------------------------------------------")
    
    if len(contra) >= 8 and contra.isalnum() == True:
        print("Contraseña valida: ")
    else:
        print("la contraseña no es seguro: ")
    return contra
    print("----------------------------------------------------------------")
