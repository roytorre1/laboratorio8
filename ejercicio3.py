# generar contraseña segura

import random
import string

def generar_contrasena(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = []

    contrasena.append(random.choice(string.ascii_uppercase))  # Al menos una letra mayúscula
    contrasena.append(random.choice(string.ascii_lowercase))  # Al menos una letra minúscula
    contrasena.append(random.choice(string.digits))  # Al menos un número
    contrasena.append(random.choice(string.punctuation))  # Al menos un carácter especial

    while len(contrasena) < longitud:
        contrasena.append(random.choice(caracteres))

    random.shuffle(contrasena)
    return ''.join(contrasena)
# Podemos cambiar esta longitud según nuetras preferencias

longitud_deseada = 12  
contrasena_generada = generar_contrasena(longitud_deseada)
print(contrasena_generada)