nif_dict = {"0": "T", "1": "R", "2": "W", "3": "A", "4": "G", "5": "M", "6": "Y", "7": "F", "8": "P", "9": "D",
            "10": "X", "11": "B", "12": "N", "13": "J", "14": "Z", "15": "S", "16": "Q", "17": "V", "18": "H",
            "19": "L", "20": "C", "21": "K", "22": "E"}


def check_nif(dni):
    """Esta funcion corrige la letra del DNI introducido realizando el resto de todos los numeros del DNI entre 23
    PARAMETROS:
                dni=Es el dni introducido por el usuario, después se corregirá"""
    dni_sin_letra = dni[0:8]
    resto = int(dni_sin_letra) % 23
    final = dni_sin_letra + nif_dict[str(resto)]
    return print(str(final))


dni = input("INTRODUZCA SU NIF\n")
check_nif(dni)
