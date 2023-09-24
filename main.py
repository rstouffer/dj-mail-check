from croniter import croniter
from datetime import datetime
import send, time, os

cts = [
        ['* * * * *','task1'], 
        ['* * * * *','task2'], 
        ['* * * * *','task3'], 
        ['* * * * *','task4'], 
        ['* * * * *','task5'], 
        ['* * * * *','task6'], 
        ['* * * * *','task7'], 
        ['*/2 * * * *','task8']
]

#set the next time to max
nextTime = datetime(2999,12,31,23,59,59)
#Tasks to run at next time
ttrant = []
def getTasks():
    global nextTime
    global ttrant 
    #set the next time to max
    nextTime = datetime(2999,12,31,23,59,59)
    for ct in cts:

        cron = croniter(ct[0], datetime.now())
        testTime = cron.get_next(datetime)

        if (testTime < nextTime):
            print('found newer time', nextTime)
            nextTime = testTime
            ttrant = []
            ttrant.append(ct)
        elif (testTime == nextTime):
            print('found same', nextTime)
            ttrant.append(ct)
#init tasks
getTasks()

while True:
    if nextTime <= datetime.now():
        for ct in ttrant:
            print(ct)
        getTasks()
        


# def job():
#     global starttime
#     starttime = time.time()

#     send.send("smtp.gmail.com", 587, os.environ.get("EMAIL_HOST_USER"), os.environ.get("EMAIL_HOST_PASSWORD"), "hi", [os.environ.get("EMAIL_HOST_USER")], "test")
    



# starttime = time.time()
# while True:
#     print(f"{time.time() - starttime: .2f}", end="\r")
