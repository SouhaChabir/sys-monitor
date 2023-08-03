"""The Python implementation of the gRPC sys monitor server."""
from concurrent import futures
import logging  #  logging library provides a flexible and powerful framework for recording log messages from Python programs. 

import grpc 
import sys_monitor_pb2 
import sys_monitor_pb2_grpc 
import psutil   # psutil is a Process and System Utilites Python library 


class SystemMonitorServicerImpl(sys_monitor_pb2_grpc.SystemMonitorServicer):
    """Provides methods that implement functionality of sys monitor server."""

    # This method retrieves the informations about the RAM 
    def getRAMUsage(self, request, context): 
        # ram_info is a tuple contains various attributes representing the virtual memory statistics of the system,
        # such as total memory, available memory, used memory, and more.
        #The virtual_memory() function returns this information as a named tuple.
        ram_info = psutil.virtual_memory()  
        # result is an instance of the class RAMInfo( the message defined in .proto ): A CLASS 
        result = RAMInfo()
        # total is a field from the RAMInfo message 
        result.total = ram_info.total
        result.used = ram_info.used
        result.free = ram_info.free 
        return result

 
    # This method contains the information about the CPU 
    def getCPUUsage(self, request, context):
          # cpu_info is a tuple contains various attributes representing the CPU statistics of the system
          cpu_info = psutil.cpu_freq()
          # Freq is a class instantiated from CPUFreq 
          Freq = CPUFreq () 

          Freq.current = cpu_info.current 
          Freq.minimum = cpu_info.minimum
          Freq.maximum = cpu_info.maximum
          return Freq 
     

    # This method contains the information about the Disk 
    def getDISkUsage(self, request, context):  
         # disk_info is a tuple contains various attributes representing the DISK statistics of the system
          disk_info = psutil.disk_usage()
          resultD= DISKinfo()
          resultD.total = disk_info.total 
          resultD.used = disk_info.used
          resultD.free = disk_info.free
          return resultD


# This function is a server-side code for a gRPC 
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

#Execute the serve() function 
if __name__ == '__main__':
    # initializes the logging system for the gRPC server
    # The basicConfig() function ensures that the gRPC server's logs will be displayed on the console.
    logging.basicConfig() 
    serve()





    # To ensure that the run function is executed 