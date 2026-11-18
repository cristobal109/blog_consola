"""Menú e interacción con el usuario (input)."""

from blog.validaciones import ESTADOS_POST


def mostrar_menu():
    """Muestra las opciones, pide una al usuario y la retorna."""
    print("\n--- MENU DEL BLOG ---")
    print("1. Ver todos los posts")
    print("2. Buscar por titulo")
    print("3. Filtrar por tag")
    print("4. Crear nuevo post")
    print("5. Validar posts")
    print("6. Guardar posts en JSON")
    print("7. Salir")
    return input("Elegí una opción: ").strip()


def pedir_texto(mensaje):
    """Pide un texto al usuario y lo retorna sin espacios sobrantes."""
    return input(mensaje).strip()


def pedir_obligatorio(mensaje):
    """Pide un texto y lo vuelve a pedir mientras esté vacío."""
    while True:
        texto = pedir_texto(mensaje)
        if texto:
            return texto
        print("Este campo es obligatorio, no puede quedar vacío.")


def pedir_datos_post():
    """Pide por consola los datos de un nuevo post y los retorna en un diccionario."""
    print("\n--- NUEVO POST ---")
    titulo = pedir_obligatorio("Título: ")
    contenido = pedir_obligatorio("Contenido: ")
    nombre_autor = pedir_obligatorio("Nombre del autor: ")
    bio_autor = pedir_texto("Bio del autor (opcional): ")
    tags_texto = pedir_texto("Tags separados por coma (ej: python, web): ")
    tags = [t.strip().lower() for t in tags_texto.split(",") if t.strip()]

    opciones = "/".join(ESTADOS_POST)
    while True:
        estado = pedir_texto(f"Estado ({opciones}) [borrador]: ").lower() or "borrador"
        if estado in ESTADOS_POST:
            break
        print(f"Estado inválido. Opciones: {opciones}.")

    return {
        "titulo": titulo,
        "contenido": contenido,
        "nombre_autor": nombre_autor,
        "bio_autor": bio_autor,
        "tags": tags,
        "estado": estado,
    }


def confirmar(mensaje):
    """Pregunta s/n y retorna True si la respuesta es 's'."""
    return pedir_texto(f"{mensaje} (s/n): ").lower() == "s"
