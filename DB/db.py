import pandas as pd
import sqlite3

select = "SELECT * FROM "

dbFile = input()
dbTable = input()

conn = sqlite3.connect(dbFile, isolation_level=None,
                       detect_types=sqlite3.PARSE_COLNAMES)
db_df = pd.read_sql_query(select + dbTable, conn)
db_df.to_csv('database.csv', index=False)