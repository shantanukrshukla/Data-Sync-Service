import configparser
import logging
import time
import redis
import os
from datasync.configuration import log_config

#logs init
logger = log_config.configure_logging()
# Get the path to the directory where this scripts is located
current_directory = os.path.abspath(os.path.dirname(__file__))
datasync_directory = os.path.join(current_directory, '..', '..', 'datasync')
config_file_path = os.path.join(datasync_directory, "resource/config.ini")

# Create a ConfigParser instance and read the config.ini file
config = configparser.ConfigParser()
config.read(config_file_path)

redis_host = config.get('redis', 'host')
redis_port = config.getint('redis', 'port')
redis_password = config.get('redis', 'password')

class ClassNameFilter(logging.Filter):
    def __init__(self, name=""):
        super().__init__()
        self.class_name = name

    def filter(self, record):
        record.classname = self.class_name
        return True

class RedisIni():
    def __init__(self):
        self.redis_client = redis.StrictRedis(
            host=redis_host,
            port=redis_port,
            password=redis_password,
            decode_responses=True,  # Convert byte responses to strings
        )
    def caching(self, value):
        # Connect to the Redis server
        logger.addFilter(ClassNameFilter(self.__class__.__name__))
        try:
            client = self.redis_client
            # Push a value into a Redis key
            key = 'userDetails'
            client.set(key, value)
            # Retrieve and print the value from the Redis key
            retrieved_value = client.get(key)
            logger.info(f"Value in Redis key '{key}': {retrieved_value}")
        except redis.exceptions.ConnectionError as err:
            logger.error(f"Error connecting to Redis: {err}")
        except Exception as err:
            logger.error(f"An error occurred: {err}")
        finally:
            # Close the Redis client connection
            logger.info("last time synced at: {}".format(int(time.time())))
            if 'redis_client' in locals():
                client.close()

