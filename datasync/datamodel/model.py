import logging
import time
import mysql.connector
import os
import json
from datasync.datamodel.db_connector import database_access
from datasync.datacaching.redisinit import RedisIni
from datasync.configuration import log_config

logger = log_config.configure_logging()
# Create a custom filter to add the class name to the log record
class ClassNameFilter(logging.Filter):
    def __init__(self, name=""):
        super().__init__()
        self.class_name = name

    def filter(self, record):
        record.classname = self.class_name
        return True

class DataModel:
    def __init__(self):
        self.current_directory = os.path.abspath(os.path.dirname(__file__))
        self.datasync_directory = os.path.join(self.current_directory, '..', '..', 'datasync')
        self.script = os.path.join(self.datasync_directory, "scripts/sellerValidation.sql")
        #self.sync = RedisIni()

    def datacontrol(self):
        while True:
            # Establish a database connection
            connection = database_access()
            # Create a cursor object to execute SQL queries
            cursor = connection.cursor(dictionary=True)  # Use dictionary cursor to get JSON-like results
            try:
                # Read and execute SQL queries from the SQL file
                logger.addFilter(ClassNameFilter(self.__class__.__name__))
                with open(self.script, 'r') as sql_file:
                    queries = sql_file.read().split(';')
                    logger.info("database connected successfully")
                    for query in queries:
                        if query.strip():
                            cursor.execute(query)
                            # Fetch and print the results in JSON format
                            results = cursor.fetchall()
                            value = json.dumps(results, indent=4)
                            logger.debug("queries are executed successfully.")
                            logger.debug(value)
                            RedisIni().caching(value=value)
                connection.commit()
            except mysql.connector.Error as err:
                logger.error(f"Error: {err}")
            finally:
                # Close the cursor and database connection
                cursor.close()
                connection.close()
            time.sleep(43200)

if __name__ == "__main__":
    instance = DataModel()
    instance.datacontrol()
