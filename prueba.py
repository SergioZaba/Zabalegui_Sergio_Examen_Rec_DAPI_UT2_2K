import csv


nif_dict = {"0": "T", "1": "R", "2": "W", "3": "A", "4": "G", "5": "M", "6": "Y", "7": "F", "8": "P",
                            "9": "D",
                            "10": "X", "11": "B", "12": "N", "13": "J", "14": "Z", "15": "S", "16": "Q", "17": "V",
                            "18": "H",
                            "19": "L", "20": "C", "21": "K", "22": "E"}

countries_dict = {"30": "Grecia", "33": "Francia", "34": "España", "351": "Portugal",
                  "380": "Ucrania", "39": "Italia", "41": "Suiza", "44": "Reino Unido",
                  "49": "Alemania", "7": "Rusia"}

def check_username(nom):
    """Esta funcion devuelve una cadena con la primera letra de cada palabra en mayuscula"""

    return nom.title()

def check_nif(dni):
    """Esta funcion corrige la letra del DNI introducido realizando el resto de todos los numeros del DNI entre 23
    PARAMETROS:
                dni=Es el dni introducido por el usuario, después se corregirá"""
    dni_sin_letra = dni[0:8]
    resto = int(dni_sin_letra) % 23
    final = dni_sin_letra + nif_dict[str(resto)]
    return str(final)

def check_phone(num):
    separar = num[1:].split(")")
    pais = countries_dict[separar[0]]
    telefono = "+" + separar[0] + "-" + separar[1].replace("-", "")

    return telefono, pais
def calculate_bill(multas_radar, multas_ITV, multas_estupefacientes):
    bill = multas_radar + multas_ITV + multas_estupefacientes
    return bill


def check_DGT():
    """Esta funcion recoje un excel """

    with open("Sergio Zabalegui Nicuesa - DGT.csv", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)


        csv_out = [["Nombre", "Apellidos", "DNI", "Teléfono", "País", "Vehículo", "Total Multas"]]

        for persona in reader:
            if persona[0] != "Nombre":

                name = persona[0]
                apellido = persona[1]
                dni = persona[2]
                Telefono, Pais = check_phone(persona[3])
                veiculo = persona[4]

                calculate_bill(int(persona[5]), int(persona[6]), int(persona[7]))

                csv_out.append([check_username(name), check_username(apellido), check_nif(dni), Telefono, Pais, veiculo, calculate_bill(int(persona[5]), int(persona[6]), int(persona[7]))])

        excel_escritor = csv.writer(csvfile)

    with open("Sergio Zabalegui Nicuesa - DGT.csv", encoding="utf-8") as salida:
        csvsalida = open('salida.csv', 'w', newline='')
        salida = csv.writer(csvsalida,
                            quotechar='"',
                            quoting=csv.QUOTE_ALL)
        for linea in csv_out:
            salida.writerow(linea)
    return



check_DGT()
