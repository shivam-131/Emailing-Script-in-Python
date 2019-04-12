import smtplib,ssl
port=465
print("Please enter the password:")
password = input()
senders= "guptashivam131@gmail.com"
recievers= "kushgpt99@gmail.com"
message = """ From: <guptashivamdausa@gmail.com>
To: <kushgpt99@gmail.com>
MIME-Version: 1.0
Content-type: text/html
Subject: Subtitle Auto-Synchroniser application

Mentors:
         Please select me for this summer project.
        -Shivam Gupta
         (180715)"""
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(senders,password)
    server.sendmail(senders, recievers,message)