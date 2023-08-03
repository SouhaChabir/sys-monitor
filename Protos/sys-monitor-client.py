"""The Python implementation of the gRPC sys monitor client."""
import logging  #  logging library provides a flexible and powerful framework for recording log messages from Python programs. 

import grpc 
import sys_monitor_pb2 
import sys_monitor_pb2_grpc

# This function establishes the gRPC channel and connect to the server 
def get_sys_monitor_client():
    # Creating the insecure_channel to connect the gRPC 
    channel = grpc.insecure_channel('localhost:50051') 
    #Creating a gRPC client 
    stub = sys_monitor_pb2_grpc.SystemMonitor()
    return stub
        
    
# This is the client side function of the RAMUsage server function 
def client_getRAMUsage (): 
    # Create a client 
    Client = get_sys_monitor_client()
    # Create an empty request message to the server 
    Request = sys_monitor_pb2.Empty()
    #call the remote function on the server 
    ResponseRAM = Client.getRAMUsage(Request)
    return ResponseRAM 

# This is the client side function of the CPUUsage server function 
def client_getCPUUsage (): 
   # Create a client 
    Client = get_sys_monitor_client()
    # Create an empty request message to the server 
    Request = sys_monitor_pb2.Empty()
    #call the remote function on the server 
    ResponseCPU = Client.getCPUUsage(Request)
    return ResponseCPU 

# This is the client side function of the DISKUsage server function 
def client_getDISKUsage (): 
    # Create a client 
    Client = get_sys_monitor_client()
    # Create an empty request message to the server 
    Request = sys_monitor_pb2.Empty()
    #call the remote function on the server 
    ResponseDISK = Client.getDISKUsage(Request)
    return ResponseDISK

# 
def run(stub): 
    print("-------------- getRAMUsage --------------")
    client_getRAMUsage(stub)
    print("-------------- getCPUUsage --------------")
    client_getCPUUsage(stub)
    print("-------------- getDISKUsage --------------")
    client_getDISKUsage(stub)


# To ensure that the run function is executed 
if __name__ == '__main__':
    # To ensure that the logging configuration is applied when the client file is run 
    logging.basicConfig()
    #Call the client_getRAMUsage() function to get RAM usage from the server
    ram_info = client_getRAMUsage()
    print("Total Memory:", ram_info.total)
    print("Used Memory:", ram_info.used)
    print("Free Memory:", ram_info.free)

    #Call the client_getCPUUsage() function to get CPU usage from the server
    cpu_info = client_getRAMUsage()
    print("Current Frequency:", ram_cpu.current)
    print("Min Frequency:", ram_cpu.min)
    print("Max Frequency:", ram_cpu.max)

    #Call the client_getDISKUsage() function to get DISK usage from the server
    disk_info = client_getDISKUsage()
    print("Total DISK:", ram_disk.total)
    print("Used DISK:", ram_disk.used)
    print("Free DISK:", ram_disk.free)

