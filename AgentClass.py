import asyncio
import json
import random

import websockets
import configuration as cf
from AgentMsgProcessor import AgentMsgProcessor


class Agent:
    def __init__(self, ID, user, password):
        self.__token = ID
        self.__userName = user
        self.__password = password
        self.__data = {
            'Node_token': ID,
            'CalculateForce': 0,
            'Memory': 0,
            'Bandwidth': 0
        }
        self.__res = None

    def data(self):
        print(self.__data)

    def userInfo(self):
        print({
            'user': self.__userName,
            'password': self.__password
        })

    def dataFilling(self, force=0, memory=0, bandwitch=0):
        self.__data['CalculateForce'] = force
        self.__data['Memory'] = memory
        self.__data['Bandwidth'] = bandwitch

    async def __runCase(self, jsonMsg, websocket):
        pr = AgentMsgProcessor()
        return await pr.run(jsonMsg, self.__response, websocket)

    # 发消息给服务器的回调函数
    async def __response(self, msg, websocket=None):
        await self.__sendMsg(msg, websocket)

    # 发送消息
    async def __sendMsg(self, msg, websocket):
        await websocket.send(msg)
        # 避免被卡线程
        await asyncio.sleep(0.2)

    async def __communicate(self, pkg):
        async with websockets.connect(cf.socket_address) as websocket:
            await websocket.send(pkg)
            while True:
                try:
                    resp = await websocket.recv()
                    choice, re = await self.__runCase(resp, websocket)
                    if choice == "break":
                        break
                    self.__res = re
                except websockets.ConnectionClosed:
                    print("ConnectionClosed...")  # 链接断开
                    break
                except websockets.InvalidState:
                    print("InvalidState...")  # 无效状态
                    break
                except Exception as e:
                    print(e)
                    break

    def register(self):
        if self.__data['Node_token'] == "":
            print("The data isn't filled!")
            return
        pkg = {
            'CMD': cf.regis,
            'Data': self.__data
        }
        print(pkg)
        pkg = json.dumps(pkg)
        asyncio.run(self.__communicate(pkg))
        return self.__res

    def unregister(self):
        pkg = {
            'CMD': cf.delete,
            'Data': self.__token
        }
        pkg = json.dumps(pkg)
        asyncio.run(self.__communicate(pkg))
        return self.__res

    def resourceFetch(self):
        pkg = {
            'CMD': cf.select,
            'Data': {
                'user': self.__userName,
                'pwd': self.__password,
                'type': 'all'
            }
        }
        pkg = json.dumps(pkg)
        asyncio.run(self.__communicate(pkg))
        return self.__res

    def task_submit(self, name, delay, jit, rate):
        cal_amount = random.randint(1, 10)
        pkg_amount = random.randint(1, 3) * 10
        pkg_size = cal_amount / pkg_amount
        # 计算量
        # 数据包大小
        # 数据包数量
        # 能耗计算公式
        pkg = {
            'CMD': cf.select,
            'Data': {
                'name': name,
                'delay': delay,
                'jitter': jit,
                'rate': rate,
                'cal_amount': cal_amount,
                'pkg_size': pkg_size,
                'pkg_amount': pkg_amount
            }
        }
        pkg = json.dumps(pkg)
        asyncio.run(self.__communicate(pkg))