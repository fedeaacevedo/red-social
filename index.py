print("Bienvenido a ... ")
print("""              _                  __
   ____ ___  (_)  ________  ____/ /
  / __ `__ \/ /  / ___/ _ \/ __  /
 / / / / / / /  / /  /  __/ /_/ /
/_/ /_/ /_/_/  /_/   \___/\__,_/

""")

nombre = input("Para empezar, dime como te llamas. ")
print()
print("Hola ", nombre, ", bienvenido a Mi Red")
print()


año = int(input("Para preparar tu perfil, dime en que año naciste. "))
edad = 2020-año-1
print("Tenes", edad, " años")

ciudad = input("Contame donde vivis: ")
print()
print("Que linda ciudad ", ciudad)
print()

estatura = float(input("Cuentame mas de ti, para agregarlo a tu perfil. ¿Cuanto mides? Dimelo en metros. "))
estatura_m = int(estatura)
estatura_cm = int( (estatura - estatura_m)*100 )

print("Gracias por darme tu estatura")

#AMIGOS

num_amigos = int(input("Muy bien. Finalmente, cuÃ©ntame cuantos amigos tienes. "))

#Con los datos recolectados escribimos en pantalla un texto que resuma los datos que hemos obtenido
print()
print("Muy bien,", nombre, ". Entonces podemos crear un perfil con estos datos.")
print("--------------------------------------------------")
print("Nombre:  ", nombre)
print("Edad:    ", edad, "años")
print("Estatura:", estatura_m, "metros y", estatura_cm, "centimetros")
print("Amigos:  ", num_amigos)
print("Ciudad: ", ciudad)
print("--------------------------------------------------")
print("Gracias por la informacion. Esperamos que disfrutes con Mi Red")
print()

#Finalmente, solicitamos un mensaje de prueba que sirva para publicar un estado del usuario.
mensaje = input("Ahora vamos a publicar tu primer mensaje. ¿Que piensas hoy? ")
print()
print("--------------------------------------------------")
print(nombre, "dice:", mensaje)
print("--------------------------------------------------")



 #Solicitamos opciÃ³n al usuario
escribir_mensaje = str(input("¿Deseas escribir un mensaje? (S/N) "))

    #Vamos a aceptar que el usuario ingrese un mensaje cuando escriban "S", "s", o nada
if escribir_mensaje == "S" or escribir_mensaje == "s" or escribir_mensaje == "":
        mensaje = input("Vamos a publicar un mensaje. Â¿QuÃ© piensas hoy? ")
        print()
        print("--------------------------------------------------")
        print(nombre, "dice:", mensaje)
        print("--------------------------------------------------")
    #En caso que sea otra respuesta, vamos a decidir salir.
    #AsÃ­, en la siguiente iteraciÃ³n el ciclo terminarÃ¡
else:
        continuar = False

#Mensaje de salida, una vez que el ciclo ha terminado.
print("Gracias por usar Mi Red. Â¡Hasta pronto!")


#Esta opcion permite entrar al ciclo. Solo interesa que no sea 0.
opcion = 1
while opcion != 0:
    print("Acciones disponibles:")
    print("  1. Escribir un mensaje pÃºblico")
    print("  2. Escribir un mensaje solo a algunos amigos")
    print("  3. Mostrar los datos de perfil")
    print("  4. Actualizar el perfil de usuario")
    print("  0. Salir")
    opcion = int(input("Ingresa una opciÃ³n: "))

    #CÃ³digo para la opciÃ³n 1. Publicar un mensaje.
    if opcion == 1:
        mensaje = input("Ahora vamos a publicar un mensaje. Â¿QuÃ© piensas hoy? ")
        print()
        print("--------------------------------------------------")
        print(nombre, "dice:", mensaje)
        print("--------------------------------------------------")

    #CÃ³digo para la opciÃ³n 2. Publicar un mensajes a un grupo de personas.
    elif opcion == 2:
        mensaje = input("Ahora vamos a publicar un mensaje a un grupo de amigos. Â¿QuÃ© quieres decirles? ")
        print()
        for i in range(num_amigos):
            nombre_amigo = input("Ingresa el nombre de tu amigo o amiga: ")
            print("--------------------------------------------------")
            print(nombre, "dice:", "@"+nombre_amigo, mensaje)
            print("--------------------------------------------------")

    #CÃ³digo para la opciÃ³n 3. Publicar los datos del perfil del usuario.
    elif opcion == 3:
        print("--------------------------------------------------")
        print("Nombre:   ", nombre)
        print("Edad:     ", edad, "aÃ±os")
        print("Estatura: ", estatura_m, "m y ", estatura_cm, "centÃ­metros")
        print("Amigos:   ", num_amigos)
        print("--------------------------------------------------")

    #CÃ³digo para la opciÃ³n 4. Actualizar los datos del perfil del usuario.
    elif opcion == 4:
        #Repetimos el cÃ³digo para solicitar datos
        # Solicitud de nombre
        nombre = input("Para empezar, dime como te llamas. ")
        print()
        print("Hola ", nombre, ", bienvenido a Mi Red")
        print()

        # CÃ¡lculo de edad
        agno = int(input("Para preparar tu perfil, dime en quÃ© aÃ±o naciste. "))
        edad = 2017-agno-1
        print()

        # CÃ¡lculo de estatura
        estatura = float(input("CuÃ©ntame mÃ¡s de ti, para agregarlo a tu perfil. Â¿CuÃ¡nto mides? DÃ­melo en metros. "))
        estatura_m = int(estatura)
        estatura_cm = int( (estatura - estatura_m)*100 )

        # Cantidad de amigos
        num_amigos = int(input("Muy bien. Finalmente, cuÃ©ntame cuantos amigos tienes. "))

        print()
        print("Muy bien,", nombre, ". Entonces podemos crear un perfil con estos datos.")
        # Repetimos el cÃ³digo para mostrar los datos del usuario.
        print("--------------------------------------------------")
        print("Nombre:  ", nombre)
        print("Edad:    ", edad, "aÃ±os")
        print("Estatura:", estatura_m, "metros y", estatura_cm, "centÃ­metros")
        print("Amigos:  ", num_amigos)
        print("--------------------------------------------------")
        print()

    #CÃ³digo para la opciÃ³n 0. Salir.
    elif opcion == 0:
        print("Has decidido salir.")

    #CÃ³digo para la opciÃ³n que no coincida con ninguna anterior.
    else:
        print("No conozco la opciÃ³n que has ingresado. IntÃ©ntalo otra vez.")

print()
print("Gracias por usar Mi Red. Â¡Hasta pronto!")
print()
