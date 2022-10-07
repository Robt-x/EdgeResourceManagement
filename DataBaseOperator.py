import sqlite3
import configuration as cf


class DataBaseOperator:
    def __init__(self):
        self.__conn = None

    def DBConnect(self):
        self.__conn = sqlite3.connect(cf.db_address)

    def DBDisConnect(self):
        self.__conn.close()

    def CheckTable(self, table):
        c = self.__conn.cursor()
        # noinspection PyBroadException
        try:
            res = c.execute("SELECT count(*) FROM sqlite_master WHERE type=? AND name = ?;", ["table", table])
            self.__conn.commit()
            f = list(res.fetchone())[0]
            if f == 0:
                return False
            else:
                return True
        except Exception:
            pass

    def db_table_build(self, sql, table):
        c = self.__conn.cursor()
        # noinspection PyBroadException
        try:
            c.execute(sql)
            self.__conn.commit()
            print("The " + table + " table has been prepared")
        except Exception:
            print("Failed to prepare the " + table + " table")

    def db_table_delete(self, sql, table):
        c = self.__conn.cursor()
        # noinspection PyBroadException
        try:
            c.execute(sql)
            self.__conn.commit()
            print("The " + table + " table is dropped successfully")
        except Exception:
            print("Failed to drop the " + table + " table")

    def db_one_node_data_insert(self, sql, data):
        c = self.__conn.cursor()
        # noinspection PyBroadException
        try:
            c.execute(sql, tuple([data[k] for k in data.keys()]))
            self.__conn.commit()
            return "Success"
        except Exception:
            return "Failed"

    def db_one_node_data_delete(self, sql, token):
        c = self.__conn.cursor()
        # noinspection PyBroadException
        try:
            c.execute(sql, [token])
            self.__conn.commit()
            return "Success"
        except Exception:
            return "Failed"

    def db_node_data_select(self, sql, token=None):
        c = self.__conn.cursor()
        # noinspection PyBroadException
        try:
            if token is None:
                res = c.execute(sql)
                return list(res.fetchall())
            else:
                res = c.execute(sql, [token])
                return res.fetchone()
        except Exception:
            print("Failed")

    def db_limit_node_data_select(self, sql, limit, offset=0):
        c = self.__conn.cursor()
        # noinspection PyBroadException
        try:
            res = c.execute(sql, [limit, offset])
            return res.fetchall()
        except Exception:
            print("Limit Fetch Failed")

    def db_task_resource_allocation(self, task_id, token, res, pk):
        c = self.__conn.cursor()
        # noinspection PyBroadException
        try:
            rc = c.execute(cf.sql_select_task_data, [task_id, token]).fetchone()
            c.execute(cf.sql_update_node_data, [res[0], res[1], res[2], token])
            if rc is None:
                c.execute(cf.sql_insert_task_data, [task_id, token, pk[0], pk[1], pk[2]])
            else:
                c.execute(cf.sql_update_task_data, [pk[0]+rc[2], pk[1]+rc[3], pk[2]+rc[4], task_id, token])
            self.__conn.commit()
            return "Success"
        except Exception:
            print(" Allocation Failed")

    def db_user_confirm(self, name, pwd):
        c = self.__conn.cursor()
        # noinspection PyBroadException
        try:
            res = c.execute(cf.sql_select_user_password, [name])
            password = res.fetchone()[0]
            return password == pwd
        except Exception:
            print("Failed")

    def re_release(self):
        pass
