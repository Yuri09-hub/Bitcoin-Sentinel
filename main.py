import time
import schedule
from web_scraper import Alert

print("Enter the email address where you want to receive the notification.")
email = str(input("Email: "))

schedule.every(10).seconds.do(Alert,email)

while True:
    schedule.run_pending()
    time.sleep(1)