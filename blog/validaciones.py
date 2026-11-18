"""Reglas lógicas y validaciones del blog."""

from blog.datos import estados_post

CLAVES_REQUERIDAS = ("titulo", "contenido", "autor", "tags", "estado")


def validar_post(post):
    """Valida la estructura de un post.

    Retorna una tupla (es_valido, lista_de_errores).
    """
    errores = []

    if not isinstance(post, dict):
        return False, ["El post no es un diccionario."]

    for clave in CLAVES_REQUERIDAS:
        if clave not in post:
            errores.append(f"Falta la clave '{clave}'.")

    if not str(post.get("titulo", "")).strip():
        errores.append("El título está vacío.")

    if not str(post.get("contenido", "")).strip():
        errores.append("El contenido está vacío.")

    autor = post.get("autor")
    if not isinstance(autor, dict):
        errores.append("El autor debe ser un diccionario.")
    elif not str(autor.get("nombre", "")).strip():
        errores.append("El autor no tiene nombre.")

    if not isinstance(post.get("tags"), list):
        errores.append("Los tags deben ser una lista.")

    if post.get("estado") not in estados_post:
        errores.append(f"Estado inválido: '{post.get('estado')}'.")

    return len(errores) == 0, errores
