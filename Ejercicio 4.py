def check_username(nom):
    """Esta funcion devuelve una cadena con la primera letra de cada palabra en mayuscula"""

    return nom.title()




nom= input("Introduzca su nombre y apellidos")
print(check_username(nom))