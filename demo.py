from DataBaseOperator import DataBaseOperator
import configuration as cf

dbo = DataBaseOperator()
dbo.DBConnect()
dbo.db_table_build(cf.sql_create_node_table, "NODE_RESOURCE")
# res = dbo.CheckTable("NODE_RESOURCE")
# print(res)
# dbo.db_table_delete(cf.sql_delete_user_table, "User")
# dbo.db_table_delete(cf.sql_delete_node_table, "NODE_RESOURCE")
dbo.DBDisConnect()