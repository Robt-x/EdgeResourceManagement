from tools import *
from DataBaseOperator import DataBaseOperator

dbo = DataBaseOperator()
resp = {
    'CMD': "",
    'State': "",
    'Content': None
}


def resp_clear():
    resp['CMD'] = ""
    resp['State'] = ""
    resp['Content'] = None


def register_module(data, regis=True):
    resp_clear()
    dbo.DBConnect()
    if regis is True:
        res = dbo.db_one_node_data_insert(cf.sql_insert_one_node_data, data)
        resp['CMD'] = "regis"
        resp['State'] = "End"
        resp['Content'] = res

    else:
        res = dbo.db_one_node_data_delete(cf.sql_delete_one_node_data, data)
        resp['CMD'] = "delete"
        resp['State'] = "End"
        resp['Content'] = res
    dbo.DBDisConnect()
    return resp


def task_schedule_module(data):
    resp_clear()
    dbo.DBConnect()
    task_id = data['id']
    delay = data['delay']
    jit = data['jitter']
    rate = data['rate']
    package = data['package']  # 2**5～2**6 * 1/1024 GB
    calf = [cf_req(delay, p) for p in package]
    memory = [p / 512 for p in package]  # memory >= package[i]
    bandwidth = rate  # bandwidth >= rate
    task_tp = []
    for c, m in zip(calf, memory):
        task_tp.append([c, m, bandwidth])
    node_list = dbo.db_limit_node_data_select(cf.sql_select_limit_node_data, limit=5, offset=0)
    for (token, c, m, b) in node_list:
        for pk in task_tp:
            isOK, res = match(pk, [c, m, b])
            if isOK:
                pass
    dbo.DBDisConnect()
    return resp


def cf_req(delay, p_size):
    return p_size * 10e3 / (delay * 1024)  # P(Ghz or Gclick per sec) >= p_size(GB) / (Delay(s) * 8)


def match(t, n):
    res = []
    for e1, e2 in zip(t, n):
        e = e2 - e1
        if e < 0:
            return False, None
        res.append(e)
    return True, res


def re_view_module(data):
    resp_clear()
    dbo.DBConnect()
    if data['type'] == "all":
        f = dbo.db_user_confirm(data['user'], data['pwd'])
        if f is False:
            resp['CMD'] = "select"
            resp['State'] = "End"
            resp['Content'] = "The user name does not match the password"
        else:
            res = dbo.db_node_data_select(cf.sql_select_all_node_data)
            resp['CMD'] = "select"
            resp['State'] = "End"
            resp['Content'] = res
    else:
        res = dbo.db_node_data_select(cf.sql_select_one_node_data, data)
        resp['CMD'] = "select"
        resp['State'] = "End"
        resp['Content'] = res
    dbo.DBDisConnect()
    return resp
