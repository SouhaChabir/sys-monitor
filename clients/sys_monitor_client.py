"""The Python implementation of the gRPC sys monitor client."""
import logging  #  logging library provides a flexible and powerful framework for recording log messages from Python programs. 

import os
import sys

parent_dir_name = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parent_dir_name + "/lib")

import grpc 
import sys_monitor_pb2 
import sys_monitor_pb2_grpc

from google.protobuf.empty_pb2 import Empty


# This function establishes the gRPC channel and connect to the server 
def get_sys_monitor_client():
    # Creating the insecure_channel to connect the gRPC 
    channel = grpc.insecure_channel('localhost:50051') 
    #Creating a gRPC client 
    stub = sys_monitor_pb2_grpc.SystemMonitorStub(channel)
    return stub

# This is the client side function of the getRAMUsage server function 
def client_getRAMUsage (): 
    print("Got getRAMUsage  ..")
    # Create a client 
    Client = get_sys_monitor_client()
    # call the remote function from the server 
    ResponseRAM = Client.getRAMUsage(Empty())
    # Streaming the informations about the RAM 
    print(f"Total Memory = {ResponseRAM.total / 1024 / 1024 / 1024:.2f} GB" )
    print(f"Used Memory =  {ResponseRAM.used / 1024 / 1024 / 1024:.2f} GB")
    print(f"Free Memory =  {ResponseRAM.free / 1024 / 1024 / 1024:.2f} GB")
    return ResponseRAM


# This is the client side function of the getCPUUsage server function
def client_getCPUUsage (): 
    print("Got getCPUUsage  ..")
   # Create a client 
    Client = get_sys_monitor_client()
    #call the remote function from the server. ResponseCPU is an instance from Freq
    ResponseCPU = Client.getCPUUsage(Empty())
    # Streaming the percentage about the CPU 
    print("Current Frequency:", ResponseCPU.current, "%")
    return ResponseCPU
   

# This is the client side function of the DISKUsage server function 
def client_getDISkUsage (): 
    print("Got getDISKUsage ..")
    # Create a client 
    Client = get_sys_monitor_client()
    # call the remote function from the server
    ResponseDISK = Client.getDISkUsage(Empty())
    # Streaming the informations about the DISK 
    print(f"Total DISK= {ResponseDISK.total / 1024 / 1024 / 1024:.2f} GB")
    print(f"Used DISK= {ResponseDISK.used / 1024 / 1024 / 1024:.2f} GB")
    print(f"Free DISK= {ResponseDISK.free / 1024 / 1024 / 1024:.2f} GB")
    return ResponseDISK

# To ensure that the functions are run  
if __name__ == '__main__':
    # To ensure that the logging configuration is applied when the client file 
    logging.basicConfig()
    get_sys_monitor_client()
    client_getRAMUsage ()
    client_getCPUUsage ()
    client_getDISkUsage()