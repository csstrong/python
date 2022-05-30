import time
import datetime
import json
from utils.db.BaseOperation import *

try:
    coll_base_equipment_info = client["db_wayeal_pipenet"]["base_equipment_info"]
    coll_data_minute = client["db_wayeal_pipenet"]["data_minute"]

    baseOperation = BaseOperation("habi")

    MINTIME = datetime.datetime(2022, 5, 29, 0, 0, 0)
    MAXTIME = datetime.datetime(2022, 5, 30, 23, 59, 59)
    # 时间戳 1653926399
    mintime_ts = int(time.mktime(MINTIME.timetuple()))
    maxtime_ts = int(time.mktime(MAXTIME.timetuple()))

    # 时间格式 2022-05-30 23:59:59
    t1 = datetime.datetime.fromtimestamp(mintime_ts)
    t2 = datetime.datetime.fromtimestamp(maxtime_ts)

    # 时间格式 '2022/03/20 00:00:00'
    startTime = t1.strftime("%Y/%m/%d %H:%M:%S")
    endTime = t2.strftime("%Y/%m/%d %H:%M:%S")

    # 需要设备id信息
    for equipData in coll_base_equipment_info.find():
        equipId = equipData["Id"]
        # print(equipId)

    equipId = "sb2022050601"

    # 获取设备监测的因子列表
    queryList = baseOperation.get_equip_factor(coll_base_equipment_info, equipId)
    factorArr = []
    for key in queryList:
        factorArr.append(key)

    # 获取配置的因子上下限值
    valRange = {}
    with open('default_value.json', 'r+') as f:
        defaultValue = json.load(f)
        valRange = defaultValue["value_range"]

    # 根据时间范围生成设备的假数据
    while startTime < endTime:
        nextTime = (datetime.datetime.strptime(startTime, "%Y/%m/%d %H:%M:%S") + datetime.timedelta(hours=1)).strftime(
            "%Y/%m/%d %H:%M:%S")

        item = baseOperation.generateItem(equipId, nextTime, factorArr, valRange)

        baseOperation.insert_item(coll_data_minute, item)

        startTime = nextTime

except Exception as e:
    print(e)
finally:
    client.close()
