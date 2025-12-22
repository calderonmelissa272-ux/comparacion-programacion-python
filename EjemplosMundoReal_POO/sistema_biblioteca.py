 # Sistema de gestión de biblioteca
# Ejemplo del mundo real usando Programación Orientada a Objetos (POO)

class Libro:
    """
    Clase que representa un libro en la biblioteca.
    """
    def _init_(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponible = True

    def prestar(self):
        """
        Método para prestar el libro.
        """
        if self.disponible:
            self.disponible = False
            print(f"El libro '{self.titulo}' ha sido prestado.")
        else:
            print(f"El libro '{self.titulo}' no está disponible.")

    def devolver(self):
        """
        Método para devolver el libro.
        """
        self.disponible = True
        print(f"El libro '{self.titulo}' ha sido devuelto.")


class Usuario:
    """
    Clase que representa un usuario de la biblioteca.
    """
    def _init_(self, nombre):
        self.nombre = nombre
        self.libros_prestados = []

    def tomar_libro(self, libro):
        """
        Método que permite al usuario tomar un libro prestado.
        """
        if libro.disponible:
            libro.prestar()
            self.libros_prestados.append(libro)
        else:
            print("No se puede prestar el libro.")


# Interacción entre objetos
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez")
usuario1 = Usuario("Melissa")

usuario1.tomar_libro(libro1)
libro1.devolver()
