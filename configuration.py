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
TableList = ["NODE_RESOURCE", "User"]
TableSQL = {
    "NODE_RESOURCE": sql_create_node_table,
    "User": sql_create_user_table
}
sql_delete_user_table = '''DROP TABLE IF EXISTS USer;'''
sql_select_user_password = "SELECT Password FROM USer WHERE UserName=?"
sql_delete_node_table = '''DROP TABLE IF EXISTS NODE_RESOURCE;'''
sql_insert_one_node_data = "INSERT INTO NODE_RESOURCE VALUES (?, ?, ?, ?)"
sql_delete_one_node_data = "DELETE FROM NODE_RESOURCE where Node_token=?;"
sql_select_one_node_data = "SELECT * FROM NODE_RESOURCE where Node_token=?;"
sql_select_all_node_data = "SELECT * FROM NODE_RESOURCE;"
sql_update_one_node_data = "UPDATE NODE_RESOURCE SET CalculateForce = ?, Memory = ?, Bandwidth=? WHERE Node_token=?; "
# server & agent
socket_address = 'ws://localhost:8765'
socket_domain = 'localhost'
socket_port = 8765
# commands
regis = "regis"
delete = "delete"
select = "select"
business = "task"
