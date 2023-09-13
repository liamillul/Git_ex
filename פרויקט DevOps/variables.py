import psutil
from func import *

# CPU cores number
CPU_cores = psutil.cpu_count()
# CPU % - gives me the percentage in 1 sec intervals
CPU_percentage = psutil.cpu_percent(1)
# total, available percentage and used RAM
memory_tuple = psutil.virtual_memory()
total_RAM = memory_tuple[0]
available_RAM = memory_tuple[1]
used_RAM = memory_tuple[3]
RAM_percentage = memory_tuple[2]
# disk usage - in percentage
disk_usage_stats = psutil.disk_usage('c:')
disk_usage = disk_usage_stats[3]
# call for the 80% func
percentage_values = [CPU_percentage, RAM_percentage, disk_usage]
# NIC status - if up or not and speed
NIC_stats_dict = psutil.net_if_stats()
values_list = NIC_stats_dict.values()
# now need to print the speed
speed_list = []
speed_dict = speed_of_nic(NIC_stats_dict, speed_list)


