tu_nombre = input("Hola buen día, puedes indicarme tu nombre? ")

print("Hola", tu_nombre,", me llamo Facturafacil.py. He nacido para ayudarte a automatizar el proceso de recordar tus compras. Bienvenid@ :)")

#Aquí iniciamos una  nueva instancia de la clase Factura con el nombre del cliente y una lista vacía de productos.
class Factura:
    def __init__(self, cliente):
       
        
        self.cliente = cliente
        self.productos = []

#Agregamos a continuación un producto nuevo

    def agregar_producto(self, nombre, cantidad, precio_unitario):
        
        if cantidad <= 0 or precio_unitario <= 0:
            raise ValueError("Disculpa, pero la cantidad y precio unitario deben ser mayores a cero. Te debes haber equivocado al teclear, revísalo :)")
        self.productos.append({'nombre': nombre, 'cantidad': cantidad, 'precio_unitario': precio_unitario})

    def eliminar_producto(self, nombre):
        """
        Elimina un producto de la factura por su nombre.
        """
        for producto in self.productos:
            if producto['nombre'] == nombre:
                self.productos.remove(producto)
                return
        raise ValueError("No podemos eliminar algo que no existe... ¿O sí? Esas son preguntas para filósofos, no para un programa de facturación. Revisa el dator e introduce un nuevo producto por favor4")

    def mostrar_productos(self):
        """
        Muestra todos los productos en la factura.
        """
        if not self.productos:
            print("No hay productos en la factura. Así que... no has comprado nada :( no puedo ayudarte")
        else:
            for producto in self.productos:
                print(f"Producto: {producto['nombre']}, Cantidad: {producto['cantidad']}, Precio Unitario: {producto['precio_unitario']}")

    def calcular_total(self):
        """
        Calcula y devuelve el total de la factura.
        """
        total = sum(producto['cantidad'] * producto['precio_unitario'] for producto in self.productos)
        return total

def main():
    """
    Función principal que permite la interacción del usuario con la clase Factura.
    """
   
    cliente = input( " Ingrese por favor los datos del cliente: ")
    factura = Factura(cliente)

    while True:
        print("\nOpciones:")
        print("Marque 1 para agregar un nuevo producto")
        print("Marque 2 para eliminar un producto (Recuerda que no podrás recuperarlo después)")
        print("Marque 3 para ver su lista de productos")
        print("Marque 4 para ver por cuánto le sale la 'multa'")
        print("Marque 5 para cerrar el programa")

        opcion = input("Seleccione una opción: ")

        try:
            if opcion == '1':
                nombre = input("Nombre del producto: ")
                cantidad = int(input("Cantidad: "))
                precio_unitario = float(input("Precio unitario: "))
                factura.agregar_producto(nombre, cantidad, precio_unitario)
                print(f"¡Listo! Producto '{nombre}' agregado correctamente.")
            
            elif opcion == '2':
                nombre = input("Nombre del producto a eliminar: ")
                factura.eliminar_producto(nombre)
                print(f"Producto '{nombre}' eliminado. Chao '{nombre}'! ")
            
            elif opcion == '3':
                print("Productos en la factura:")
                factura.mostrar_productos()
            
            elif opcion == '4':
                total = factura.calcular_total()
                print(f"Total del precio de la cesta: {total}")
            
            elif opcion == '5':
                print("Saliendo del programa. ¡Hasta pronto!")
                break
            
            else:
                print("Estoy un poco confundido. Creo que no te he dado esa opción... prueba de nuevo")
        
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Se ha producido un error inesperado: {e}")

if __name__ == "__main__":
    main()

