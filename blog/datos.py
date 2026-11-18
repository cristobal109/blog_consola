"""Persistencia del blog: carga y guardado de posts en posts.json."""

import json
import os

from blog.modelos import Post

# posts.json vive en la carpeta raíz del proyecto (al lado de main.py)
RUTA_JSON = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "posts.json")


def cargar_posts(ruta=RUTA_JSON):
    """Lee posts.json y retorna una lista de objetos Post.

    Si el archivo no existe, está vacío o es inválido, avisa y retorna
    una lista vacía en lugar de cerrar el programa.
    """
    if not os.path.exists(ruta):
        print(f"Aviso: no se encontró '{os.path.basename(ruta)}'. Se empieza con el blog vacío.")
        return []

    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
    except OSError as error:
        print(f"Error: no se pudo leer el archivo ({error}). Se empieza con el blog vacío.")
        return []

    if not contenido.strip():
        print("Aviso: posts.json está vacío. Se empieza con el blog vacío.")
        return []

    try:
        datos = json.loads(contenido)
    except json.JSONDecodeError as error:
        print(f"Error: posts.json tiene contenido inválido (línea {error.lineno}). Se empieza con el blog vacío.")
        return []

    if not isinstance(datos, list):
        print("Error: posts.json debe contener una lista de posts. Se empieza con el blog vacío.")
        return []

    posts = []
    for numero, item in enumerate(datos, start=1):
        try:
            posts.append(Post.from_dict(item))  # diccionario -> objeto
        except (ValueError, TypeError) as error:
            print(f"Aviso: se omitió el post #{numero} de posts.json porque está incompleto: {error}")
    return posts


def guardar_posts(lista_dicts, ruta=RUTA_JSON):
    """Guarda en posts.json una lista de diccionarios.

    Retorna True si se guardó bien y False si hubo un error.
    """
    if not isinstance(lista_dicts, list) or not all(isinstance(p, dict) for p in lista_dicts):
        print("Error: antes de guardar, los posts deben convertirse a diccionarios (usá Blog.a_diccionarios()).")
        return False

    try:
        # Primero se genera el texto: si algo no es serializable, falla acá
        # y no se pisa el archivo con datos a medias.
        texto = json.dumps(lista_dicts, ensure_ascii=False, indent=4)
    except TypeError as error:
        print(f"Error: hay datos que no se pueden guardar en JSON ({error}).")
        return False

    try:
        with open(ruta, "w", encoding="utf-8") as archivo:
            archivo.write(texto)
    except OSError as error:
        print(f"Error: no se pudo escribir el archivo ({error}).")
        return False
    return True
