import schedule
import time

from db.antitoken import remove_old_tokens

schedule.every(1).hour.do(remove_old_tokens())

while True:
    schedule.run_pending()
    time.sleep(1)