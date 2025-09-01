import datetime as dt
import pandas as pd
import random

PLACEHOLDER = "[NAME]"


def send_birthday_email(body_text: str, to_email: str, name: str):
    import smtplib
    import ssl
    import base64
    from email.mime.text import MIMEText
    from google.oauth2.credentials import Credentials
    from google.auth.transport.requests import Request

    MY_EMAIL = "celmicratusca@gmail.com"
    SCOPES = ["https://mail.google.com/"]

    creds = Credentials.from_authorized_user_file("../token.json", SCOPES)
    if not creds.valid:
        if creds.refresh_token:
            creds.refresh(Request())
            with open("token.json", "w") as f:
                f.write(creds.to_json())
        else:
            raise RuntimeError(
                "Nu există refresh_token în token.json. Rulează get_token.py cu prompt='consent'.")

    subject = f"Happy Birthday, {name}! 🎉"
    msg = MIMEText(body_text, "plain", "utf-8")
    msg["From"] = MY_EMAIL
    msg["To"] = to_email
    msg["Subject"] = subject

    def xoauth2_str(user, token):
        return base64.b64encode(f"user={user}\1auth=Bearer {token}\1\1".encode()).decode()

    context = ssl.create_default_context()
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls(context=context)
        auth_string = xoauth2_str(MY_EMAIL, creds.token)
        code, resp = server.docmd("AUTH", "XOAUTH2 " + auth_string)
        if code != 235:
            raise Exception(f"AUTH failed: {code} {resp}")
        server.sendmail(MY_EMAIL, to_email, msg.as_string())
    print(f"Trimis către {to_email} ✅")


bdays_df = pd.read_csv("birthdays.csv")
bdays_dict = bdays_df.to_dict(orient="records")

now = dt.datetime.now()


for person in bdays_dict:
    if person["month"] == now.month and person["day"] == now.day:

        letter_index = random.randint(1, 3)
        with open(f"./letter_templates/letter_{letter_index}.txt") as letter_file:
            letter_contents = letter_file.read()

            updated_letter = letter_contents.replace(
                PLACEHOLDER, person["name"])
            print(updated_letter)
            send_birthday_email(
                updated_letter, person["email"], person["name"])
