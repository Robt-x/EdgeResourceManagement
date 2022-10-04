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
        resp = {
            'CMD': "",
            'State': None,
            'Content': None
        }
        if cmd == "regis":
            resp = fm.register_module(data)
        elif cmd == "delete":
            res = self.dbo.db_one_node_data_delete(cf.sql_delete_one_node_data, data)
            resp['CMD'] = "delete"
            resp['State'] = "End"
            resp['Content'] = res
        elif cmd == "task":
            pass
        elif cmd == "select":
            resp = fm.re_view_module(data)
        else:
            await response("UNKNOWN COMMAND!")
            return
        await response(json.dumps(resp), websocket)
