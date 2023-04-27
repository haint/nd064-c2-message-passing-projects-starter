import json
import logging
import os
import psycopg2

from schemas import LocationSchema
from typing import Dict

from kafka import KafkaConsumer
from datetime import datetime

DB_USERNAME = os.environ["DB_USERNAME"]
DB_PASSWORD = os.environ["DB_PASSWORD"]
DB_HOST = os.environ["DB_HOST"]
DB_PORT = os.environ["DB_PORT"]
DB_NAME = os.environ["DB_NAME"]

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("udaconnect-location-service")

TOPIC_NAME = os.environ["TOPIC_NAME"]
KAFKA_SERVER = os.environ["KAFKA_SERVER"]

# TOPIC_NAME = "location_topic"
# KAFKA_SERVER = "localhost:9092"

# Create the kafka consumer
consumer = KafkaConsumer(TOPIC_NAME, bootstrap_servers=[KAFKA_SERVER])

def save_location(location):
    # Verify if a dictionary was provided
    try:
        location_dict = json.loads(location)
        creation_time = datetime.fromtimestamp(location_dict["timestamp"])
        str_creation_time = creation_time.strftime('%Y-%m-%d %H:%M:%S.000000')
        location_dict["creation_time"] = str_creation_time
        del location_dict["timestamp"]
    except:
        logger.warning(f"Unexpected non-dictionary payload detected: {location}")
        return

    # Validate the provided location data
    validation_result: Dict = LocationSchema().validate(location_dict)
    if validation_result:
        logger.warning(f"Unexpected data format in payload: {location}, reason: {validation_result}")
        return

    with psycopg2.connect(
        database = DB_NAME,
        user = DB_USERNAME,
        password = DB_PASSWORD,
        host = DB_HOST,
        port = DB_PORT
    ) as conn:
        person_id = int(location_dict["person_id"])
        
        with conn.cursor() as cursor:
            try:
                query = "INSERT INTO location (person_id, coordinate, creation_time) VALUES ({}, ST_Point({}, {}), '{}')".format(person_id, location_dict["latitude"], location_dict["longitude"], location_dict["creation_time"])
                cursor.execute(query)
            except Exception as e:
                logger.error(f"Unable to save location data to the database. reason: {e}")


while True:
    for message in consumer:
        location_data = message.value.decode('utf-8')
        
        save_location(location_data)
