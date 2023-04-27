import grpc
import location_pb2
import location_pb2_grpc
from datetime import datetime

"""
Sample implementation of a writer that can be used to write messages to gRPC.
"""

print("Sending sample payload...")


channel = grpc.insecure_channel("localhost:5005")
stub = location_pb2_grpc.LocationServiceStub(channel)

# location = location_pb2.LocationMessage(
#     person_id = 1,
#     latitude = -122.290883,
#     longtitude = 37.55363,
#     timestamp = datetime.time.microsecond
# )

timestamp = int(round(datetime.now().timestamp()))

location = location_pb2.LocationMessage(person_id=1,latitude="-122.290883", longitude="37.55363", timestamp=timestamp)

response = stub.Create(location)