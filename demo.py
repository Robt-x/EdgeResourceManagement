from DataBaseOperator import DataBaseOperator
import configuration as cf

dbo = DataBaseOperator()
dbo.DBConnect()
# dbo.db_table_build(cf.sql_create_task_table, "TASK_AllOCATION")
# res = dbo.CheckTable("NODE_RESOURCE")
# print(res)
# dbo.db_table_delete(cf.sql_delete_user_table, "User")
# dbo.db_table_delete(cf.sql_delete_task_table, "TASK_AllOCATION")
dbo.DBDisConnect()
