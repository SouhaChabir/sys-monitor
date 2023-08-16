"""The Python implementation of the gRPC sys monitor server."""
from concurrent import futures
import logging  #  logging library provides a flexible and powerful framework for recording log messages from Python programs. 

import os 
import sys

parent_dir_name = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parent_dir_name + "/lib")

import grpc 
import sys_monitor_pb2
import sys_monitor_pb2_grpc
import psutil   # psutil is a Process and System Utilites Python library

class SystemMonitorServicerImpl(sys_monitor_pb2_grpc.SystemMonitorServicer):
    """Provides methods that implement functionality of sys monitor server."""

    # This method retrieves the info sys_monitor_pb2 informations about the RAM 
    def getRAMUsage(self, request, context):
        logging.info("Got getRAMUsage request ..")
        # ram_info is a tuple contains various attributes representing the virtual memory statistics of the system,
        # such as total memory, available memory, used memory, and more.
        #The virtual_memory() function returns this information as a named tuple.
        ram_info = psutil.virtual_memory()  
        # RAM is an instance of the class RAMInfo( the message defined in .proto ): A CLASS 
        RAM = sys_monitor_pb2.RAMinfo()
        # total is a field from the RAMInfo message 
        RAM.total = ram_info.total
        RAM.used = ram_info.used
        RAM.free = ram_info.free
        logging.info(f"Total RAM = {RAM.total / 1024 / 1024 / 1024:.2f} GB")
        logging.info(f"UsedRAM = {RAM.used / 1024 / 1024 / 1024:.2f} GB")
        logging.info(f"Free RAM = {RAM.free / 1024 / 1024 / 1024:.2f} GB")
        
        return RAM
        
 
    # This method contains the information about the CPU 
    def getCPUUsage(self, request, context):
        logging.info("Got getCPUUsage request ..")
        # cpu_info is a tuple contains various attributes representing the CPU statistics of the system
        #cpu_info = psutil.percent()
        # Freq is an instance from CPUFreq 
        Freq = sys_monitor_pb2.CPUFreq()
        Freq.current = psutil.cpu_percent(2)
        logging.info(f"Percentage usage: {Freq.current}%")
        return Freq 


    # This method contains the information about the Disk 
    def getDISkUsage(self, request, context):  
        # disk_info is a tuple contains various attributes representing the DISK statistics of the system
        disk_info = psutil.disk_usage("/")
        # DISK is an instance from DISKinfo
        DISK= sys_monitor_pb2.DISkinfo()
        # Filling the fields 
        DISK.total = disk_info.total
        DISK.used = disk_info.used
        DISK.free = disk_info.free
        logging.info(f"Total DISK =  {DISK.total / 1024 / 1024 / 1024:.2f} GB") 
        logging.info(f"Used DISK = {DISK.used / 1024 / 1024 / 1024:.2f} GB")
        logging.info(f"Free DISK = {DISK.free / 1024 / 1024 / 1024:.2f} GB")
        return DISK


# This function is a server-side code for a gRPC. This function allows the server to listen ro the client requests 
def serve():
    # Create a gRPC Server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    # Add Servicer to the Server
    # The SystemMonitorServicer() is the class that implements the actual behavior of the gRPC service. 
    # It contains the implementation of all the RPC methods defined in the service's .proto file
    sys_monitor_pb2_grpc.add_SystemMonitorServicer_to_server(SystemMonitorServicerImpl(), server)
    # Configure Server Port, like opening a socket 
    server.add_insecure_port('[::]:50051')  
    # Start the Server
    server.start()
    # Wait for Termination
    server.wait_for_termination()
    logging.info("Done")

#Execute the serve() function 
if __name__ == '__main__':
    # initialize the logging system for the gRPC server
    # The basicConfig() function ensures that the gRPC server's logs will be displayed on the console.
    try:
        logging.basicConfig() 
        serve()
        getRAMUsage()
        getCPUUsage()
        getDISkUsage()
    except KeyboardInterrupt:
        logging.warning("Got Keyboard interruption, exiting ...")
