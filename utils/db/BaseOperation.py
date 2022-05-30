from pymongo import MongoClient
import random

client = MongoClient(host="mongodb://admin:wayee_soft_123@192.168.200.105:27017")


class BaseOperation:

    def __init__(self, name):
        self.name = name

    def print(self):
        print(self.name)

    # 在数据表中插入单条数据
    def insert_item(self, collection, item):

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
    def get_equip_factor(self, collection, equipId):
        query = {"Id": equipId}

        cursor = collection.find(query)
        queryArr = []

        for doc in cursor:
            # print(doc)
            queryArr.append(doc)
        # 取第一个设备
        equipInfo = queryArr[0]
        fieldFactor = equipInfo["Factor"]
        return fieldFactor

    # 生成因子数据
    def generateItem(self, equipId, time, factorArr, valRange):
        tempJson = {"VerifyDate": time, "IsVerify": True, "DataTime": time}

        for code in factorArr:
            minV = 0
            maxV = 0
            for key in valRange:
                if key == code:
                    minV = valRange[key]["min"]
                    maxV = valRange[key]["max"]
            # 生成随机数
            r_num = random.randint(minV, maxV) + random.random()
            tempJson[code] = ('%.2f' % r_num)
            index = code.index('-Avg')
            code_Flag = code[:index] + '-Flag'
            tempJson[code_Flag] = 'N'

        item = {'Id': equipId, 'Type': '', 'MonitorTime': time, 'StroageTime': time, 'Ip': '', "ComponentVal": tempJson}
        return item
