import requests
import smtplib
from email.mime.text import MIMEText
def send_simple_message(rec, title, message):
  	return requests.post(
  		"http://api.mailgun.net/v3/sandbox65968820fdb74c2eb550466716200637.mailgun.org/messages",
  		auth=("api", "308e91c9d526349190b7c6c93b3b6538"),
  		data={"from": "Excited User <mailgun@sandbox65968820fdb74c2eb550466716200637.mailgun.org>",
  			"to": [rec, "YOU@sandbox65968820fdb74c2eb550466716200637.mailgun.org"],
  			"subject": title,
  			"text": message})
   
   
print(send_simple_message("matin@gmail.com", "hello", "fsjkahfksjhdfsjkdf"))


def send_smtp_email(subject, message):
    msg = MIMEText(message)
    msg["Subject"] = subject
    msg["From"] = "postmaster@sandbox65968820fdb74c2eb550466716200637.mailgun.org"
    msg["To"] =  "msai.sadeghi@gmail.com"
    
    with smtplib.SMTP('smtp.mailgun.org', 587) as mail_server:
        mail_server.login('postmaster@sandbox65968820fdb74c2eb550466716200637.mailgun.org', '47b8a345528fd7326f226f3975fc6e6a-0920befd-e8854862')
        mail_server.sendmail(msg["From"],msg["to"], msg.as_string())
    
    
send_smtp_email("hello" ,"helllo blalallalalal")