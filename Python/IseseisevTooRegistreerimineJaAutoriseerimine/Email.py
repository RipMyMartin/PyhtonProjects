import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

smtp_server = "smtp.gmail.com"
port = 587
sender_email = "martinsild.mr@gmail.com"
receiver_email = "ripmyloven"
password = input("Введите пароль: ")

subject = "Martin SIld"
message = "Martin Sild"

context = ssl.create_default_context()

try:
    server = smtplib.SMTP(smtp_server, port)
    server.ehlo()
    server.starttls(context=context)
    server.ehlo()
    server.login(sender_email, password)

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))

    server.sendmail(sender_email, receiver_email, msg.as_string())

except Exception as e:
    print(e)
finally:
    server.quit()
