import FuncModule as fm
from DataBaseOperator import DataBaseOperator
import json
import configuration as cf


class ServerMsgProcessor:
    def __init__(self):
        self.dbo = DataBaseOperator()
        self.dbo.DBConnect()

    async def run(self, jsonMsg, response, websocket):
        if jsonMsg == "Terminate":
            await websocket.send("Communication: Session Terminated")
            self.dbo.DBDisConnect()
            return
        # 发送消息方法，单独和请求的客户端发消息
        pkg = jsonMsg
        pkg = json.loads(pkg)
        cmd = pkg['CMD']
        data = pkg['Data']
        if cmd == "regis":
            resp = fm.register_module(data)
        elif cmd == "delete":
            resp = fm.register_module(data, regis=False)
        elif cmd == "task":
            resp = fm.task_schedule_module(data)
        elif cmd == "select":
            resp = fm.re_view_module(data)
        else:
            await response("UNKNOWN COMMAND!")
            return
        await response(json.dumps(resp), websocket)
