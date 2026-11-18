"""Archivo principal: carga los datos, crea el Blog y coordina el menú."""

from blog.datos import cargar_posts, guardar_posts
from blog.menu import mostrar_menu, pedir_texto, pedir_datos_post, confirmar
from blog.modelos import Blog
from blog.operaciones import mostrar_posts, mostrar_validacion


def guardar(blog):
    """Convierte los posts a diccionarios y los guarda en posts.json."""
    if guardar_posts(blog.a_diccionarios()):
        print(f"Se guardaron {len(blog.obtener_posts())} post(s) en posts.json.")
        return True
    return False


def main():
    print("Bienvenido al Blog por consola")
    blog = Blog("Blog de Cristóbal", cargar_posts())
    print(f"Se cargaron {len(blog.obtener_posts())} post(s) desde posts.json.")
    cambios_sin_guardar = False

    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            mostrar_posts(blog.obtener_posts())
        elif opcion == "2":
            termino = pedir_texto("Término a buscar: ")
            resultados = blog.buscar_por_titulo(termino)
            print(f"Se encontraron {len(resultados)} post(s):")
            mostrar_posts(resultados)
        elif opcion == "3":
            tag = pedir_texto("Tag a filtrar: ")
            resultados = blog.filtrar_por_tag(tag)
            print(f"Se encontraron {len(resultados)} post(s) con el tag '{tag}':")
            mostrar_posts(resultados)
        elif opcion == "4":
            datos = pedir_datos_post()
            try:
                post = blog.crear_post(**datos)
                cambios_sin_guardar = True
                print(f"Post creado: {post}")
                print("Recordá guardar (opción 6) para que quede en posts.json.")
            except ValueError as error:
                print(f"No se pudo crear el post: {error}")
        elif opcion == "5":
            mostrar_validacion(blog.validar_posts())
        elif opcion == "6":
            if guardar(blog):
                cambios_sin_guardar = False
        elif opcion == "7":
            if cambios_sin_guardar and confirmar("Hay cambios sin guardar. ¿Guardar antes de salir?"):
                guardar(blog)
            print("¡Gracias por usar el blog! Hasta luego.")
            break
        else:
            print("Opción inválida. Elegí un número del 1 al 7.")


if __name__ == "__main__":
    main()
