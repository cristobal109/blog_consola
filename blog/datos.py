"""Estructuras de datos base del blog."""

perfil_autor = {
    "nombre": "Cristóbal Pérez",
    "email": "cristobal@example.com",
    "bio": "Estudiante de marketing que aprende Python.",
}

estados_post = ("borrador", "publicado", "archivado")

etiquetas_blog = {"python", "programacion", "marketing", "web", "ia"}

posts = [
    {
        "id": 1,
        "titulo": "Mi primer script en Python",
        "contenido": "Hoy configuré el entorno y ejecuté mi primer script.",
        "autor": perfil_autor,
        "tags": ["python", "programacion"],
        "estado": "publicado",
    },
    {
        "id": 2,
        "titulo": "Listas y diccionarios",
        "contenido": "Cómo modelar los datos de un blog con estructuras de Python.",
        "autor": perfil_autor,
        "tags": ["python"],
        "estado": "publicado",
    },
    {
        "id": 3,
        "titulo": "Marketing digital e IA",
        "contenido": "Ideas sobre cómo la IA cambia el marketing.",
        "autor": perfil_autor,
        "tags": ["marketing", "ia"],
        "estado": "borrador",
    },
    {
        # Post con errores a propósito, para probar las validaciones
        "id": 4,
        "titulo": "",
        "contenido": "Post incompleto de prueba.",
        "autor": "Ana López",
        "tags": "web",
        "estado": "pendiente",
    },
]
