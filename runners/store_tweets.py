import psycopg2
from sqlalchemy import create_engine

from constants import conn_string


class StoreTweets:
    def __init__(self):
        self.engine = create_engine(conn_string)
        self.conn = self.engine.connect()

    def storetweets(self, dataframe):

        dataframe.to_sql('twitter', con=self.conn, if_exists='replace',
                         index=False)

    def __del__(self):
        self.conn.close()
