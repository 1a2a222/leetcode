

from pymongo import  MongoClient

client = MongoClient()
collection = client["test"]["testmongo"]

data_list = [{"_id":i,"name":"py{}".format(i)} for i in range(1000)]
collection.insert_many(data_list)

ret = collection.find()
data_list = list(ret)
data_list = [i for i in data_list if i["_id"]%100==0 and i["_id"]]

import copy
l1 = [[1,2,3],4,5]
l2 = copy.deepcopy(l1)
l1[0][0]=110
print(l2)