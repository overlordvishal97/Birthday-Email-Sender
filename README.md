# Birthday-Email-Sender
This script sends a birthday email to individuals listed in a birthdays.csv file on their birthday.

# Features
Reads a birthdays.csv file to retrieve birthday information
Checks if today is a birthday and sends a personalized email if it is
Selects a random letter template from a directory to use for the email
Replaces the [NAME] placeholder with the person's actual name
Sends the email using Gmail's SMTP server

# Getting Started
Clone the repository or download the code.
Create a birthdays.csv file in the same directory as the script with the following columns:
name: the person's name
month: the person's birth month
day: the person's birth day
email: the person's email address
Replace my_email and password with your own Gmail credentials.
Create a letter_templates directory with at least one letter template file (e.g., letter_1.txt, letter_2.txt, etc.).
Run the script using Python (e.g., python script.py).

# Requirements
Python 3.x
smtplib library (built-in)
pandas library (install with pip install pandas)
datetime library (built-in)
random library (built-in)
Gmail account with SMTP access enabled

# Security Note
Make sure to keep your email credentials secure and do not share them with anyone.
Consider using a secure password storage method, such as environment variables or a secrets manager.
