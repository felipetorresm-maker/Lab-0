import math

def bsa(alturaen_cm, pesoen_kg):
    return math.sqrt((alturaen_cm * pesoen_kg) / 3600)

def clasificar_bsa(valor_bsa):
    if valor_bsa < 0.25:
        return "Recien nacido"
    elif valor_bsa < 0.5:
        return "Bebé"
    elif valor_bsa < 0.8:
        return "Niño pequeño"
    elif valor_bsa < 1.2:
        return "Niño grande"
    elif valor_bsa < 1.7:
        return "Adolescente"
    elif valor_bsa < 2.0:
        return "Adulto promedio"
    else:
        return "Adulto grande o atleta"

if __name__ == "__main__":
    personas = int(input("Ingrese el número de personas: "))
    datos = []
    recienNacido = 0
    bebe = 0
    niñoPequeño = 0
    niñoGrande = 0
    adolecente = 0
    adulto = 0

    for i in range(personas):
        print(f"\nPersona {i + 1}:")
        h = float(input("Ingrese su altura en cm: "))
        w = float(input("Ingrese su peso en kg: "))

        area = bsa(h, w)
        categoria = clasificar_bsa(area)
        datos.append(categoria)

        print(f"BSA estimada: {area:.2f} m²")
        print(f"Usted es: {categoria}")

    for i in datos:
        if i == "Recien nacido":
            recienNacido += 1
        elif i == "Bebé":
            bebe += 1
        elif i == "Niño pequeño":
            niñoPequeño += 1
        elif i == "Niño grande":
            niñoGrande += 1
        elif i == "Adolescente":
            adolecente += 1
        else:
            adulto += 1

    reciennacido2 = recienNacido / personas * 100
    bebe2 = bebe / personas * 100
    niñopequeño2 = niñoPequeño / personas * 100
    niñogrande2 = niñoGrande / personas * 100
    adolecente2 = adolecente / personas * 100
    adulto2 = adulto / personas * 100

    print("\nPorcentajes por categoría:")
    print(f"Recién nacido: {reciennacido2:.2f}%")
    print(f"Bebé: {bebe2:.2f}%")
    print(f"Niño pequeño: {niñopequeño2:.2f}%")
    print(f"Niño grande: {niñogrande2:.2f}%")
    print(f"Adolescente: {adolecente2:.2f}%")
    print(f"Adulto promedio / grande: {adulto2:.2f}%")