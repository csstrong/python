from pymongo import MongoClient
import random
import time
import datetime

client = MongoClient(host="mongodb://admin:wayee_soft_123@192.168.200.105:27017")
collection = client["db_wayeal_pipenet"]["data_hour"]


class GenerateMongodbData:

    def __init__(self, name):
        self.name = name

    def print(self):
        print(self.name)

    # 在数据表中插入单条数据
    def process_item(self, item):

        # count = collection.count_documents(item)
        itemId = item["Id"]
        itemMonitorTime = item["MonitorTime"]
        isExists = collection.find_one({"Id": itemId, "MonitorTime": itemMonitorTime})

        if (not isExists):
            print(item)
            collection.insert_one(item)
        else:
            print("This data has exists!")
        return item

    # 获得设备的因子列表
    def get_equip_factor(self,equipId):
        query={}
        query["Id"]=equipId

        cursor=collection.find(query)
        try:
            for doc in cursor:
                print(doc)
        finally:
            client.close()


gen = GenerateMongodbData("habi")

MINTIME = datetime.datetime(2022, 3, 20, 0, 0, 0)
MAXTIME = datetime.datetime(2022, 5, 30, 23, 59, 59)
mintime_ts = int(time.mktime(MINTIME.timetuple()))
maxtime_ts = int(time.mktime(MAXTIME.timetuple()))


# 循环生成数据
for i in range(1000):
    random_ts = random.randint(mintime_ts, maxtime_ts)
    RANDOMTIME = datetime.datetime.fromtimestamp(random_ts)
    t = RANDOMTIME.strftime("%Y/%m/%d %H:%M:%S")
    t2 = (datetime.datetime.strptime(t, "%Y/%m/%d %H:%M:%S") + datetime.timedelta(hours=1)).strftime(
        "%Y/%m/%d %H:%M:%S")
    t_val = t[:-5] + '00:00'
    t2_val = t2[:-5] + '00:00'

    # 生成随机数
    r_num = random.randint(1, 99) / 10
    r_num2 = random.randint(1, 99) / 10
    r_num3 = random.randint(1, 99) / 10
    item = {
        'Id': 'sb2022050601',
        'Type': '',
        'MonitorTime': t_val,
        'StroageTime': t2_val,
        'Ip': '',
        "ComponentVal": {
            "VerifyDate": t2_val,
            "IsVerify": True,
            "DataTime": t_val,
            "w-liuliang-Flag": "N",
            "w-liuliang-Avg": str(1.1111 + round(r_num * r_num2, 5)),
            "w-liusu-Flag": "N",
            "w-liusu-Avg": str(2.2222 + round(r_num2 * r_num3, 5)),
            "w-shuiwei-Flag": "N",
            "w-shuiwei-Avg": str(3.3333 + round(r_num3 * r_num, 5))
        }
    };

    # gen.process_item(item)

