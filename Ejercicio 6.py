countries_dict = {"30": "Grecia", "33": "Francia", "34": "España", "351": "Portugal",
                  "380": "Ucrania", "39": "Italia", "41": "Suiza", "44": "Reino Unido",
                  "49": "Alemania", "7": "Rusia"}
def check_phone(num):
    separar = num[1:].split(")")
    pais = countries_dict[separar[0]]
    telefono = "+"+separar[0]+"-"+separar[1].replace("-", "")

    return print(pais, telefono)

num = str(input("Introduzca su numero de telefono con su prefijo"))
check_phone(num)