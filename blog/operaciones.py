"""Operaciones de salida: muestran en pantalla lo que devuelve la clase Blog."""


def mostrar_posts(lista):
    """Muestra título, autor y estado de cada Post de la lista."""
    if not lista:
        print("No hay posts para mostrar.")
        return
    for post in lista:
        print(f"- {post}")


def mostrar_validacion(resultados):
    """Muestra el resultado de Blog.validar_posts()."""
    if not resultados:
        print("No hay posts para validar.")
        return
    for post, es_valido, errores in resultados:
        nombre = post.titulo or f"Post #{post.id}"
        if es_valido:
            print(f"✔ {nombre}: válido")
        else:
            print(f"✘ {nombre}: con errores")
            for error in errores:
                print(f"    - {error}")
