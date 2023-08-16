#!/bin/bash

echo "Generating python grpc library ..."
python3 -m grpc_tools.protoc -Iprotos --python_out=lib/ --pyi_out=lib/ --grpc_python_out=lib/ --doc_out=doc/ --doc_opt=html,index.html sys_monitor.proto