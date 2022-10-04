import random

from AgentClass import Agent
import json
from tools import *

ID = str(uuid.uuid1())

uuid = str(uuid.uuid1())
a = Agent(uuid, 'hhhhh', '123456')
a.dataFilling(force=random.randint(5, 10), memory=random.randint(10, 20), bandwitch=random.randint(10, 30))
a.register()
res = a.resourceFetch()
for i in res:
    print(i)
# a.data()
# res = a.unregister()
# print(res)
