import random
import datetime
import time

MINTIME = datetime.datetime(2022, 4, 1, 0, 0, 0)
MAXTIME = datetime.datetime(2022, 4, 15, 23, 59, 59)

mintime_ts = int(time.mktime(MINTIME.timetuple()))
maxtime_ts = int(time.mktime(MAXTIME.timetuple()))

for RECORD in range(10):
    random_ts = random.randint(mintime_ts, maxtime_ts)
    RANDOMTIME = datetime.datetime.fromtimestamp(random_ts)
    t = RANDOMTIME.strftime("%Y/%m/%d %H:%M:%S")
    t2 = (datetime.datetime.strptime(t, "%Y/%m/%d %H:%M:%S") + datetime.timedelta(hours=1)).strftime("%Y/%m/%d %H:%M:%S")
    print(t[:-5] + '00:00')
    print(t2[:-5] + '00:00')
