# Blog por consola – Preentrega 5 (Organización modular)

Sistema de blog que se usa desde la terminal. Permite **ver todos los posts**, **buscar por título**, **filtrar por tag** y **validar la estructura** de los posts cargados en memoria.

En esta versión el código está separado en módulos dentro de un paquete (`blog/`), para que sea más fácil de leer, mantener y escalar.

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

No requiere instalar librerías externas.

## Estructura del proyecto

```
blog_consola/
│
├── main.py
├── README.md
│
└── blog/
    ├── __init__.py
    ├── datos.py
    ├── menu.py
    ├── operaciones.py
    └── validaciones.py
```

## Responsabilidad de cada archivo

| Archivo | Responsabilidad |
|---|---|
| `main.py` | Archivo principal que se ejecuta. Importa los módulos del paquete, coordina el flujo del menú y llama a la función correspondiente según la opción. La ejecución está protegida con `if __name__ == "__main__":`. |
| `blog/__init__.py` | Hace que Python reconozca la carpeta `blog/` como un paquete. |
| `blog/datos.py` | Estructuras de datos base: `perfil_autor`, `estados_post`, `etiquetas_blog` y `posts`. El autor es un diccionario anidado dentro de cada post. |
| `blog/menu.py` | Muestra el menú y maneja el `input()` del usuario. |
| `blog/operaciones.py` | Funciones del blog: `listar_posts(lista)`, `buscar_por_titulo(lista, termino)` y `filtrar_por_tag(lista, tag)`. Reciben los datos por parámetro. |
| `blog/validaciones.py` | Reglas lógicas: `validar_post(post)` revisa que sea un diccionario, que tenga las claves necesarias, título y contenido no vacíos, autor como diccionario con nombre, tags como lista y estado válido. |

## Funcionalidades del menú

```
--- MENU DEL BLOG ---
1. Ver todos los posts
2. Buscar por titulo
3. Filtrar por tag
4. Validar posts
5. Salir
```

1. **Ver todos los posts:** muestra título, nombre del autor y estado.
2. **Buscar por título:** coincidencia total o parcial, sin distinguir mayúsculas/minúsculas (`.lower()`).
3. **Filtrar por tag:** muestra los posts con esa etiqueta, sin distinguir mayúsculas/minúsculas (`.lower()`).
4. **Validar posts:** indica qué posts son válidos y cuáles tienen errores (el post 4 tiene errores a propósito para probar las validaciones).
5. **Salir:** muestra un mensaje de despedida y termina el programa.
