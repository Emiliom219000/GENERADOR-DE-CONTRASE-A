import random
import string
import pyperclip

class GeneradorContraseña:
    @staticmethod
    def generar(longitud=12):
        caracteres = string.ascii_letters + string.digits + string.punctuation
        contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
        return contraseña

    @staticmethod
    def copiar_al_portapapeles(contraseña):
        pyperclip.copy(contraseña)
        print(" Contraseña copiada al portapapeles.")



