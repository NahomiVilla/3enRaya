
import time
import threading
class Cronometro:
    def __init__(self, tiempo_limite_segundos):
        self.tiempo_limite = tiempo_limite_segundos
        self.inicio = time.time() - self.cargar_tiempo()
        self.tiempo_transcurrido = 0

    def guardar_tiempo(self, tiempo):
        with open("tiempo_guardado.txt", "w") as archivo:
            archivo.write(str(tiempo))

    def cargar_tiempo(self):
        try:
            with open("tiempo_guardado.txt", "r") as archivo:
                tiempo_guardado = float(archivo.read())
            return tiempo_guardado
        except FileNotFoundError:
            return 0
    def iniciar_cronometro(self):
        # Crear un hilo para ejecutar la función en segundo plano
        cronometro_thread = threading.Thread(target=self._iniciar_cronometro_thread)
        cronometro_thread.start()
    def _iniciar_cronometro_thread(self):
        #print("Cronómetro iniciado. Presiona Ctrl+C para salir.")

        
        while self.tiempo_transcurrido < self.tiempo_limite:
            self.tiempo_transcurrido = time.time() - self.inicio
            self.minutos, segundos = divmod(self.tiempo_transcurrido, 60)
            self.tiempo_restante = self.tiempo_limite - self.tiempo_transcurrido

            # Formatear el tiempo en minutos y segundos
            tiempo_formateado = "{:02}:{:02}".format(int(self.minutos), int(segundos))

            # Imprimir el tiempo transcurrido y el tiempo restante
            print(f"Tiempo transcurrido: {tiempo_formateado} | Tiempo restante: {self.tiempo_restante:.2f} segundos", end="\r")

            # Dormir durante un segundo antes de la próxima actualización
            time.sleep(1)

            # Guardar el tiempo transcurrido en un archivo
            self.guardar_tiempo(self.tiempo_transcurrido)

    def reiniciar_cronometro(self):
        # Reiniciar el cronómetro
        self.inicio = time.time()
        self.tiempo_transcurrido = 0

