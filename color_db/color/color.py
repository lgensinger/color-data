import json
import psycopg2
import psycopg2.extras

from .. import configuration

class Color:
    """
    Color is a color object. 
    It is the lowerst-level color object and represents a single value.
    """

    # initialize
    def __init__(self, connection):

        # postgres database cursor
        self.postgres = psycopg2.connect(connection).cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    # create a color object
    def create(self, r, g, b):

        # set-up dict to capture relevant info
        d = {
            "r": r,
            "g": g,
            "b": b
        }
        
        statement = "insert into test (r,g,b) values (200,234,100);"

        # ingest to postgres
        self.postgres.execute(statement)
        
        # close connection
        self.postgres.close()
        
        # commit changes
        self.postgres.commit()