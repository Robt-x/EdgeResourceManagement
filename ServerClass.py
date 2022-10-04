import asyncio
import json

import websockets
import configuration as cf
import threading
# 功能模块
from DataBaseOperator import DataBaseOperator
from ServerMsgProcessor import ServerMsgProcessor

# 存储所有的客户端
Clients = []


class Server:
    def __init__(self):
        self.dbo = DataBaseOperator()
        self.dbo.DBConnect()
        for t in cf.TableList:
            if self.dbo.CheckTable(t) is False:
                self.dbo.db_table_build(cf.TableSQL[t], t)
        self.dbo.DBDisConnect()

    async def runCase(self, jsonMsg, websocket):
        pr = ServerMsgProcessor()
        await pr.run(jsonMsg, self.response, websocket)

    # 发消息给客户端的回调函数
    async def response(self, msg, websocket=None):
        await self.sendMsg(msg, websocket)

    # 发送消息
    async def sendMsg(self, msg, websocket):
        if websocket is not None:
            await websocket.send(msg)
        else:
            await self.broadcastMsg(msg)
        # 避免被卡线程
        await asyncio.sleep(0.2)

    # 群发消息
    async def broadcastMsg(self, msg):
        for user in Clients:
            await user.send(msg)

    # 每一个客户端链接上来就会进一个循环
    async def echo(self, websocket, path):
        Clients.append(websocket)
        await websocket.send("Communication: Session Established")
        while True:
            try:
                recv_text = await websocket.recv()
                # 分析当前的消息 json格式，跳进功能模块分析
                await self.runCase(recv_text, websocket=websocket)

            except websockets.ConnectionClosed:
                print("ConnectionClosed...", path)  # 链接断开
                Clients.remove(websocket)
                break
            except websockets.InvalidState:
                print("InvalidState...")  # 无效状态
                Clients.remove(websocket)
                break
            except Exception as e:
                print(e)
                Clients.remove(websocket)
                break

    # 启动服务器
    async def runServer(self):
        async with websockets.serve(self.echo, cf.socket_domain, cf.socket_port):
            await asyncio.Future()  # run forever

    # 多线程模式，防止阻塞主线程无法做其他事情
    def WebSocketServer(self):
        asyncio.run(self.runServer())

    def startServer(self):
        # 多线程启动，否则会堵塞
        thread = threading.Thread(target=self.WebSocketServer)
        thread.start()
        thread.join()
