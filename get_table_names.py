
from promptflow import tool
from promptflow.connections import CustomConnection
#from langchain.sql_database import SQLDatabase

# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need

@tool
def get_table_names(schema_name: str) -> str:
    
    #Get table names from the DB in future  
    file = open('./tablenames.txt','r')
    tablenames = file.read()
    file.close()     
    return tablenames

