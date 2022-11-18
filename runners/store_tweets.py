import psycopg2
from sqlalchemy import create_engine

from constants import conn_string

class storeTweets:

engine = create_engine(conn_string)
conn = engine.connect()
df.to_sql('twitter', con=conn, if_exists='replace',
          index=False)
conn = psycopg2.connect(conn_string
                        )
conn.autocommit = True
cursor = conn.cursor()



# conn.commit()
conn.close()