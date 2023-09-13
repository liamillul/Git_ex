from variables import *
import time
while True:
    print("hello, Welcome to the automated system")
    print("CPU cores:", CPU_cores)
    print("CPU percentage:", CPU_percentage)
    print("total RAM:", total_RAM)
    print("available RAM:", available_RAM)
    print("used RAM:", used_RAM)
    print("RAM percentage:", RAM_percentage)
    print("Disk usage:", disk_usage)
    deviation_list = []
    for val in percentage_values:
        for name in names:
            print(if_deviation(val, name))
            deviation_list.append(if_deviation(val, name))
    print("NIC status:", NIC_stats_dict)
    print("NIC speed:", speed_dict)
    # up check - this func is immediately printing so has to put it here
    up_check = nic_not_up(NIC_stats_dict, values_list)
    # PART B
    start_time = time.time()
    for i in range(10):
        file = open(r"C:\Users\liami\Documents\devops.txt", 'a')
        data = ["hello, Welcome to the automated system", "CPU cores:" + str(CPU_cores),
                "CPU percentage:" + str(CPU_percentage) + "%", "total RAM:" + str(total_RAM),
                "available RAM:" + str(available_RAM),"used RAM:" + str(used_RAM),
                "RAM percentage:" + str(RAM_percentage),"Disk usage:" + str(disk_usage) + "%",
                "NIC status:" + str(NIC_stats_dict), "NIC speed:" + str(speed_dict), str(deviation_list)]
        for line in data:
            file.write(line)
            file.write("\n""\n")
        file.close()
        time.sleep(30)

    time.sleep(30)
