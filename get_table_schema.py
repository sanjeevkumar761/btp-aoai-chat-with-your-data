from promptflow import tool
from promptflow.connections import CustomConnection
#from langchain.sql_database import SQLDatabase
import ast

# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def get_table_schema(tables: str, schema_name: str) -> str:
    #In future get table schema from the DB
    print("In get_table_schema, tables", tables)
    #tables_list = ast.literal_eval(tables)
    #print(tables_list)
    file = open('./tableschema.txt','r')
    tableschema = file.read()
    file.close()
    return tableschema
    #return db.get_table_info_no_throw()

