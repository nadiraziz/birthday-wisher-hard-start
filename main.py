import smtplib
import datetime as dt
import pandas
import random
now = dt.datetime.now()
today_tuple = (now.month, now.day)
my_email = "nadirtest7@gmail.com"
password = "Nadir@123"

data = pandas.read_csv("birthdays.csv")
birthday_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}
print(birthday_dict)

if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        content = letter_file.read()
        letter = content.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="nadiraziziyah@gmail.com",
            msg=f"Subject: Birthday Wish\n\n{letter}"
        )