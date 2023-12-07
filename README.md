# Proyecto final de coder

## Configuración inicial del proyecto

0. Instalar `django`:  `pip install django`
1. Crear carpeta para nuestro repositorio, yo elegí nombrarla: "proyecto-final-47790"
2. dentro de esa carpeta: `django-admin startproject ProyectoFinal`. Este comando dejará creada una nueva carpeta `ProyectoFinal` con una
estructura como esta:
```bash
# directorio: ProyectoCoder/ProyectoFinal
drwxr-xr-x@ 8 marianobarraco  staff   256B Sep  3 09:26 ProyectoFinal  # <--- directorio principal del proyecto (nombre repetido)
-rw-r--r--@ 1 marianobarraco  staff     0B Sep  3 09:28 db.sqlite3
-rwxr-xr-x@ 1 marianobarraco  staff   669B Sep  3 09:25 manage.py
```
3. Dentro de la carpeta `proyecto-final-47790/ProyectoFinal/ProyectoFinal` vamos a correr el comando `python manage.py startapp AppCoder` lo
cual nos dejará en este estado
```bash
# directorio: ProyectoCoder/ProyectoFinal
drwxr-xr-x@ 9 marianobarraco  staff   288B Sep  3 09:31 AppCoder  # <--- nueva carpeta
drwxr-xr-x@ 8 marianobarraco  staff   256B Sep  3 09:26 ProyectoFinal
-rw-r--r--@ 1 marianobarraco  staff     0B Sep  3 09:28 db.sqlite3
-rwxr-xr-x@ 1 marianobarraco  staff   669B Sep  3 09:25 manage.py
```
4. Registrar la aplicacion en `ProyectoFinal/settings.py`
5. Probamos que nuestro servidor web funcione correctamente, para ello vamos a correr el siguiente comando `python manage.py runserver` y comprobaeremos de 2 maneras: (i) observar la respuesta en la consola y (ii)en el browser (por ejemplo _Google Chrome_):

```bash
# directorio: ProyectoCoder/ProyectoFinal
>>  python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
September 03, 2023 - 12:34:23
Django version 4.2.4, using settings 'ProyectoFinal.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```
copiar y pegar en cualquier browser: `http://127.0.0.1:8000/` y comprobar que el servidor responda.

5. La consola queda "colgada" con el **proceso** de django bloqueando toda interacción entre nosotros y la misma. Para terminar/matar dicho procesopodemos utilizar lo que dice `django` en su salida: `Quit the server with CONTROL-C.` (salir del servidor conn CTRL + C)


## Configurar Rutas

**Consejo**: cuando el proceso del servidor está corriendo, los cambios que realicemos en el código se incorporarán automáticamente. A veces esto puede no funcionar, por eso es recomendable apagar y encender el proceso del servidor con: `CRTL + C` y luego `python manage.py runserver` desde el directorio raíz del proyecto `ProyectoCoder/ProyectoFinal`


1. Checkear que nuestro proyecto tenga 1 archivo `urls.py` en el directorio `ProyectoCoder/`
2. Crear un archivo exactamente igual pero en el directorio `AppCoder`
3. Modificar el nuevo archivo `AppCoder/urls.py` para que contenga una ruta llamada `cursos`: ```path("inicio/", inicio_view),```
4. Crear una función para "hacerse cargo" de los pedidos en la ruta `cursos`, la llamaremos `cursos_view`
5. Registrar las rutas definidas por el archivo `AppCoder/urls.py` en el archivo `urls.py` general del proyecto: `ProyectoCoder/urls.py`
6. Checkear que la ruta funcione entrando a:  `http://127.0.0.1:8000/cursos`
7. Modificaremos el archivo general `urls.py` para que la ruta

    `http://127.0.0.1:8000/cursos`

    se transforme en

    `http://127.0.0.1:8000/AppCoder/cursos`


# Modelos

1. en el archivo `AppCoder/models.py` crear (por ejemplo) 2 modelos:
    ```python
    from django.db import models


    class Profesor(models.Model):
        nombre = models.CharField(max_length=30)
        email = models.EmailField()

    class Comision(models.Model):
        numero = models.IntegerField()
    ```
2. Ejecutar los comandos de migraciones:
   ```bash
   >> python manage.py makemigrations
   >> python manage.py migrate
3. Crear modelos utilizando una `view`

## Entregar contenido HTML desde plantillas (templates)

**Consejo**: las plantillas se escriben en lenguaje **HTML**, no vamos a profundizar sobre este lenguaje, por lo tanto nuestra tarea será simplemente manipularlo.

### Funcionamiento básico de templates
1. Crear un directorio llamado `templates` dentro del directorio `AppCoder`, luego crear otro directorio dentro de `templates` llamado `AppCoder` (sí, se repite)
2. Crear un archivo `padre.html` en ese directorio: `ProyectoCoder/ProyectoFinal/AppCoder/templates/AppCoder/padre.html` y llenarlo con cualquier contenido
3. Modificaremos la función `cursos_view` (desde ahora la llamaremos **vista**) que _se hace cargo_ de la ruta `AppCoder/cursos` para que entregue el contenido del archivo `padre.html`

**nota**: en el archivo `settings.py` hay una variable del tipo diccionario que se llama `TEMPLATES`. Esta variable contiene un par clave valor: ` "APP_DIRS": True,`
```python
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]
```
esta es la manera de informarle a `Django` que queremos que utilice los templates alojados en la carpeta `templates` de cada aplicación que hayamos creado.


### Herencia
1. Vamos a crear un template llamado `cursos.html` que herede el contenido de `padre.html`
2. Reemplazamos el template `padre.html` utilizado por `cursos_view` por `cursos.html`
3. Agregamos en `cursos.html`
    ```html
    {% extends "AppCoder/padre.html" %}
    ```
4. Agregamos en `padre.html`
    ```html
    {% block contenidoQueCambia %}
    {% endblock %}
    ```

    y en `cursos.html`

    ```html
    {% block contenidoQueCambia %}
    Este es el contenido de cursos.html!
    {% endblock %}
    ```
### Templates con valores dinámicos

1. Modificamos la forma en la que `cursos_view` utiliza el template:
   ```python
    return render(
        request,
        "AppCoder/cursos.html",
        {
            "nombre": "Curso de Python",
            "camadas": [1000, 1001, 1002, 1003, 1004, 1005]
        }
    )
   ```

### Templates con CSS ("mejorando nuestros templates")
1. Crear una carpeta llamada `static` en nuestra app: `/AppCoder/static/AppCoder`
2. Descargarse el archivo `.zip` con contenido estático de: [este link](https://startbootstrap.com/previews/landing-page)
3. Descomprimir y guardar todo el contenido en la carpeta `static/AppCoder`
4. Creamos un archivo que se llame `inicio.html` en la carpeta de templates. El contenido de este archivo tiene que ser el mismo que en `index.html` del archivo `.zip` que descomprimimos.
5. Vamos a elminar todo el contenido dede la línea 74 `<!-- Icons Grid-->` hasta la línea 201 `</section>`
6. Le agregamos 1 línea y modificamos otra:
    ```html
    {% load static %}
    ```

    ```html
    <!-- Core theme CSS (includes Bootstrap)-->
    <link href="{% static 'AppCoder/css/styles.css'  %}" rel="stylesheet" />
    ```
7. Creamos una ruta `inicio` y una view para responder con el template `inicio.html`
8. Ahora podemos hacer modificaciones en el texto que se muestra en el browser.

### Modelos
1. Correr `python manage.py migrate`
2. Crear un Modelo en `AppCoder/models.py`
   ```python
    class Curso(models.Model):
        curso = models.CharField(max_length=100)
        camada = models.IntegerField()
    ```
4. Corrrer sucesivamente
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
5. Checkear la existencia de la tabla en la base de datos utilizando **DB Browser**

### Formularios (básicos) para crear instancias de modelos en la base de datos

Idea: vamos a evolucionar la vista `cursos_view` para que pueda cumplir 2 funciones:
 * Devolver un formulario de creación de cuross
 * Crear un formulario en la base de datos.

1. Crear un template `curso_formulario_basico.html` con el siguiente contenido:
   ```html
    <!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Formulario</title>
    </head>

    <body style="background-color: pink;">
        <form action="/AppCoder/cursos/" method="POST">
            {% csrf_token %}
            <p>Curso: <input type="text" name="curso"> </p>
            <p>Camada: <input type="number" name="camada"> </p>
            <input type="submit" value="Guardar">
        </form>
    </body>

    </html>
   ```
2. Vamos a devolver este formulario mediante la vista `cursos_view` cuando el usuario pida la ruta `cursos`
3. Vamos a modificar `curso_formulario_basico.html` para que herede del template `padre.html`
4. Tener en cuenta la siguiente línea que es la que indicará a qué ruta viajará la información del formulario
   ```html
   <form action="/AppCoder/cursos/" method="POST">
    ```
5. Modificamos la vista `cursos_view` para que distinga entre requests `GET` y `POST`
   ```python
    def cursos_view(request):
        if request.method == "GET":
            print("+" * 90) #  Imprimimos esto para ver por consola
            print("+" * 90) #  Imprimimos esto para ver por consola
            return render(
                request,
                "AppCoder/curso_formulario_basico.html",
            )
        else:
            print("*" * 90)     #  Imprimimos esto para ver por consola
            print(request.POST) #  Imprimimos esto para ver por consola
            print("*" * 90)     #  Imprimimos esto para ver por consola
            return render(
                request,
                "AppCoder/curso_formulario_basico.html",
            )
   ```
6. Vamos a crear un modelo cuando el request sea del tipo `POST` mediante estas líneas:
    ```python
    from .models import Curso

    modelo = Curso(curso=request.POST["curso"], camada=request.POST["camada"])
    modelo.save()
    ```

### Formularios (avanzados) para crear modelos

1. Creamos un archivo `AppCoder/forms.py` con el siguiente contenido
   ```python
    from django import forms


    class CursoFormulario(forms.Form):

        curso = forms.CharField()
        camada = forms.IntegerField()
   ```

2. Creamos una copia de `curso_formulario_basico.html` con el nombre `curso_formulario_avanzado.html` y efecutamos la siguiente modificación en el nuevo archivo:
    ```html
    <p>Curso: <input type="text" name="curso"> </p>
    <p>Camada: <input type="number" name="camada"> </p>
    ```
    por
    ```html
    {{ form.as_p }}
    ```
4. Editamos `cursos_view` para que utilice el nuevo template tanto para requests `GET` como para `POST`
5. Modificamos el template `padre.html` para que tenga un link a `AppCoder/cursos` y al `inicio`.

# Clase 12

## Pendiente

1. Usar validación de Forms
```python
def cursos_view(request):
    if request.method == "GET":
        print("+" * 90) #  Imprimimos esto para ver por consola
        print("+" * 90) #  Imprimimos esto para ver por consola
        return render(
            request,
            "AppCoder/curso_formulario_avanzado.html",
            {"form": CursoFormulario()}
        )
    else:
        formulario = CursoFormulario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            modelo = Curso(curso=informacion["curso"], camada=informacion["camada"])
            modelo.save()
        return render(
            request,
            "AppCoder/inicio.html",
        )

```
## Panel de Administración

1. Creamos el panel de administración en `ProyectoFina/AppCoder/admin.py` con el siguiente contenido
 ```python
    from django.contrib import admin

    # Register your models here.

    from .models import Curso


    @admin.register(Curso)
    class CursoAdmin(admin.ModelAdmin):
        pass

```
2. Creamos un super usuario mediante `python manage.py createsuperuser`
   ```bash
    >> python manage.py createsuperuser
        Username (leave blank to use 'marianobarraco'): admin
        Email address: a@a.com
        Password:
        Password (again):
        The password is too similar to the username.
        This password is too common.
        Bypass password validation and create user anyway? [y/N]: y
        Superuser created successfully.
    ```
## Otros modelos

1. Creamos los modelos: `Profesor`, `Estudiante`, `Entregable`

```python
class Entregable(models.Model):
    nombre = models.CharField(max_length=50)
    fecha_entrega = models.DateField()
    entregado = models.BooleanField()


class Estudiante(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)


class Profesor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    profesion = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} {self.appelido}"
```
2. Corrrer sucesivamente
```bash
python manage.py makemigrations
python manage.py migrate
```

3. Podemos crear modelos desde una vista: ver `AppCoder.views.crear_profesores_varios`

## CRUD

**Consejo**: Familiarizarse con la `shell` de **Django**: `python manage.py shell`
```python
from AppCoder.models import *

cursos = Curso.objects.all()
for curso in cursos:
    print(curso.curso)
```

### Crear (Create)

1. Creamos un formulario para el modelo `Profesor`
2. Creamos una vista que sepa mostrar el formulario vacío (`GET`) y sepa procesar el formulario lleno (`POST`)
3. Creamos un template
### Leer (Read)

1. Creamos una view para leer todos los cursos: `cursos_crud_read_view`:
    ```python
    def cursos_crud_read_view(request):
        cursos = Curso.all()

    contexto = {"cursos": cursos}
    ```
2. Creamos un **template** y registramos la **url**
3. **consejo**: agregar al template: `<a href="/AppCoder/profesores">Crear profesor</a>`

### Eliminar (Delete)

### Editar (Update)

## Login / Logous

1. Template + view + urls