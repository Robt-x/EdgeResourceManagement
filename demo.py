from DataBaseOperator import DataBaseOperator
import configuration as cf

dbo = DataBaseOperator()
dbo.DBConnect()
node_list = dbo.db_limit_node_data_select(cf.sql_select_limit_node_data, limit=5, offset=0)
for i in node_list:
    print(i)
# dbo.db_table_build(cf.sql_create_task_table, "TASK_AllOCATION")
# res = dbo.CheckTable("NODE_RESOURCE")
# print(res)
# dbo.db_table_delete(cf.sql_delete_user_table, "User")
# dbo.db_table_delete(cf.sql_delete_task_table, "TASK_AllOCATION")
dbo.DBDisConnect()
