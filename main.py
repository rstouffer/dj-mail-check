from croniter import croniter
from datetime import datetime
import send, time, os

cts = ['* * * * *', '*/2 * * * *']

iters = []
nextTimes = []

for ct in cts:
    iters.append(croniter(ct, datetime.now()))
    nextTimes.append(iters[-1].get_next(datetime))

while True:
    for i in range(len(nextTimes)):
        if datetime.now() > nextTimes[i]:
            nextTimes[i] = iters[i].get_next(datetime)
            print(nextTimes[i])


# def job():
#     global starttime
#     starttime = time.time()

#     send.send("smtp.gmail.com", 587, os.environ.get("EMAIL_HOST_USER"), os.environ.get("EMAIL_HOST_PASSWORD"), "hi", [os.environ.get("EMAIL_HOST_USER")], "test")
    



# starttime = time.time()
# while True:
#     print(f"{time.time() - starttime: .2f}", end="\r")