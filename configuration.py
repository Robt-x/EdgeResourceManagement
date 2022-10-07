# database
db_address = 'database/ER.db'
# Table
sql_create_node_table = '''CREATE TABLE IF NOT EXISTS NODE_RESOURCE(
           Node_token TEXT PRIMARY KEY    NOT NULL,
           CalculateForce REAL    NOT NULL,
           Memory         REAL    NOT NULL,
           Bandwidth      REAL    NOT NULL);'''
sql_create_user_table = '''CREATE TABLE IF NOT EXISTS User(
           UserName TEXT PRIMARY KEY    NOT NULL,
           Password TEXT    NOT NULL);'''

sql_create_task_table = '''CREATE TABLE IF NOT EXISTS TASK_AllOCATION(
           Task_id TEXT     NOT NULL,
           Node_token TEXT     NOT NULL,
           CalculateForce REAL    NOT NULL,
           Memory         REAL    NOT NULL,
           Bandwidth      REAL    NOT NULL,
           PRIMARY KEY (Task_id, Node_token));'''
TableList = ["NODE_RESOURCE", "User"]
TableSQL = {
    "NODE_RESOURCE": sql_create_node_table,
    "User": sql_create_user_table
}
sql_delete_user_table = '''DROP TABLE IF EXISTS USer;'''
sql_delete_task_table = '''DROP TABLE IF EXISTS TASK_AllOCATION;'''
sql_select_user_password = "SELECT Password FROM USer WHERE UserName=?"
sql_delete_node_table = '''DROP TABLE IF EXISTS NODE_RESOURCE;'''
sql_insert_one_node_data = "INSERT INTO NODE_RESOURCE VALUES (?, ?, ?, ?)"
sql_delete_one_node_data = "DELETE FROM NODE_RESOURCE where Node_token=?;"
sql_select_one_node_data = "SELECT * FROM NODE_RESOURCE where Node_token=?;"
sql_select_all_node_data = "SELECT * FROM NODE_RESOURCE;"
sql_update_node_data = "UPDATE NODE_RESOURCE SET CalculateForce = ?, Memory = ?, Bandwidth=? WHERE Node_token=?; "
sql_insert_task_data = "INSERT INTO TASK_ALLOCATION VALUES(?, ?, ?, ?, ?)"
sql_select_limit_node_data = "SELECT * FROM NODE_RESOURCE Order BY Memory DESC, CalculateForce DESC, Bandwidth DESC LIMIT ? OFFSET ?;"
sql_select_task_data = "SELECT * FROM TASK_ALLOCATION WHERE Task_id=? AND Node_token = ?"
sql_update_task_data = "UPDATE TASK_ALLOCATION SET CalculateForce = ?, Memory = ?, Bandwidth=? WHERE Task_id=? AND Node_token = ?;"
# server & agent
socket_address = 'ws://localhost:8765'
socket_domain = 'localhost'
socket_port = 8765
# commands
regis = "regis"
delete = "delete"
select = "select"
task = "task"
