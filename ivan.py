"""
edad = 18
nombre = "Ivan"
print(edad)
print(nombre)

numero_1 = 10
numero_2 = 20 
resultado = numero_1 + numero_2
print("El resultado es " + str(resultado))

numero_1 = 15
numero_2 = 35
resultado = numero_1 * numero_2
print("El resultado es " + str(resultado))

numero_1 = 250
numero_2 = 250
resultado = numero_1 / numero_2
print("El resultado es " + str(resultado))

numero_1 =395
numero_2 = 175
resultado = numero_1 - numero_2
print("El resultado es " + str(resultado))


operacion = input("Teclee la operacion: ")
numero_1 = int(input("Teclee el primer numero"))
numero_2 = int(input("Teclee el segundo numero"))
if operacion == "suma":
    resultado = numero_1 + numero_2
elif operacion == "resta":
    resultado == numero_1 - numero_2
elif operacion == "division":
    resultado = numero_1 / numero_2
else:
    resultado = numero_1 * numero_2
print("El resultado de laoperacion " + str(operacion) + " es " + str(resultado)) 
#print("El resultado de la operacion {0} es {1}").format(operacion, resultado)

"""
participantes =  {'nombre': 'Ivan', 'edad': 37, 'cursos': ['Python', 'React' , 'Django'], }
print(participantes['nombre'])
print(participantes['edad'])
print(participantes['cursos'])

participantes['telefono'] = 9811419236
participantes['ocupacion'] ='Developer'
print(participantes)

jugador = {}

jugador['nickname'] = 'ivicosgaya'
jugador['score'] = 0

print(jugador)

jugador['score']  = 60
print("el score actual del jugador " + jugador['nickname'] + "es" + str(jugador['score']))
