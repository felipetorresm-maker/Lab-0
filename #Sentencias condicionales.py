#Sentencias condicionales
import math
def bsa(alturaen_cm, pesoen_kg):
    return math.sqrt((alturaen_cm * pesoen_kg) / 3600)
def clasificar_bsa(bsa):
    if bsa < 0.25:
        return "Recien nacido"
    elif bsa < 0.5:
        return "Bebé"
    elif bsa < 0.8:
        return "Niño pequeño"
    elif bsa < 1.2:
        return "Niño grande"
    elif bsa < 1.7:
        return "Adolescente"
    elif bsa < 2.0:
        return "Adulto promedio"
    else:
        return "Adulto grande o atleta"
if __name__ == "__main__":
    h = float(input("Ingrese su altura:"))
    w = float(input("Ingrese su peso:"))
    area = bsa(h, w)
    prueba = 10
    categoria = clasificar_bsa(prueba)
    print(f"BSA estimada: {area:.2f} m²")
    print(f"Usted es:{categoria}")
