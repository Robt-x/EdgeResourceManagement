import sqlite3
import configuration as cf
import uuid


def db_table_build(sql, table):
    conn = sqlite3.connect(cf.db_address)
    c = conn.cursor()
    # noinspection PyBroadException
    try:
        c.execute(sql)
        conn.commit()
        print("The " + table + " table has been prepared")
    except Exception:
        print("Failed to prepare the " + table + " table")
    finally:
        conn.close()


def db_table_delete(sql, table):
    conn = sqlite3.connect(cf.db_address)
    c = conn.cursor()
    # noinspection PyBroadException
    try:
        c.execute(sql)
        conn.commit()
        print("The " + table + " table is dropped successfully")
    except Exception:
        print("Failed to drop the " + table + " table")
    conn.close()


def db_one_node_data_insert(sql, data):
    conn = sqlite3.connect(cf.db_address)
    c = conn.cursor()
    # noinspection PyBroadException
    try:
        c.execute(sql, tuple([data[k] for k in data.keys()]))
        conn.commit()
        print("The data has been inserted successfully")
    except Exception:
        print("Failed to insert the data")
    conn.close()


def db_one_node_data_delete(sql, token):
    conn = sqlite3.connect(cf.db_address)
    c = conn.cursor()
    # noinspection PyBroadException
    try:
        c.execute(sql, [token])
        conn.commit()
        print("The data has been deleted successfully")
    except Exception:
        print("Failed to delete the data")
    conn.close()


def db_one_node_data_select(sql, token):
    conn = sqlite3.connect(cf.db_address)
    c = conn.cursor()
    # noinspection PyBroadException
    try:
        res = c.execute(sql, [token])
        for r in res:
            print(r)
        print("The data has been selected successfully")
    except Exception:
        print("Failed to select the data")
    conn.close()
