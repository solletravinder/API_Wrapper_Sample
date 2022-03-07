
import json
from TODO_API.apiWrapper import ApiWrapper

data_id = 10



AW = ApiWrapper()


print(AW.get_list_data())
print(AW.get_particular_data(data_id))

print(AW)