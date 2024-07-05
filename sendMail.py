import smtplib

# simple mail transfer protocol library
sender = "forjunk786@gmail.com"
receiver = "iqboy1200@gmail.com"
password = "Google@786"
subject = "No subject"
body = "I want to fuck you!"

# this is the email header"
message = f"""
    from: {sender}
    to: {receiver}
    subject = {subject}
    body: {body}
"""


server = smtplib.SMTP("SMTP.gmail.com", 587)
server.starttls()

try:

    server.login(sender, password)
    server.sendmail(sender, receiver, message)
except smtplib.SMTPAuthenticationError:
    print("You email cannot be sent")
