
import time
import smtplib
from email.message import EmailMessage

def envoyer_email():
    msg = EmailMessage()
    msg.set_content('Un créneau est disponible !')
    msg['Subject'] = 'Alerte rendez-vous VFS'
    msg['From'] = 'tonemail@example.com'
    msg['To'] = 'destination@example.com'

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login('tonemail@example.com', 'ton_mot_de_passe')
        server.send_message(msg)

while True:
    print("Je vérifie... (simulation)")
    # Ici tu mettras plus tard le code pour vérifier VFS
    time.sleep(60)  # Vérifie toutes les minutes
