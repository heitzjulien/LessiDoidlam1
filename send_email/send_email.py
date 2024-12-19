import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from dotenv import load_dotenv

load_dotenv()

# Chemin du dossier actuel du script
current_dir = os.path.dirname(os.path.abspath(__file__))
# Creation du chemin absolu vers les fichiers
email_file_path = os.path.join(current_dir, "email.html")
filename_path = os.path.join(current_dir, "Facture_2024-INV-1547.pdf")
#Extraction du nom du fichier
filename = os.path.basename(filename_path)

# Lire le contenu du fichier email.html
with open(email_file_path, "r", encoding="utf-8") as file:
    body = file.read()

# Paramètres de l'email
sender_email = os.getenv('SENDER_MAIL_NAME')
receiver_email = os.getenv('RECEIVER_MAIL_NAME')
password = os.getenv('SENDER_MAIL_MDP')
subject = "Facture impayée - Urgent"

# Configuration du serveur SMTP
smtp_server = "smtp.gmail.com"
smtp_port = 587

# Création du message
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject
with open(filename_path, "rb") as file:
    payload = MIMEBase('application', "octet-stream")
    payload.set_payload(file.read())
encoders.encode_base64(payload)
payload.add_header('Content-Disposition', f"attachment; filename={filename}")
msg.attach(payload)

# Ajouter le corps du message
msg.attach(MIMEText(body, 'html'))

# Se connecter au serveur SMTP
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.login(sender_email, password)
        
# Convertir le message en chaîne de caractères et l'envoyer
text = msg.as_string()
server.sendmail(sender_email, receiver_email, text)
print("Email envoyé avec succès !")
