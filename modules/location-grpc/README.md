## Generating gRPC files
`pip install grpcio-tools grpcio`

`python3 -m grpc_tools.protoc -I./ --python_out=./ --pyi_out=./ --grpc_python_out=./ location.proto`