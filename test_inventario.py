import unittest
from inventario import Producto, \
    Inventario  # Asegúrate de que el nombre de tu archivo con el código principal sea 'inventario.py'


class TestInventario(unittest.TestCase):

    def test_agregar_producto(self):
        inventario = Inventario()
        producto = Producto("Manzana", 1.0, 10)
        inventario.agregar_producto(producto)
        self.assertIn(producto, inventario.productos)

    def test_eliminar_producto(self):
        inventario = Inventario()
        producto = Producto("Manzana", 1.0, 10)
        inventario.agregar_producto(producto)
        inventario.eliminar_producto("Manzana")
        self.assertNotIn(producto, inventario.productos)


if __name__ == "__main__":
    unittest.main()
