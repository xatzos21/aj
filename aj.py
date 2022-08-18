import os
import time
import datetime
import smtplib #
from email.mime.multipart import* #
from email.mime.text import* #
from email.message import * #
from colorama import *
from art import *

# initializing colorama
init()

#email function
# def gmail_send(subject, message, from_mail, to_mail, password):  
#     global link
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.starttls()
#     server.login(from_mail, password)
#     msg            = EmailMessage()
#     message        = f'{message}'
#     msg.set_content(message)
#     msg['Subject'] = subject
#     msg['From']    = from_mail
#     msg['To']      = to_mail
#     server.send_message(msg)

new_entry = input("ENTER DIARY ENTRY HERE >>>")

now = datetime.datetime.today().strftime("%H:%M:%S %d-%m-%Y")

with open("copy.text", "a") as file:
    file.write(now + " " + new_entry + "\n")
