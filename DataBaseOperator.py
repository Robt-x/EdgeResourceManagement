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

    def db_one_node_data_updata(self, sql, token, data):
        c = self.__conn.cursor()
        # noinspection PyBroadException
        try:
            res = c.execute(sql, [token, data[0], data[1], data[2], data[3]])
            return list(res.fetchall())
        except Exception:
            print("Failed")

    def db_user_confirm(self, name, pwd):
        c = self.__conn.cursor()
        # noinspection PyBroadException
        try:
            res = c.execute(cf.sql_select_user_password, [name])
            password = res.fetchone()[0]
            return password == pwd
        except Exception:
            print("Failed")

    def re_allocation(self):
        resource_node = {
            'node': [],
            'resource': []
        }

        pass

    def re_release(self):
        pass
