##################### Extra Hard Starting Project ######################
import  smtplib
import pandas
import datetime as dt
import random
import os
from dotenv import load_dotenv, dotenv_values

load_dotenv()
# in order for this code  to run every day use python anywhere website.
my_email = os.getenv("my_email")
password = os.getenv("password")

today = dt.datetime.now()
today_tuple = (today.month,today.day)


# 1. Update the birthdays.csv
data = pandas.read_csv("birthdays.csv")
birthday_dict = {(data_row["month"],data_row["day"]): data_row for (index,data_row) in data.iterrows()}
if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    filepath = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(filepath) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]",birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=os.getenv("to_addrs"),
                            msg=f"subject:Happy birthday\n\n{contents}")
    #
# 2. Check if today matches a birthday in the birthdays.csv
# now = dt.datetime.now()
# today = now.today()
#
# if today == birthday:
#     print(now.date())
# else:
#     print(now.time())

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# with open("letter_templates/letter_1.txt") as  l1:
#     letter1 = l1.read()
# with open("letter_templates/letter_2.txt") as l2:
#     letter2 = l2.read()
# with open("letter_templates/letter_3.txt") as l3:
#     letter3 = l3.read()
#
# letters = letter1, letter2, letter3
# letter = random.choice(letters)
# print(letter)
# 4. Send the letter generated in step 3 to that person's email address.



