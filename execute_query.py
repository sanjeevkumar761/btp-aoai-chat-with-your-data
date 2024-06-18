from promptflow import tool
import pyodbc
from dotenv import load_dotenv
import os

load_dotenv()
@tool
def execute_query(query: str) -> str:
    print("in execute_query, query", query)
    cnxn = pyodbc.connect(os.getenv("DB_CONNECTION_STRING"))
    cursor = cnxn.cursor()
    #cursor.execute('SELECT * FROM "SAPA4H"."SFLIGHT"')
    cursor.execute(query)
    rows = cursor.fetchall()
    print(rows)
    rowsStr = "SQL query is " + query + " and result is as follows: " + "\n"
    for row in rows:
        for r in row:
            print(str(r))
            rowsStr = rowsStr + str(r) + ","
        rowsStr = rowsStr + " \n"
    print(rowsStr)
    cursor.close()
    cnxn.close()
    return rowsStr
