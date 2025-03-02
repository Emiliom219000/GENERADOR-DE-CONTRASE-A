from generador import GeneradorContraseña

longitud = int(input(" Ingresa la longitud de la contraseña: "))
contraseña = GeneradorContraseña.generar(longitud)
print(f" Tu contraseña generada es: {contraseña}")

# Copiar automáticamente al portapapeles
GeneradorContraseña.copiar_al_portapapeles(contraseña)
