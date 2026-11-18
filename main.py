"""Archivo principal: orquesta el blog por consola."""

from blog.datos import posts
from blog.menu import mostrar_menu, pedir_texto
from blog.operaciones import listar_posts, buscar_por_titulo, filtrar_por_tag
from blog.validaciones import validar_post


def ejecutar_validacion(lista):
    """Recorre los posts y muestra cuáles son válidos y cuáles tienen errores."""
    for numero, post in enumerate(lista, start=1):
        es_valido, errores = validar_post(post)
        titulo = post.get("titulo") if isinstance(post, dict) else None
        nombre = titulo or f"Post #{numero}"
        if es_valido:
            print(f"✔ {nombre}: válido")
        else:
            print(f"✘ {nombre}: con errores")
            for error in errores:
                print(f"    - {error}")


def main():
    print("Bienvenido al Blog por consola")
    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            listar_posts(posts)
        elif opcion == "2":
            termino = pedir_texto("Término a buscar: ")
            resultados = buscar_por_titulo(posts, termino)
            print(f"Se encontraron {len(resultados)} post(s):")
            listar_posts(resultados)
        elif opcion == "3":
            tag = pedir_texto("Tag a filtrar: ")
            resultados = filtrar_por_tag(posts, tag)
            print(f"Se encontraron {len(resultados)} post(s) con el tag '{tag}':")
            listar_posts(resultados)
        elif opcion == "4":
            ejecutar_validacion(posts)
        elif opcion == "5":
            print("¡Gracias por usar el blog! Hasta luego.")
            break
        else:
            print("Opción inválida. Elegí un número del 1 al 5.")


if __name__ == "__main__":
    main()
