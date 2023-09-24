from croniter import croniter
from datetime import datetime
import send, time, os

starttime = time.time()

base = datetime.now()

iter = croniter('* * * * *', base)

nextTime = iter.get_next(datetime)
print(nextTime)

while True:
    if datetime.now() > nextTime:
        nextTime = iter.get_next(datetime)
        print(nextTime)

# def job():
#     global starttime
#     starttime = time.time()

#     send.send("smtp.gmail.com", 587, os.environ.get("EMAIL_HOST_USER"), os.environ.get("EMAIL_HOST_PASSWORD"), "hi", [os.environ.get("EMAIL_HOST_USER")], "test")
    



# starttime = time.time()
# while True:
#     print(f"{time.time() - starttime: .2f}", end="\r")