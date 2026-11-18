# Blog por consola – Preentrega 6 (POO y persistencia JSON)

Sistema de blog que se usa desde la terminal. Permite **ver todos los posts**, **buscar por título**, **filtrar por tag**, **crear posts nuevos**, **validar los posts** y **guardarlos en un archivo `posts.json`**, para que los datos no se pierdan al cerrar el programa.

En esta versión el blog está modelado con **Programación Orientada a Objetos** (clases `Autor`, `Post` y `Blog`) y mantiene la organización modular en el paquete `blog/`.

## Cómo ejecutarlo

1. Abrí la terminal y ubicate en la carpeta raíz del proyecto (donde está `main.py`):
   ```bash
   cd blog_consola
   ```
2. Ejecutá el archivo principal:
   ```bash
   python main.py
   ```
   (En Mac puede ser `python3 main.py`.)

No requiere instalar librerías externas (solo usa el módulo `json` y `os`, que vienen con Python).

## Estructura del proyecto

```
blog_consola/
│
├── main.py
├── README.md
├── posts.json
│
└── blog/
    ├── __init__.py
    ├── datos.py
    ├── menu.py
    ├── modelos.py
    ├── operaciones.py
    └── validaciones.py
```

## Responsabilidad de cada archivo

| Archivo | Responsabilidad |
|---|---|
| `main.py` | Punto de entrada. Carga los posts desde `posts.json`, crea la instancia de `Blog`, muestra el menú y llama a los métodos del blog según la opción. Protegido con `if __name__ == "__main__":`. |
| `posts.json` | Archivo donde se guardan los posts (lista de diccionarios en formato JSON). |
| `blog/__init__.py` | Hace que Python reconozca la carpeta `blog/` como un paquete. |
| `blog/modelos.py` | **Nuevo.** Clases `Autor`, `Post` y `Blog`. |
| `blog/datos.py` | **Modificado.** Persistencia: `cargar_posts()` lee `posts.json` y devuelve objetos `Post`; `guardar_posts(lista_dicts)` escribe los diccionarios en `posts.json`. |
| `blog/menu.py` | Muestra el menú y pide datos al usuario (incluye `pedir_datos_post()` para crear un post). |
| `blog/operaciones.py` | Muestra en pantalla los resultados que devuelve la clase `Blog` (`mostrar_posts`, `mostrar_validacion`). |
| `blog/validaciones.py` | `validar_post(post)` revisa que un objeto `Post` tenga título y contenido, un `Autor` con nombre, tags en lista y estado válido. |

## Clases principales

### `Autor`
Representa a la persona que escribe. Atributos: `nombre`, `bio`, `email`.
- `to_dict()`: convierte el autor en diccionario.
- `Autor.from_dict(datos)`: crea un autor desde un diccionario (da error si falta `nombre`).

### `Post`
Representa una publicación. Atributos: `id`, `titulo`, `contenido`, `autor`, `tags`, `estado`.
- **Composición:** el atributo `autor` es un objeto `Autor`, no un texto. Si se intenta crear un `Post` con un autor que no es `Autor`, se lanza un `TypeError`.
- `to_dict()`: convierte el post (y su autor) en diccionario.
- `Post.from_dict(datos)`: crea un post desde un diccionario (da error si faltan claves).
- `tiene_tag(tag)`: indica si el post tiene ese tag, sin distinguir mayúsculas.

### `Blog`
Centraliza la lógica. Su atributo `posts` es una **lista de objetos `Post`**.
- `obtener_posts()`: devuelve todos los posts.
- `buscar_por_titulo(termino)`: búsqueda parcial, ignora mayúsculas/minúsculas.
- `filtrar_por_tag(tag)`: filtra por etiqueta, ignora mayúsculas/minúsculas.
- `crear_post(...)`: crea un `Post` con id automático y lo agrega a la lista (si el autor ya existe, reutiliza el mismo objeto `Autor`).
- `validar_posts()`: valida todos los posts usando `validaciones.py`.
- `a_diccionarios()`: convierte todos los posts en una lista de diccionarios lista para guardar.

## Cómo se guarda y se carga la información (JSON)

JSON no puede guardar objetos de Python directamente, así que se convierten en ambos sentidos:

```
CARGA:   posts.json  ──json.loads──▶  lista de diccionarios  ──Post.from_dict()──▶  objetos Post  ──▶  Blog
GUARDA:  Blog  ──a_diccionarios() / to_dict()──▶  lista de diccionarios  ──json.dumps──▶  posts.json
```

- **Al iniciar**, `main.py` llama a `cargar_posts()` y con esos objetos crea el `Blog`.
- **Al guardar** (opción 6), el blog convierte sus posts a diccionarios y `guardar_posts()` los escribe en `posts.json`.
- **Al salir** (opción 7), si hay posts nuevos sin guardar, el programa pregunta si querés guardarlos.

## Funcionalidades del menú

```
--- MENU DEL BLOG ---
1. Ver todos los posts
2. Buscar por titulo
3. Filtrar por tag
4. Crear nuevo post
5. Validar posts
6. Guardar posts en JSON
7. Salir
```

El post 4 de `posts.json` tiene errores a propósito, para probar la opción 5.

## Manejo de errores

| Situación | Qué hace el programa |
|---|---|
| `posts.json` no existe | Avisa y arranca con el blog vacío. |
| `posts.json` está vacío | Avisa y arranca con el blog vacío. |
| `posts.json` tiene JSON inválido | Muestra el error (con el número de línea) y arranca con el blog vacío. |
| Un post del JSON está incompleto | Lo omite y avisa qué claves le faltan; carga el resto. |
| Opción de menú incorrecta | Muestra "Opción inválida" y vuelve al menú. |
| Campos vacíos al crear un post | Vuelve a pedir el dato hasta que no esté vacío. |
| Guardar objetos sin convertir a diccionario | `guardar_posts()` lo detecta, muestra un error claro y no toca el archivo. |

## Qué cambió respecto a la Preentrega 5

- Se agregó `blog/modelos.py` con las clases `Autor`, `Post` y `Blog`.
- Los posts dejaron de ser diccionarios en memoria: ahora son objetos `Post`, y el autor es un objeto `Autor`.
- Las funciones de búsqueda y filtrado de `operaciones.py` pasaron a ser **métodos de la clase `Blog`**; `operaciones.py` ahora solo muestra resultados.
- `datos.py` ya no tiene los datos escritos en el código: los **lee y guarda en `posts.json`**.
- Se agregaron las opciones **Crear nuevo post** y **Guardar posts en JSON** al menú.
- `validaciones.py` ahora valida objetos `Post` en lugar de diccionarios.
