class libro:
    def __init__(self, titulo, autor, ano_publi, codigo):
        self.titulo=titulo
        self.autor=autor
        self.ano=ano_publi
        self.codigo=codigo
        self.disponible = True

    def __str__(self):
         estado = "Disponible" if self.disponible else "Prestado"
         return f"[{self.codigo}]{self.titulo} - {self.autor}  ({self.ano}) - {estado}"

class usuario:
    def __init__(self,nombre,carnet,carrera):
        self.nombre=nombre
        self.carnet=carnet
        self.carrera=carrera

    def __str__(self):
        return f"{self.nombre}({self.carnet})-{self.carrera}"

class prestados:
    def __init__(self,libro,ususario,fecha_presta,fecha_devolu=None):
        self.libro=libro
        self.usuario=usuario
        self.fecha_presta=fecha_presta
        self.fecha_devolu=fecha_devolu
    def devolucion(self):
        self.fecha_devolu=self.fecha_presta
        self.libro.disponible=True

class gestionlibros:
    def __init__(self):
        self.libros={}
    def registro_libro(self,titulo, autor, ano_publi, codigo):
        if codigo in self.libros:
            raise ValueError ("Codigo del libro existente.")
        self.libros[codigo]= libro(titulo, autor, ano_publi, codigo)
    def buscar_libro(self,codigo):
        return self.libros.get(codigo)

    def muestra_libro(self):
        return list(self.libros.values())

