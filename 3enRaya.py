import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk, ImageSequence

import os
import sys


class TresEnRaya:
    def __init__(self, root):
        self.root = root
        self.root.title("Tres en Raya")
        self.jugador = "X"
        self.buttons = [[None, None, None] for _ in range(3)]
        self.root.attributes('-fullscreen', True)

        script_dir = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        self.background_image = tk.PhotoImage(file=os.path.join(script_dir, "imagenes\\fondo_rayas.png"))
        self.background_label = tk.Label(root, image=self.background_image)
        self.background_label.place(relwidth=1, relheight=1)

        button_frame = tk.Frame(self.background_label, bg='')
        button_frame.place(relx=0.5, rely=0.5, anchor="center")

        self.gif_cruz = self.load_gif(os.path.join(script_dir, "imagenes\\cruz.gif"))
        self.gif_circulo = self.load_gif(os.path.join(script_dir, "imagenes\\circulo.gif"))

        for i in range(3):
            for j in range(3):
                button_color = "black"
                padx_value = 32
                pady_value = 42
                self.buttons[i][j] = tk.Button(button_frame, text="", font=("Helvetica", 32), borderwidth=0,
                                               relief=tk.GROOVE, width=10, height=4, bg=button_color, fg="black",
                                               command=lambda i=i, j=j: self.hacer_movimiento(i, j))
                self.buttons[i][j].grid(row=i, column=j, padx=(padx_value, padx_value), pady=(pady_value, pady_value),
                                        sticky="nsew")

        for i in range(3):
            button_frame.grid_rowconfigure(i, weight=1, uniform="group1")
            button_frame.grid_columnconfigure(i, weight=1, uniform="group1")

        self.tablero = [["" for _ in range(3)] for _ in range(3)]
        self.root.bind("<Escape>", self.exit_fullscreen)
        self.root.bind("<space>", self.reiniciar_juego)

    def exit_fullscreen(self, event):
        self.root.attributes("-fullscreen", False)
        self.root.destroy()

    def hacer_movimiento(self, row, col):
        if self.tablero[row][col] == "" and not self.verificar_ganador():
            self.tablero[row][col] = self.jugador

            if self.jugador == 'X':
                self.show_gif(self.gif_cruz, row, col)
            else:
                self.show_gif(self.gif_circulo, row, col)

            if self.verificar_ganador():
                messagebox.showinfo("Fin del juego", f"Ganador: Jugador {self.jugador}")
            elif sum(row.count('') for row in self.tablero) == 0:
                messagebox.showinfo("Fin del juego", "Empate")
            else:
                self.root.after(800, lambda: setattr(self, 'jugador', "O" if self.jugador == "X" else "X"))

    
    def show_gif(self, frames, row, col, index=0):
        if index < len(frames):
            self.buttons[row][col].config(image=frames[index])
            self.root.after(20, lambda: self.show_gif(frames, row, col, index + 1))
        else:
            # También actualiza el tablero con el nuevo jugador
            self.tablero[row][col] = self.jugador
    def verificar_ganador(self):
        for i in range(3):
            if self.check_row(i) or self.check_column(i):
                return True

        return self.check_diagonal() or self.check_antidiagonal()

    def check_row(self, row):
        return all(self.tablero[row][i] == self.jugador for i in range(3))

    def check_column(self, col):
        return all(self.tablero[i][col] == self.jugador for i in range(3))

    def check_diagonal(self):
        return all(self.tablero[i][i] == self.jugador for i in range(3))

    def check_antidiagonal(self):
        return all(self.tablero[i][2 - i] == self.jugador for i in range(3))

    def reiniciar_juego(self, event=None):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(image="", text="", state=tk.NORMAL)
                self.tablero[i][j] = ""
        self.jugador = "X"
    def load_gif(self, file_path):
        gif = Image.open(file_path)
        frames = []

        try:
            while True:
                current_frame = gif.tell()
                frames.append(ImageTk.PhotoImage(gif.crop((0, 0, gif.width, gif.height))))
                gif.seek(current_frame + 1)
        except EOFError:
            pass

        return frames




def main():
    root = tk.Tk()
    tres_en_raya = TresEnRaya(root)
    root.mainloop()

if __name__ == '__main__':
    main()
