import csv

# Datos de ejemplo
datos = [
    ["altura", "peso"],
    [170, 65],
    [160, 55],
    [175, 70],
    [180, 80],
    [165, 60],
    [155, 50],
    [185, 85],
    [190, 90],
    [175, 75],
    [165, 62]
]

# Crear y escribir en el archivo CSV
with open('altura_peso.csv', mode='w', newline='') as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)
    escritor_csv.writerows(datos)

print("Archivo CSV creado exitosamente.")
