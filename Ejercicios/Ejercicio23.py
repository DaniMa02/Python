def Login(usuario, contraseña, intentos):
    # Usuario y contraseña correctos
    usuario_correcto = "usuario1"
    contraseña_correcta = "asdasd"
    
    if usuario == usuario_correcto and contraseña == contraseña_correcta:
        return True, intentos
    else:
        intentos += 1
        return False, intentos

intentos = 0
while intentos < 3:
    usuario = input("Nombre de usuario: ")
    contraseña = input("Contraseña: ")
    
    if Login(usuario, contraseña, intentos)[0]: 
        print("Has iniciado sesión en " +str(intentos)+ " intentos.")
        
        break
    else:
        intentos = Login(usuario, contraseña, intentos)[1]  # Actualiza el número de intentos
        print("Usuario o contraseña incorrectos. Intentalo de nuevo.")

if intentos == 3:
    print("Has excedido el número máximo de intentos.")
