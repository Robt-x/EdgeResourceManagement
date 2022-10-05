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
        return resp
    else:
        res = dbo.db_one_node_data_delete(cf.sql_delete_one_node_data, data)
        resp['CMD'] = "delete"
        resp['State'] = "End"
        resp['Content'] = res
        return resp


def task_schedule_module(data):
    delay = data['delay']
    jit = data['jitter']
    rate = data['rate']
    cal = data['cal_amount']
    p_size = data['pkg_size']
    p_amount = data['pkg_amount']
    calf = cal * 2**-3 / (delay * 10e3)  # P(Ghz or click per sec) = cal(GB)* 2**-3 / (Delay(ms) * 10e3)
    memory = 0
    bandwidth = rate  # rate < bandwidth
    pass


def re_view_module(data):
    resp_clear()
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
    return resp
