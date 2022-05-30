from utils.db.BaseOperation import *

collection = client["db_wayeal_pipenet"]["base_equipment_info"]

baseOperation = BaseOperation("habi")

queryList = baseOperation.get_equip_factor(collection, "sb2022050601")

factorArr = []
for key in queryList:
    factorArr.append(key)

print(factorArr)

with open('default_value.json', 'r+') as f:
    defaultValue = json.load(f)
    val_range = defaultValue["value_range"]
    for key in val_range:
        print(val_range[key]["min"])
        print(val_range[key]["max"])
