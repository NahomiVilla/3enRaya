import random
import string
from datetime import datetime, timedelta
import smtplib
from email.mime.text import MIMEText

class GeneradorContraseñas:

    def __init__(self, correo_emisor, contraseña_emisor, correo_destinatario):
        self.correo_emisor = correo_emisor
        self.contraseña_emisor = contraseña_emisor
        self.correo_destinatario = correo_destinatario

    def obtener_fecha_inicio(self):
        try:
            with open("fecha_inicio.txt", "r") as file:
                fecha_inicio_str = file.read()
                fecha_inicio = datetime.strptime(fecha_inicio_str, "%Y-%m-%d")
        except FileNotFoundError:
            fecha_inicio = datetime.now()
            with open("fecha_inicio.txt", "w") as file:
                file.write(fecha_inicio.strftime("%Y-%m-%d"))
        return fecha_inicio

    def guardar_fecha_inicio(self, fecha_inicio):
        with open("fecha_inicio.txt", "w") as file:
            file.write(fecha_inicio.strftime("%Y-%m-%d"))

    def generar_contraseña_mensual(self):
        fecha_inicio = self.obtener_fecha_inicio()
        fecha_actual = datetime.now()
        self.diferencia_meses = (fecha_actual.year - fecha_inicio.year) * 12 + fecha_actual.month - fecha_inicio.month

        if self.diferencia_meses >= 0:
            nueva_fecha_inicio = fecha_inicio + timedelta(days=fecha_actual.day - fecha_inicio.day)
            self.guardar_fecha_inicio(nueva_fecha_inicio)

            longitud_contraseña = 10
            caracteres = string.ascii_letters + string.digits + string.punctuation
            contraseña = ''.join(random.choice(caracteres) for _ in range(longitud_contraseña))

            return contraseña
        else:
            return None

    def enviar_correo_gmail(self, asunto, contraseña):
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587

        msg = MIMEText(contraseña)
        msg['Subject'] = asunto
        msg['From'] = self.correo_emisor
        msg['To'] = self.correo_destinatario

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(self.correo_emisor, self.contraseña_emisor)
            server.sendmail(self.correo_emisor, self.correo_destinatario, msg.as_string())

# Ejemplo de uso de la clase
#generador = GeneradorContraseñas(correo_emisor, 'daleikxdjjcgrhaw', 'nahomyvillag2@gmail.com')
#nueva_contraseña = generador.generar_contraseña_mensual()

#if nueva_contraseña:
#    generador.enviar_correo_gmail('Nueva Contraseña Mensual', nueva_contraseña)
