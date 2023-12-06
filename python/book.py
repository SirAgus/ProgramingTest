class SQL:

    seq = 0

    def create(self, table_name="books", *args, **kwargs):
        print("Creando registro nuevo")
        print(table_name)
        print(args)
        print(kwargs)
        SQL.seq += 1
        return SQL.seq

    def update(self, record_id, table_name="books", *args, **kwargs):
        print(f"Actulizando {table_name} con id: {record_id}")
        print(f"Valores: {args}")
        print(kwargs)

    def list(self, table_name="books"):
        print(f"Lista de {table_name}")

    def retrieve(self, record_id, table_name="books"):
        print(f"Se obtiene {record_id} desde {table_name}")

    def delete(self, record_id, table_name="books"):
        print(f"Se elimino {record_id} desde {table_name}")


class Book:

    def __init__(self, titulo, nombre_autor, fecha_publicacion):
        self.id = None
        self.titulo = titulo
        self.nombre_Autor = nombre_autor
        self.fecha_publicacion = fecha_publicacion

    def save(self):
        if self.id is None:
            self.id = SQL().create("books", self.titulo, self.nombre_Autor, self.fecha_publicacion)
        else:
            print('id ya existente')

    def update(self):
        if self.id is not None:
            SQL().update(self.id, "books", self.titulo,
                         self.nombre_Autor, self.fecha_publicacion)

    def list(self):
        SQL().list("books")

    def retrieve(self):
        SQL().retrieve(self.id, "books")

    def delete(self):
        if self.id is not None:
            SQL().delete(self.id, "books")
