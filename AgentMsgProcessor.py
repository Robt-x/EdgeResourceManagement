import json
import configuration as cf
import websockets


class AgentMsgProcessor:
    async def run(self, jsonMsg, response, websocket):
        if jsonMsg == "Communication: Session Established":
            return "", None
        if jsonMsg == "Communication: Session Terminated":
            return "break", None
        pkg = json.loads(jsonMsg)
        state = pkg['State']
        print("State: {}".format(state))
        content = pkg['Content']
        await response("Terminate", websocket)
        return "", content
