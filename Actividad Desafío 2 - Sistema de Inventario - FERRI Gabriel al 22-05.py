import flet as ft
import json
import sys

# Defino la clase Producto
class Producto:
    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio

    #Convierto la clase Producto en diccionario para después guardarla en el json
    def to_dict(self):
        return {
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio
        }

#Defino una lista vacía llamada "inventario"
inventario = []

#Función para cargar los datos del inventario desde un archivo.json
def cargar_inventario():
    try:
        with open("inventario.json", "r") as archivo:
            datos_inventario = json.load(archivo)
            return datos_inventario["inventario"]
    except FileNotFoundError:
        return []
#Función para guardar el inventario con los nuevos datos en el archivo.json
def guardar_inventario(inventario_a_guardar):
    with open("inventario.json", "w") as archivo:
        json.dump({"inventario": inventario_a_guardar}, archivo, indent=4)

#INTERFAZ GRÁFICA CON FLET
def main(page: ft.Page):
    page.clean()
    page.title = "Sistema de inventarios"
    
    #Tamaño de la ventana principal
    page.window_width = 700
    page.window_height = 500
    
    #Centrado
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    #Defino ancho de los botones del menu
    ancho_boton = 300
    
    #Defino los botones
    
    #Botón volver uado en varios lados
    def volver(e):
        page.clean()
        main(page)

    # Función para agregar un nuevo producto al inventario
    def button_clicked_agregar(e):
        datos_inventario = cargar_inventario()
        nombre = nombre_field_agregar.value
        categoria = categoria_field_agregar.value
        try:
            precio = int(precio_field_agregar.value)  # Convertir a int
        except ValueError:
            page.snack_bar = ft.SnackBar(
                content=ft.Text("Precio inválido. Ingrese un número entero."),
                open=True,
            )
            page.update()
            main(page)
            return
        
        nuevo_producto = Producto(nombre, categoria, precio)
        datos_inventario.append(nuevo_producto.to_dict())
        guardar_inventario(datos_inventario)

        # Borro los campos utilizados
        nombre_field_agregar.value = ""
        categoria_field_agregar.value = ""
        precio_field_agregar.value = ""
        page.update()

        # Mostrar mensaje de confirmación
        page.snack_bar = ft.SnackBar(
            content=ft.Text("Producto agregado exitosamente!"),
            open=True,
        )
        page.update()
        page.clean()
        main(page)

    # Entradas utilizadas en "agregar productos"
    nombre_field_agregar = ft.TextField(label="Nombre del producto", width=ancho_boton)
    categoria_field_agregar = ft.TextField(label="Categoría del producto", width=ancho_boton)
    precio_field_agregar = ft.TextField(label="Precio del producto", width=ancho_boton, keyboard_type=ft.KeyboardType.NUMBER)
    
    # Función para mostrar la ventana donde se agrega el producto
    def mostrar_vista_agregar_producto(e):
        page.clean()
        page.add(nombre_field_agregar, 
                categoria_field_agregar, 
                precio_field_agregar, 
                ft.ElevatedButton(text="Agregar producto", on_click=button_clicked_agregar, width=ancho_boton),
                ft.ElevatedButton(text="Volver", on_click=volver, width=ancho_boton)
        )
        page.update()

    #Funciones para actualizar un producto del archivo inventario.json
    def button_clicked_actualizar(e):
        page.clean()
        datos_inventario = cargar_inventario()
        nombre_a_actualizar = nombre_field_actualizar.value
        for producto in datos_inventario:
            if nombre_a_actualizar.lower() == producto["nombre"].lower():
                # Mostrar mensaje de confirmación
                page.snack_bar = ft.SnackBar(
                    content=ft.Text("Producto encontrado, actualice los datos"),
                    open=True,
                )
                page.add(nombre_field_actualizado, 
                categoria_field_actualizado, 
                precio_field_actualizado, 
                ft.ElevatedButton(text="Actualizar Producto", on_click=button_clicked_actualizar_2, width=ancho_boton),
                ft.ElevatedButton(text="Volver", on_click=volver, width=ancho_boton)
                )
                break
        else:
            #Mensaje no encontrado
            page.snack_bar = ft.SnackBar(
                    content=ft.Text("Producto no encontrado"),
                    open=True,
            )
            page.update()
            main(page)
        
        page.update()
    
    # Segunda página de actualzar producto -- Se actualizan los datos
    def button_clicked_actualizar_2(e):
        page.clean()
        datos_inventario = cargar_inventario()
        nombre_a_actualizar = nombre_field_actualizar.value
        for producto in datos_inventario:
            if nombre_a_actualizar.lower() == producto["nombre"].lower():
                producto["nombre"] = nombre_field_actualizado.value
                producto["categoria"] = categoria_field_actualizado.value
                try:
                    producto["precio"] = int(precio_field_actualizado.value)  # Convertir a int
                except ValueError:
                    page.snack_bar = ft.SnackBar(
                        content=ft.Text("Precio inválido. Ingrese un número entero."),
                        open=True,
                    )
                    page.update()
                    main(page)
                    return
                
                guardar_inventario(datos_inventario)
                break
        
        page.update()
        page.clean()
        main(page)


    # Función para mostrar la primer ventana para actualizar producto
    def mostrar_vista_actualizar_producto(e):
        page.clean()
        page.add(nombre_field_actualizar, 
                ft.ElevatedButton(text="Buscar producto a actualizar", on_click=button_clicked_actualizar, width=ancho_boton),
                ft.ElevatedButton(text="Volver", on_click=volver, width=ancho_boton)
        )
        page.update()
    
    # Entradas utilizadas en actualizar productos
    nombre_field_actualizar = ft.TextField(label="Nombre del producto a actualizar", width=ancho_boton)
    nombre_field_actualizado = ft.TextField(label="Nombre actualizado", width=ancho_boton)
    categoria_field_actualizado = ft.TextField(label="Categoría actualizada", width=ancho_boton)
    precio_field_actualizado = ft.TextField(label="Precio actualizado", width=ancho_boton, keyboard_type=ft.KeyboardType.NUMBER)
    
    #Función para eliminar un producto del archivo inventario.json
    def button_clicked_eliminar(e):
        page.clean()
        datos_inventario = cargar_inventario()
        producto_a_eliminar = nombre_field_eliminar.value
        for producto in datos_inventario:
            if producto_a_eliminar.lower() == producto["nombre"].lower():
                datos_inventario.remove(producto)
                # Mostrar mensaje de confirmación
                page.snack_bar = ft.SnackBar(
                    content=ft.Text(f"El producto {producto['nombre']} ha sido eliminado correctamente."),
                    open=True,
                )
                guardar_inventario(datos_inventario)
                page.update()
                main(page)
                break
            
        else:
            #Mensaje no encontrado
            page.snack_bar = ft.SnackBar(
                    content=ft.Text("Producto no encontrado"),
                    open=True,
            )
            page.update()
            main(page)
    
    # Función para mostrar la ventana de eliminar producto
    def mostrar_vista_eliminar_producto(e):
        page.clean()
        page.add(nombre_field_eliminar, 
                ft.ElevatedButton(text="Eliminar producto", on_click=button_clicked_eliminar, width=ancho_boton),
                ft.ElevatedButton(text="Volver", on_click=volver, width=ancho_boton)
        )
        page.update()
    
    # Entradas usadas en eliminar productos
    nombre_field_eliminar = ft.TextField(label="Nombre del producto a eliminar", width=ancho_boton)

    #Funciones usadas para ver el inventario (archivo.json)
    def button_clicked_mostrar(e):
        page.clean()
        inventario_actualizado = cargar_inventario()
        inventario_texto = ft.Text("INVENTARIO:\n\n", text_align=ft.TextAlign.CENTER, style= ft.TextThemeStyle.TITLE_MEDIUM)

        for producto in inventario_actualizado:
            nombre = producto['nombre']
            categoria = producto['categoria']
            precio = producto['precio']
            
            producto_info = ft.Text(f"Nombre: {nombre}\nCategoría: {categoria}\nPrecio: {precio}\n\n")
            inventario_texto.value += producto_info.value
        
        inventario_scrollable = ft.ListView(expand=True, spacing=5, controls=[inventario_texto])
        
        page.add(inventario_scrollable, 
                ft.ElevatedButton(text="Volver", on_click=volver, width=ancho_boton),
        )
        page.update()

    #Funciones para buscar productos según distintos criterios
    def button_clicked_buscar_nombre(e):
        page.clean()
        inventario_actualizado = cargar_inventario()
        
        inventario_buscado = ft.Text("Los items que coinciden con su búsqueda son:\n\n", text_align=ft.TextAlign.CENTER, style= ft.TextThemeStyle.TITLE_SMALL)

        nombre_a_buscar = nombre_field_buscar.value
        for producto in inventario_actualizado:
            if nombre_a_buscar.lower() == producto["nombre"].lower():
                nombre = producto['nombre']
                categoria = producto['categoria']
                precio = producto['precio']
                
                producto_info = ft.Text(f"Nombre: {nombre}\nCategoría: {categoria}\nPrecio: {precio}\n\n")
                inventario_buscado.value += producto_info.value
        
        inventario_buscado_scrollable = ft.ListView(expand=True, spacing=5, controls=[inventario_buscado])
        
        page.add(inventario_buscado_scrollable, 
                ft.ElevatedButton(text="Volver", on_click=volver, width=ancho_boton)
        )
        
        page.update()
        
    def button_clicked_buscar_categoria(e):            
        page.clean()
        inventario_actualizado = cargar_inventario()
        categoria_a_buscar = categoria_field_buscar.value
        
        inventario_buscado = ft.Text(f"Los productos de la categoría {categoria_a_buscar} son:\n\n", text_align=ft.TextAlign.CENTER, style= ft.TextThemeStyle.TITLE_SMALL)

        for producto in inventario_actualizado:
            if categoria_a_buscar.lower() == producto["categoria"].lower():
                nombre = producto['nombre']
                precio = producto['precio']
                
                producto_info = ft.Text(f"Nombre: {nombre}\nPrecio: {precio}\n\n")
                inventario_buscado.value += producto_info.value
        
        inventario_buscado_scrollable = ft.ListView(expand=True, spacing=5, controls=[inventario_buscado])
        
        page.add(inventario_buscado_scrollable, 
                ft.ElevatedButton(text="Volver", on_click=volver, width=ancho_boton)
        )
        
        page.update()

    def button_clicked_buscar_precio(e):            
        page.clean()
        inventario_actualizado = cargar_inventario()
        try:
            precio_a_buscar = int(precio_field_buscar.value)  # Convertir a int
        except ValueError:
            page.snack_bar = ft.SnackBar(
                content=ft.Text("Precio inválido. Ingrese un número entero."),
                open=True,
            )
            page.update()
            main(page)
            return
        
        inventario_buscado = ft.Text(f"Los items que valen {precio_a_buscar} son:\n\n", text_align=ft.TextAlign.CENTER, style= ft.TextThemeStyle.TITLE_SMALL)

        for producto in inventario_actualizado:
            if precio_a_buscar == producto["precio"]:
                nombre = producto['nombre']
                categoria = producto['categoria']
                
                producto_info = ft.Text(f"Nombre: {nombre}\nCategoría: {categoria}\n\n")
                inventario_buscado.value += producto_info.value
        
        inventario_buscado_scrollable = ft.ListView(expand=True, spacing=5, controls=[inventario_buscado])
        
        page.add(inventario_buscado_scrollable,
                ft.ElevatedButton(text="Volver", on_click=volver, width=ancho_boton)
        )
        
        page.update()

    # Función para mostrar la ventana de buscar producto -- donde se eligen los criterios
    def mostrar_vista_buscar_producto(e):
        page.clean()
        title_buscar = ft.Text("Elija un criterio para buscar:")
        page.add(title_buscar, 
                ft.ElevatedButton(text="por Nombre", on_click=mostrar_vista_buscar_producto_2_nombre, width=ancho_boton),
                ft.ElevatedButton(text="por Categoría", on_click=mostrar_vista_buscar_producto_2_categoria, width=ancho_boton),
                ft.ElevatedButton(text="por Precio", on_click=mostrar_vista_buscar_producto_2_precio, width=ancho_boton),
                ft.ElevatedButton(text="Volver", on_click=volver, width=ancho_boton)
        )
        page.update()
    
    # Entradas usadas para buscar productos
    nombre_field_buscar = ft.TextField(label="Nombre del producto a buscar", width=ancho_boton)
    categoria_field_buscar = ft.TextField(label="Nombre de la categoría a buscar", width=ancho_boton)
    precio_field_buscar = ft.TextField(label="Precio a buscar", width=ancho_boton, keyboard_type=ft.KeyboardType.NUMBER)
    
    #Las ventanas que se abren una vez que se elije el criterio
    def mostrar_vista_buscar_producto_2_nombre(e):
        page.clean()
        page.add(nombre_field_buscar, 
                ft.ElevatedButton(text="Buscar por nombre del producto", on_click=button_clicked_buscar_nombre, width=ancho_boton),
                ft.ElevatedButton(text="Volver", on_click=volver, width=ancho_boton)
        )
        page.update()
    
    def mostrar_vista_buscar_producto_2_categoria(e):
        page.clean()
        page.add(categoria_field_buscar, 
                ft.ElevatedButton(text="Buscar por categoría del producto", on_click=button_clicked_buscar_categoria, width=ancho_boton),
                ft.ElevatedButton(text="Volver", on_click=volver, width=ancho_boton)
        )
        page.update()
    
    def mostrar_vista_buscar_producto_2_precio(e):
        page.clean()
        page.add(precio_field_buscar, 
                ft.ElevatedButton(text="Buscar por precio del producto", on_click=button_clicked_buscar_precio, width=ancho_boton),
                ft.ElevatedButton(text="Volver", on_click=volver, width=ancho_boton)
        )
        page.update()
    
    #Botón para cerrar la aplicación
    def button_clicked_salir(e):
        page.window_close()
        sys.exit()
    
    # Menu interactivo
    menu = ft.Text("MENU PRINCIPAL", style=ft.TextThemeStyle.TITLE_MEDIUM)
    m1 = ft.ElevatedButton(text="Agregar un nuevo producto", width=ancho_boton, on_click=mostrar_vista_agregar_producto)
    m2 = ft.ElevatedButton(text="Actualizar un producto", width=ancho_boton, on_click=mostrar_vista_actualizar_producto)
    m3 = ft.ElevatedButton(text="Eliminar un producto", width=ancho_boton, on_click=mostrar_vista_eliminar_producto)
    m4 = ft.ElevatedButton(text="Ver el inventario", width=ancho_boton, on_click=button_clicked_mostrar)
    m5 = ft.ElevatedButton(text="Buscar un producto", width=ancho_boton, on_click=mostrar_vista_buscar_producto)
    m6 = ft.ElevatedButton(text="Salir", color=ft.colors.RED, width=ancho_boton, on_click=button_clicked_salir)
    page.add(menu, m1, m2, m3, m4, m5, m6)

ft.app(main)