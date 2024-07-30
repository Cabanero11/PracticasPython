# Simple mail transport protocol library
import smtplib


sender = 'drossitoversominecraft@gmail.com'
receiver = 'cabasito1111@gmail.com'
password = 'anime200064'
subject = 'Python email'
body = ' Uohhhhh'

# Se usan los """
mensaje_correo = f"""De: Feixiao{sender}
Para: Lingsha{receiver}
Asunto: {subject}\n
{body}
"""

# Puerto 587 para enviar mails
servidor = smtplib.SMTP('smtp.gmail.com', 587)
# Empezar protoclo TTLS de seguridad
servidor.starttls()


# Weno no funciona, por la seguridad de google xd
try:
    servidor.login(sender, password)
    print('Me logie')
    servidor.sendmail(sender, receiver, mensaje_correo)
    print('Email enviado')
except smtplib.SMTPAuthenticationError as e:
    print(f'Error: {e}')


