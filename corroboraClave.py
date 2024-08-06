while True:
    clave = input("Escriba la clave")
    if len(clave) > 8:
        if(clave.find(" ") == -1):
            if(clave.isdigit() == False):
                            if(clave.find("1") != -1 or 
                            clave.find("2") != -1 or 
                            clave.find("3") != -1 or 
                            clave.find("4") != -1 or 
                            clave.find("5") != -1 or 
                            clave.find("6") != -1 or 
                            clave.find("7") != -1 or 
                            clave.find("8") != -1 or 
                            clave.find("9") != -1 or 
                            clave.find("0") != -1): 
                                    if(clave.isalnum() == False):
                                        if(clave.islower() == False and clave.isupper() == False):
                                            print("Todo bien")
                                        else:
                                            print("Debe tener letras mayusculas y minusculas")
                                    else:
                                        print("No tiene caracter especial")
                            else:
                                print("No tiene numeros")
            else:
                print("Solo estas ingresando numeros")
        else:
            print("Estas ingresando espacios")
    else:
        print("Debe tener mas de 8 caracteres")
