from concurrent import futures

import grpc
import location_pb2
import location_pb2_grpc

import json
import os
from kafka import KafkaProducer

TOPIC_NAME = os.environ["TOPIC_NAME"]
KAFKA_SERVER = os.environ["KAFKA_SERVER"]

# TOPIC_NAME = "location_topic"
# KAFKA_SERVER = "localhost:9092"

producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)

class LocationService(location_pb2_grpc.LocationServiceServicer):
    def Create(self, request, context):
        request_value = {
            "person_id": int(request.person_id),
            "latitude": request.latitude,
            "longitude": request.longitude,
            "timestamp": request.timestamp
        }

        #TODO: produce to kafka

        encoded_data = json.dumps(request_value).encode('utf-8')
        producer.send(TOPIC_NAME, encoded_data)
        producer.flush()

        print(f"Data sent ${request_value}")

        return location_pb2.LocationMessage(**request_value)
    
# Initialize gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
location_pb2_grpc.add_LocationServiceServicer_to_server(LocationService(), server)

print("Server starting on port 5005...")
server.add_insecure_port("[::]:5005")
server.start()


# Kee thread alive
server.wait_for_termination()


