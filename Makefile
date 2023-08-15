protoc:
	 python3 -m grpc_tools.protoc -I proto --python_out=./protobuff --pyi_out=./protobuff --grpc_python_out=./protobuff proto/product.proto

