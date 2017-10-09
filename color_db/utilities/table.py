import psycopg2
import psycopg2.extras

from .. import configuration

class Table:
    """
    Table is a postgres table. 
    The table class allows easy manipulation of postgres tables.
    """

    # initialize
    def __init__(self, connection=configuration.PG_CONNECTION):
        
        # postgres connection
        self.postgres_connection = psycopg2.connect(connection)

        # postgres database cursor
        self.postgres_cursor = self.postgres_connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    # create a table
    def create(self, name, columns):

        # set-up dict to capture relevant info
        d = {
            "name": name,
            "columns": columns
        }
        
        statement = "drop table if exists " + name + "; create table " + name + " (id serial primary key, name text, description text);"

        # ingest to postgres
        self.postgres_cursor.execute(statement)
        
        # commit changes
        self.postgres_connection.commit()
        
        # close cursor
        self.postgres_cursor.close()
        
        # close connection
        self.postgres_connection.close()