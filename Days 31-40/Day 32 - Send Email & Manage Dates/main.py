# -------------------- OUT OF DATE METHOD ----------------------#
# import smtplib

# my_email = "celmicratusca@gmail.com"
# my_password = "SIXTEENLETTERCOD"
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=my_password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="antoniastanila411@yahoo.com",
#                         msg="Subject: Hello\n\n This is the body of my email.")


import os
import smtplib
import ssl
import base64
import random
import datetime as dt
from email.mime.text import MIMEText
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request


# Selecting Random Motivational Quote


def get_random_quote():
    with open("quotes.txt") as data_file:
        quotes_list = data_file.readlines()
        quotes_list = [quote.strip() for quote in quotes_list]

    quote_of_the_week = random.choice(quotes_list)
    return quote_of_the_week


# Emails
MY_EMAIL = "celmicratusca@gmail.com"
TO_EMAIL = "antoniastanila411@yahoo.com"
SUBJECT = "Your weekly motivation :D"
BODY = get_random_quote()

# Scopes for Gmail API
SCOPES = ["https://mail.google.com/"]


def xoauth2_str(user, token):
    return base64.b64encode(
        f"user={user}\1auth=Bearer {token}\1\1".encode()
    ).decode()


# Load the token from file (generated with get_token.py)
creds = Credentials.from_authorized_user_file("token.json", SCOPES)


if not creds.valid:
    if creds.refresh_token:
        creds.refresh(Request())
        with open("token.json", "w") as f:
            f.write(creds.to_json())
    else:
        raise RuntimeError(
            "Nu există refresh_token în token.json. Rulează din nou get_token.py cu prompt='consent'."
        )
# Creating the message
msg = MIMEText(BODY)
msg["From"] = MY_EMAIL
msg["To"] = TO_EMAIL
msg["Subject"] = SUBJECT

now = dt.datetime.now()

# Connecting to SMTP Gmail
if now.weekday() == 0:
    context = ssl.create_default_context()
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls(context=context)
        auth_string = xoauth2_str(MY_EMAIL, creds.token)
        code, response = server.docmd("AUTH", "XOAUTH2 " + auth_string)
        if code != 235:
            raise Exception(f"AUTH failed: {code} {response}")
        server.sendmail(MY_EMAIL, TO_EMAIL, msg.as_string())

    print("Email sent succesfully ✅")
