import random


longitud = int(input("Ingrese la longitud de la contraseña: "))

numeros = input("¿Desea incluir números? (si/no): ")
simbolos = input("¿Desea incluir símbolos? (si/no): ")
mayusculas = input("¿Desea incluir mayúsculas? (si/no): ")

caracteres = "abcdefghijklmnopqrstuvwxyz"

if mayusculas == "si":
    caracteres = caracteres + "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

if numeros == "si":
    caracteres = caracteres + "0123456789"

if simbolos == "si":
    caracteres = caracteres + "!@#$%&*?"

contrasena = ""

for i in range(longitud):
    contrasena = contrasena + random.choice(caracteres)

print("Contraseña generada:")
print(contrasena)