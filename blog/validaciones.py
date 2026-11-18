"""Reglas lógicas y validaciones del blog."""

ESTADOS_POST = ("borrador", "publicado", "archivado")


def validar_post(post):
    """Valida que un objeto Post tenga datos correctos.

    Retorna una tupla (es_valido, lista_de_errores).
    """
    # Import local para evitar una importación circular con modelos.py
    from blog.modelos import Autor, Post

    if not isinstance(post, Post):
        return False, ["No es un objeto Post."]

    errores = []

    if not str(post.titulo).strip():
        errores.append("El título está vacío.")

    if not str(post.contenido).strip():
        errores.append("El contenido está vacío.")

    if not isinstance(post.autor, Autor):
        errores.append("El autor debe ser un objeto Autor.")
    elif not str(post.autor.nombre).strip():
        errores.append("El autor no tiene nombre.")

    if not isinstance(post.tags, list):
        errores.append("Los tags deben ser una lista.")

    if post.estado not in ESTADOS_POST:
        errores.append(f"Estado inválido: '{post.estado}'.")

    return len(errores) == 0, errores
