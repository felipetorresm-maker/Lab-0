import math

def bsa(alturaen_cm, pesoen_kg):
    return math.sqrt((alturaen_cm * pesoen_kg) / 3600)

def clasificar_bsa(valor_bsa):
    if valor_bsa < 0.25:
        return "Recien nacido"
    elif valor_bsa < 0.5:
        return "Bebé"
    elif valor_bsa < 1.14:
        return "Niño "
    elif valor_bsa < 1.6:
        return "adolecente"
    elif valor_bsa < 1.9:
        return "adulto"
    else :
        return "Adulto atleta"

def clasificar_por_edad(edad_años):
    if edad_años == 0 :
        return "Recien nacido"
    elif edad_años < 3:
        return "Bebé"
    elif edad_años < 6:
        return "Niño pequeño"
    elif edad_años < 10:
        return "Niño grande"
    elif edad_años <=17:
        return "Adolescente"
    else:
        return "Adulto"

def calculo(edad_años, area):
    if area < 0.25 and edad_años == 0:
        return "ideal"
    elif area < 0.5 and edad_años < 3:
        return "ideal"
    elif area < 1.14 and edad_años < 15:
        return "ideal"
    elif area < 1.6 and edad_años < 22:
        return "ideal"
    elif area < 1.9 and edad_años < 100:
        return "ideal"
    elif area < 0.25 and edad_años > 0:
        return "bajo para su edad"
    elif area < 0.5 and edad_años >= 3:
        return "bajo para su edad"
    elif area < 1.14 and edad_años >= 15:
        return "bajo para su edad"
    elif area < 1.6 and edad_años >= 22:
        return "bajo para su edad"
    elif area < 1.9 and edad_años >= 100:
        return "bajo para su edad"
    elif area > 0.25 and edad_años == 0:
        return "alto para su edad"
    elif area > 0.5 and edad_años < 3:
        return "alto para su edad"
    elif area > 1.14 and edad_años < 15:
        return "alto para su edad"
    elif area > 1.6 and edad_años < 22:
        return "alto para su edad"
    elif area > 1.9 and edad_años < 100:
        return "alto para su edad"
    
    else:
        return "peso ideal"

def calculopeso2(jj,h):
    return 3600*jj**2/h
def bsaminimo(area):
    if area < 0.25:
       valor1 =0 
       valor2 =0.25
       return valor1,valor2
        
    elif area < 0.5:
       valor1 =0.25 
       valor2 =0.5
       return valor1,valor2
    elif area < 1.14:
      valor1 =0.5 
      valor2 =1.14
      return valor1,valor2
    elif area < 1.6:
      valor1 =1.14 
      valor2 =1.6
      return valor1,valor2
    elif area < 1.9:
      valor1 =1.6 
      valor2 =1.9
      return valor1,valor2
    else:
        valor1 =1.9 
        valor2 =2.5
        return valor1,valor2

personas = int(input("Ingrese el número de personas: "))
datos = []
recienNacido = 0
bebe = 0
niñoPequeño = 0
niñoGrande = 0
adolecente = 0
adulto = 0
valor1=0
valor2=0

for i in range(personas):
    print(f"\nPersona {i + 1}:")
    h = float(input("Ingrese su altura en cm: "))
    w = float(input("Ingrese su peso en kg: "))
    edad_años = int(input("Ingrese su edad en años (0 si es menor de 1 año): "))
    area = bsa(h, w)
    valor1, valor2 = bsaminimo(area)

    categoria = clasificar_bsa(area)
    datos.append(categoria)

    calculodebsa=calculo(edad_años,area)
    pesoideal=calculopeso2(valor1,h)
    pesoideal2=calculopeso2(valor2,h)
    print(f"su peso es :{calculodebsa}")
    print(f"BSA estimada: {area:.2f} m²")
    print(f"su bsa es de un : {categoria}")
    print(f"El rango de peso adecuado es entre {pesoideal:.2f} y {pesoideal2: .2f} kg")

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