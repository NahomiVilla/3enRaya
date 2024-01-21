import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class CrearMenuDesplegable:
    def __init__(self,background_label):
        self.rutas_seleccionadas = {
            "Cruz": None,
            "Circulo": None,
            "Imagen de Ganador": None
        }

        # Diccionario para almacenar los botones por opción
        self.botones_por_opcion = {}
        self.background_label=background_label
        self.ventana = tk.Toplevel(self.background_label)
        self.ventana.title('Seleccion de Imagen')
        ancho_ventana = 300
        alto_ventana = 250
        x_ventana = (self.background_label.winfo_screenwidth() - ancho_ventana) // 2
        y_ventana = (self.background_label.winfo_screenheight() - alto_ventana) // 2
        self.ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{x_ventana}+{y_ventana}")

        # Crear menú
        opciones = ['Cruz', 'Circulo', 'Imagen de Ganador']
        seleccion = tk.StringVar()
        self.combo = ttk.Combobox(self.ventana, values=opciones, textvariable=seleccion)
        self.combo.bind('<<ComboboxSelected>>', self.on_select)
        self.combo.pack(pady=10)

        # Frame para contener los cuadrados
        self.frame_cuadrados = tk.Frame(self.ventana)
        self.frame_cuadrados.pack(pady=10)

        # Frame botones guardar y cancelar
        self.frame_g_c = tk.Frame(self.ventana)
        self.frame_g_c.pack(pady=10)

        # Botón guardar
        self.boton_guardar = tk.Button(self.frame_g_c, text="Guardar", command=self.guardar_selecciones)
        self.boton_guardar.pack(side=tk.LEFT, padx=10, pady=10)

        # Botón para cerrar la ventana
        self.boton_cerrar = tk.Button(self.frame_g_c, text="Cancelar", command=self.ventana.destroy)
        self.boton_cerrar.pack(side=tk.LEFT, padx=10, pady=10)
    def cargar_imagen(self, ruta, size=(30, 30)):
        imagen = Image.open(ruta)
        imagen = imagen.resize(size, Image.ANTIALIAS)
        imagen_tk = ImageTk.PhotoImage(imagen)
        return imagen_tk

    def crear_menu_cuadrados(self, opcion):
        #print(opcion)
        # Limpiar el frame de cuadrados antes de agregar nuevos
        for widget in self.frame_cuadrados.winfo_children():
            widget.destroy()

        # Función para ejecutar cuando se selecciona un cuadrado
        def seleccionar_cuadrado(ruta):
            self.rutas_seleccionadas[opcion] = ruta
            #print(f"Ruta seleccionada para {opcion}: {self.rutas_seleccionadas[opcion]}")

        # Diccionario de rutas de imágenes por opción
        rutas_por_opcion = {
            "Cruz": ("imagenes-img\\cruz.png", "imagenes-img\\cruz_200.png"),
            "Circulo": ("imagenes-img\\circulo.png", "imagenes-img\\circulo_200_2.png"),
            "Imagen de Ganador": ("imagenes-img\\ganador1.png", "imagenes-img\\ganador2.png")
        }

        # Obtener las rutas de imágenes según la opción seleccionada
        rutas_imagenes = rutas_por_opcion.get(opcion, (None, None))

        # Crear un menú de cuadrados con imágenes
        for i, ruta_imagen in enumerate(rutas_imagenes):
            if ruta_imagen:
                imagen = self.cargar_imagen(ruta_imagen, size=(80, 80))
                boton_cuadrado = tk.Button(self.frame_cuadrados, image=imagen, command=lambda r=ruta_imagen: seleccionar_cuadrado(r), borderwidth=0, relief=tk.GROOVE,fg='black',bg='black', width=80, height=80)
                boton_cuadrado.image = imagen
                boton_cuadrado.pack(side=tk.LEFT, padx=10, pady=10)

                # Almacenar el botón en el diccionario para actualizarlo más tarde
                self.botones_por_opcion[opcion] = boton_cuadrado



    def on_select(self, event):
        self.seleccion = self.combo.get()
        self.crear_menu_cuadrados(self.seleccion)



    def obtener_seleccion(self):
        return self.seleccion

    def guardar_selecciones(self):
        # Obtener las rutas seleccionadas y realizar la acción de guardar (puedes ajustar esta función según tus necesidades)
        rutas_seleccionadas = self.obtener_rutas_seleccionadas()
        #print("Rutas seleccionadas guardadas:")
        #for opcion, ruta in rutas_seleccionadas.items():
        #    print(f"{opcion}: {ruta}")
        self.ventana.destroy()
        
    def obtener_rutas_seleccionadas(self):
        return self.rutas_seleccionadas
if __name__=='__main__':
    app = CrearMenuDesplegable(None)  # Crear instancia de la clase
    app.ventana.mainloop()
