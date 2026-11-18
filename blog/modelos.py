"""Modelos del blog: clases Autor, Post y Blog."""

from blog.validaciones import validar_post


class Autor:
    """Representa a una persona autora del blog."""

    def __init__(self, nombre, bio="", email=""):
        self.nombre = nombre
        self.bio = bio
        self.email = email

    def to_dict(self):
        """Convierte el autor a un diccionario compatible con JSON."""
        return {"nombre": self.nombre, "bio": self.bio, "email": self.email}

    @classmethod
    def from_dict(cls, datos):
        """Crea un Autor a partir de un diccionario.

        Lanza ValueError si el diccionario no tiene la clave 'nombre'.
        """
        if not isinstance(datos, dict):
            raise ValueError("los datos del autor deben ser un diccionario.")
        if "nombre" not in datos:
            raise ValueError("al autor le falta la clave 'nombre'.")
        return cls(datos["nombre"], datos.get("bio", ""), datos.get("email", ""))

    def __str__(self):
        return self.nombre


class Post:
    """Representa una publicación del blog. Su autor es un objeto Autor."""

    CLAVES_REQUERIDAS = ("id", "titulo", "contenido", "autor", "tags", "estado")

    def __init__(self, id, titulo, contenido, autor, tags=None, estado="borrador"):
        if not isinstance(autor, Autor):
            raise TypeError("el autor de un Post debe ser una instancia de Autor.")
        self.id = id
        self.titulo = titulo
        self.contenido = contenido
        self.autor = autor  # Composición: el post "tiene un" Autor
        self.tags = tags if tags is not None else []
        self.estado = estado

    def to_dict(self):
        """Convierte el post (y su autor) a un diccionario compatible con JSON."""
        return {
            "id": self.id,
            "titulo": self.titulo,
            "contenido": self.contenido,
            "autor": self.autor.to_dict(),
            "tags": self.tags,
            "estado": self.estado,
        }

    @classmethod
    def from_dict(cls, datos):
        """Crea un Post a partir de un diccionario cargado desde JSON.

        Lanza ValueError si el diccionario está incompleto.
        """
        if not isinstance(datos, dict):
            raise ValueError("cada post debe ser un diccionario.")
        faltantes = [c for c in cls.CLAVES_REQUERIDAS if c not in datos]
        if faltantes:
            raise ValueError(f"faltan las claves {', '.join(faltantes)}.")
        autor = Autor.from_dict(datos["autor"])
        return cls(
            datos["id"],
            datos["titulo"],
            datos["contenido"],
            autor,
            datos["tags"],
            datos["estado"],
        )

    def tiene_tag(self, tag):
        """Indica si el post tiene el tag (ignora mayúsculas/minúsculas)."""
        if not isinstance(self.tags, list):
            return False
        return tag.lower() in [str(t).lower() for t in self.tags]

    def __str__(self):
        titulo = self.titulo or "(sin título)"
        return f"[{self.id}] {titulo} | Autor: {self.autor} | Estado: {self.estado}"


class Blog:
    """Centraliza la lógica del blog y guarda la lista de objetos Post."""

    def __init__(self, nombre, posts=None):
        self.nombre = nombre
        self.posts = posts if posts is not None else []

    def obtener_posts(self):
        """Retorna todos los posts cargados."""
        return self.posts

    def buscar_por_titulo(self, termino):
        """Retorna los posts cuyo título contiene el término (ignora mayúsculas)."""
        termino = termino.lower()
        return [p for p in self.posts if termino in str(p.titulo).lower()]

    def filtrar_por_tag(self, tag):
        """Retorna los posts que tienen el tag indicado (ignora mayúsculas)."""
        return [p for p in self.posts if p.tiene_tag(tag)]

    def siguiente_id(self):
        """Calcula el próximo id disponible."""
        ids = [p.id for p in self.posts if isinstance(p.id, int)]
        return max(ids, default=0) + 1

    def buscar_autor(self, nombre):
        """Retorna el Autor ya existente con ese nombre, o None."""
        for post in self.posts:
            if post.autor.nombre.lower() == nombre.lower():
                return post.autor
        return None

    def crear_post(self, titulo, contenido, nombre_autor, bio_autor="", tags=None, estado="borrador"):
        """Crea un Post nuevo, lo agrega al blog y lo retorna.

        Lanza ValueError si hay campos obligatorios vacíos.
        """
        for campo, valor in (("título", titulo), ("contenido", contenido), ("autor", nombre_autor)):
            if not str(valor).strip():
                raise ValueError(f"el campo '{campo}' no puede estar vacío.")

        # Si el autor ya existe en el blog, se reutiliza el mismo objeto
        autor = self.buscar_autor(nombre_autor) or Autor(nombre_autor, bio_autor)
        post = Post(self.siguiente_id(), titulo, contenido, autor, tags or [], estado)
        self.posts.append(post)
        return post

    def validar_posts(self):
        """Valida todos los posts. Retorna una lista de (post, es_valido, errores)."""
        resultados = []
        for post in self.posts:
            es_valido, errores = validar_post(post)
            resultados.append((post, es_valido, errores))
        return resultados

    def a_diccionarios(self):
        """Convierte todos los posts a una lista de diccionarios para JSON."""
        return [post.to_dict() for post in self.posts]
