import pandas as pd
import random as rnd
import datetime as dt
import smtplib
from email.message import EmailMessage
import os

MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

##################### Extra Hard Starting Project ######################
# 1. Update the birthdays.csv
# noinspection argument-list
bday_file = pd.read_csv('birthdays.csv')
bdays_df = bday_file.to_dict(orient='records')

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
this_month = now.month
today = now.day
birthday_boys_and_girls = [{person["name"]:person["email"]} for person in bdays_df if person["day"] == today and person["month"] == this_month]

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
for person in birthday_boys_and_girls:
	for name, email in person.items():
		split_name = name.split()
		first_name = split_name[0]
		with open(f"letter_templates/letter_{rnd.randint(1, 3)}.txt") as letter_file:
			bday_letter = letter_file.read()
			bday_letter = bday_letter.replace("[NAME]", first_name)
			bday_letter = bday_letter.replace("Angela", "DannyDanX")

	# 4. Send the letter generated in step 3 to that person's email address.
		msg = EmailMessage()
		msg.set_content(bday_letter)
		msg["Subject"] = "Happy Birthday!"
		msg["From"] = MY_EMAIL
		msg["To"] = email
		with smtplib.SMTP('smtp.gmail.com', 587) as connection:
			connection.starttls()
			connection.login(user=MY_EMAIL, password=MY_PASSWORD)
			connection.send_message(msg)
			# connection.sendmail(from_addr=MY_EMAIL,to_addrs=email,msg=f"Subject: Happy Birthday!\n\n{bday_letter}")
