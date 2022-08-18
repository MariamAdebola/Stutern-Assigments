#import libraries

import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine

#create a connect to postgres

engine = create_engine("postgresql+psycopg2://postgres:4991@localhost:5432/demo_DB", pool_recycle=-1)

db_engine = engine.connect()

print("engine created successfully")

def query_db(query: str, db_conn: sqlalchemy.engine.base.Connection) -> pd.DataFrame:
    df = pd.read_sql(query, db_conn)
    print(df)
    return df

query_db("SELECT * FROM science_student LIMIT 10", db_engine)

db_engine.close()
