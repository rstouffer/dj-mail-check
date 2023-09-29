from croniter import croniter
from datetime import datetime
import send, time, os
import mariadb
import sys
from dotenv import load_dotenv

load_dotenv()

def getConn():
    try:
        return mariadb.connect(
            user=os.environ.get("DB_USERNAME"),
            password=os.environ.get("DB_PASSWORD"),
            host=os.environ.get("DB_HOST"),
            port=int(os.environ.get("DB_PORT")),
            database=os.environ.get("DB_DATABASE")
        )
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)

#set the next time to max
nextTime = datetime(2999,12,31,23,59,59)
#Tasks to run at next time
ttrant = []
def getTasks():
    global nextTime
    global ttrant 
    global conn

    #set the next time to max

    conn = getConn()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM cron')

    nextTime = datetime(2999,12,31,23,59,59)

    for row in cursor:
    
        cron = croniter(row[1], datetime.now())
        print('NOW ', datetime.now())
        print(row[1])
        testTime = cron.get_next(datetime)
        print('TestTime', testTime)
        if (testTime < nextTime):
            print(testTime, 'newer than', nextTime)
            nextTime = testTime
            ttrant = []
            ttrant.append(row)
        elif (testTime == nextTime):
            print('found same', nextTime)
            ttrant.append(row)
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
