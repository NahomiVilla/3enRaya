import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk
import os 
import sys

from MenuDesplegable import *
from cronometro import Cronometro
from contraseña import GeneradorContraseñas

class TresEnRaya:
    def __init__(self, root):
        self.root = root
        self.jugador = "X"
        self.buttons = [[None, None, None] for _ in range(3)]
        self.root.attributes('-fullscreen', True)

        # Crear fondo
        self.script_dir = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        self.background_image = tk.PhotoImage(file=os.path.join(self.script_dir, "imagenes-img\\fondo_rayas.png"))
        self.background_label = tk.Label(root, image=self.background_image)
        self.background_label.place(relwidth=1, relheight=1)
        #imagenes
        self.x_image=''
        self.o_image=''
        self.G_image=''

        # Colocar el botón "Iniciar Juego" en el fondo
        self.iniciar_button = tk.Button(self.background_label, text="Iniciar Juego", command=self.confirmacion_cambio_imagen,font=("Helvetica", 24), width=15, height=3)
        self.iniciar_button.place(relx=0.5, rely=0.5, anchor="center")
        
        self.cronometro=Cronometro(60)#5minutos
    def seleccion_imagen(self):
        self.ventana_confirmacion_cambio.destroy()
        self.menu_desplegable=CrearMenuDesplegable(self.background_label)

        self.menu_desplegable_frame=tk.Frame(self.background_label,bg='')
        self.menu_desplegable_frame.place(relx=0.5, rely=0.5, anchor="center")
        #esperar a que se cierren las ventanas para seguir con el codigo
        self.root.wait_window(self.menu_desplegable.ventana)
        #imagenes 
        self.rutas=self.menu_desplegable.obtener_rutas_seleccionadas()
        if self.rutas['Cruz']is not None:
            self.x_image=ImageTk.PhotoImage(file=os.path.join(self.script_dir,self.rutas['Cruz']))
        else:
            self.x_image=ImageTk.PhotoImage(file=os.path.join(self.script_dir,"imagenes-img\\cruz_200.png"))
        if self.rutas['Circulo']is not None:
            self.o_image=ImageTk.PhotoImage(file=os.path.join(self.script_dir,self.rutas['Circulo']))
        else:
            self.o_image = ImageTk.PhotoImage(file=os.path.join(self.script_dir, "imagenes-img\\circulo_200_2.png"))
        if self.rutas['Imagen de Ganador']is not None:
            self.G_image=ImageTk.PhotoImage(file=os.path.join(self.script_dir,self.rutas['Imagen de Ganador']))
        else:
            self.G_image=ImageTk.PhotoImage(file=os.path.join(self.script_dir,"imagenes-img\\ganador1.png"))
        self.iniciar_juego()
    def funcion_boton_no(self):
        self.ventana_confirmacion_cambio.destroy()
        self.x_image=ImageTk.PhotoImage(file=os.path.join(self.script_dir,"imagenes-img\\cruz_200.png"))
        self.o_image = ImageTk.PhotoImage(file=os.path.join(self.script_dir, "imagenes-img\\circulo_200_2.png"))
        self.G_image=ImageTk.PhotoImage(file=os.path.join(self.script_dir,"imagenes-img\\ganador1.png"))
        self.iniciar_juego()
    #ventana de si quiere cambiar las imagenes
    def confirmacion_cambio_imagen(self):
        
        self.ventana_confirmacion_cambio=tk.Toplevel(self.root)
        ancho_ventana = 300
        alto_ventana = 150
        x_ventana = (self.root.winfo_screenwidth() - ancho_ventana) // 2
        y_ventana = (self.root.winfo_screenheight() - alto_ventana) // 2
        self.ventana_confirmacion_cambio.geometry(f"{ancho_ventana}x{alto_ventana}+{x_ventana}+{y_ventana}")
        button_frame_si_no = tk.Frame(self.ventana_confirmacion_cambio, bg='') 
        button_frame_si_no.pack(side=tk.BOTTOM, padx=8)
        button_si = tk.Button(button_frame_si_no, text="Si", command=self.seleccion_imagen,font=("Helvetica", 12), width=15, height=5)
        button_si.pack(side=tk.LEFT,padx=5, pady=5) 
        button_no = tk.Button(button_frame_si_no, text="No", command=self.funcion_boton_no,font=("Helvetica", 12), width=15, height=5)
        button_no.pack(side=tk.LEFT,padx=5, pady=5) 
   

    #se inicia el juego y se pide contraseña    
    def iniciar_juego(self):
        #self.cronometro.reiniciar_cronometro()
        self.cronometro.iniciar_cronometro()
        if self.cronometro.tiempo_transcurrido < self.cronometro.tiempo_limite:
            if 0 <= self.cronometro.tiempo_transcurrido <= 5:
                self.pedir_contraseña()
            elif 5<self.cronometro.tiempo_transcurrido < self.cronometro.tiempo_limite:
                self.ventana_confirmacion_cambio.destroy()
                self.inicializar_juego()
        else:# Si llegamos aquí, el tiempo límite se alcanzó
            self.pedir_contraseña()
                

     
    def pedir_contraseña(self):
        self.ventana_confirmacion_cambio.destroy()
        self.generador=GeneradorContraseñas('nahomyvillag7@gmail.com', 'daleikxdjjcgrhaw', 'nahomyvillag2@gmail.com')
        self.contraseña_generada=self.generador.generar_contraseña_mensual()
        if self.contraseña_generada:
            self.generador.enviar_correo_gmail('Nueva Contraseña Mensual', self.contraseña_generada)
        # Crear una ventana secundaria para solicitar la contraseña
        self.ventana_contraseña = tk.Toplevel(self.background_label)
        ancho_ventana = 300
        alto_ventana = 150
        x_ventana = (self.root.winfo_screenwidth() - ancho_ventana) // 2
        y_ventana = (self.root.winfo_screenheight() - alto_ventana) // 2
        self.ventana_contraseña.geometry(f"{ancho_ventana}x{alto_ventana}+{x_ventana}+{y_ventana}")

        # Solicitar la contraseña al usuario
        self.contraseña_entry = tk.Entry(self.ventana_contraseña, show="*", font=("Helvetica", 16))
        self.contraseña_entry.pack(pady=15)

        # Botón para verificar la contraseña
        verificar_button = tk.Button(self.ventana_contraseña, text="Verificar Contraseña", command=self.verificar_contraseña,font=("Helvetica", 12), width=15, height=5)
        verificar_button.pack()
        #boton enter
        self.ventana_contraseña.bind("<Return>", lambda event: self.verificar_contraseña())

    #verificacion de contraseña
    def verificar_contraseña(self):
        # Verificar la contraseña
        contraseña_ingresada = self.contraseña_entry.get()
        if contraseña_ingresada == self.contraseña_generada: 
            # Cerrar la ventana de contraseña
            self.ventana_contraseña.destroy()
            # Inicializar el juego después de verificar la contraseña
            self.cronometro.reiniciar_cronometro()
            self.inicializar_juego()
            self.cronometro.iniciar_cronometro()
        else:
            messagebox.showerror("Error", "Contraseña incorrecta. Inténtelo nuevamente.")
    
    #inicio de juego
    def inicializar_juego(self):
        #frame de botones para centrar
        button_frame = tk.Frame(self.background_label, bg='')
        button_frame.place(relx=0.5, rely=0.5, anchor="center")
        #crear botones
        for i in range(3):
            for j in range(3):
                button_color = "black"
                padx_value=32
                pady_value=42
                self.buttons[i][j] = tk.Button(button_frame, text="", font=("Helvetica", 32), borderwidth=0,relief=tk.GROOVE, width=10, height=4, bg=button_color, fg="black",highlightbackground='black',highlightcolor='black',bd=0, command=lambda i=i, j=j: self.hacer_movimiento(i, j))
                self.buttons[i][j].grid(row=i, column=j, padx=(padx_value, padx_value), pady=(pady_value,pady_value), sticky="nsew")

        for i in range(3):
            button_frame.grid_rowconfigure(i, weight=1, uniform="group1")
            button_frame.grid_columnconfigure(i, weight=1, uniform="group1")
        self.tablero = [["" for _ in range(3)] for _ in range(3)]
        self.root.bind("<Escape>", self.exit_fullscreen)
        self.root.bind("<space>", self.reiniciar_juego)
        

    def exit_fullscreen(self,event):
        # Salir del modo fullscreen al presionar Escape
        self.root.attributes("-fullscreen", False)
        self.root.destroy() 
    def hacer_movimiento(self, row,col):
        if self.cronometro.tiempo_transcurrido<self.cronometro.tiempo_limite and self.generador.diferencia_meses<1:
            if self.tablero[row][col] == "" and not self.verificar_ganador():
                self.tablero[row][col] = self.jugador
                if self.jugador=='X':
                    self.buttons[row][col].config(image=self.x_image)
                else:
                    self.buttons[row][col].config(image=self.o_image)
        
                self.buttons[row][col].config(text=self.jugador, state=tk.DISABLED)


                if self.verificar_ganador():
                    # Mostrar la imagen de ganador en lugar de la messagebox
                    ganador_label = tk.Label(self.background_label, image=self.G_image,bg='black')
                    ganador_label.place(relx=0.5, rely=0.5, anchor="center")
                    self.root.update()
                    self.root.after(2000, ganador_label.destroy) 
                elif sum(row.count('') for row in self.tablero) == 0:
                    messagebox.showinfo("Fin del juego", "Empate")
                else:
                    self.jugador = "O" if self.jugador == "X" else "X"
        else:
            self.buttons[row][col].config(text='', state=tk.DISABLED)
            self.pedir_contraseña()
    def verificar_ganador(self):
        # Verificar si hay un ganador en la fila, columna o diagonal
        for i in range(3):
            if self.check_row(i) or self.check_column(i):
                return True

        return self.check_diagonal() or self.check_antidiagonal()


    def check_row(self,row):
        return all(self.tablero[row][i] == self.jugador for i in range(3))
    def check_column(self, col):
        return all(self.tablero[i][col] == self.jugador for i in range(3))
    def check_diagonal(self):
        return all(self.tablero[i][i] == self.jugador for i in range(3))

    def check_antidiagonal(self):
        return all(self.tablero[i][2 - i] == self.jugador for i in range(3))
    def reiniciar_juego(self, event=None):
        # Lógica para reiniciar el juego
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(image="", text="", state=tk.NORMAL)
                self.tablero[i][j] = ""
        self.jugador = "X"

def main():
    root = tk.Tk()
    tres_en_raya = TresEnRaya(root)
    root.mainloop()

if __name__ == '__main__':
    main()
