# Implementar una clase Usuario que tenga:
# Metodos: obtener_nombre(), obtener_email(), es_mayor_de_edad(), edad(),

class Usuario:

    def __init__(self, nombre, email="indefinido"):
        self.nombre = nombre
        self.email = email

    def obtener_nombre(self):
        return self.nombre

    def obtener_email(self):
        return self.email


user = Usuario("Nicolas", "nicol@s.com")
email = user.obtener_email()

if email == "nicol@s.com":
    print("Prueba exitosa")
else:
    print("Prueba fallida")


user = Usuario("XXXXXXXXXXX")
email = user.obtener_email()
if email == "indefinido":
    print("Prueba exitosa")
else:
    print("Prueba fallida")


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