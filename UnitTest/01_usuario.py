

# Implementar una clase Usuario que tenga:
# Metodos: obtener_nombre(), obtener_email(), es_mayor_de_edad(), edad(),


class Usuario:
    pass


user = Usuario("Olivia")
nombre = user.obtener_nombre()
if nombre == "Olivia":
    print("Prueba exitosa")
else:
    print("Prueba fallida")


user = Usuario("Alberto")
nombre = user.obtener_nombre()
if nombre == "Alberto":
    print("Prueba exitosa")
else:
    print("Prueba fallida")