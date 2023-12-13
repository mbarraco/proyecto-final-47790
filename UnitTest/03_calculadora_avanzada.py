
def calcular(numero_1, numero_2, operacion):
    if operacion == "+":
        return numero_1 + numero_2
    elif operacion == "-":
        return numero_1 - numero_2
    elif operacion ==":":
        return numero_1 / numero_2


resultado = calcular(100, 10, "x")
if resultado == 1000:
    print("OK")
else:
    print(f"FAILLLLLL: {resultado}")


resultado = calcular(100, 0, ":")
if resultado == "NO PERMITIDO":
    print("OK")
else:
    print(f"FAILLLLLL: {resultado}")

resultado = calcular(100, 10, ":")
if resultado == 10:
    print("OK")
else:
    print(f"FAILLLLLL: {resultado}")


resultado = calcular(10, 9, "-")
if resultado == 1:
    print("OK")
else:
    print(f"FAILLLLLL: {resultado}")


resultado = calcular(10, 9, "+")
if resultado == 19:
    print("OK")
else:
    print("FAILLLLLL")

resultado = calcular(-10, 9, "+")
if resultado == -1:
    print("OK")
else:
    print("FAILLLLLL")