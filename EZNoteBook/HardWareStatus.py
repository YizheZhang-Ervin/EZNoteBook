import psutil


def getCPUStatus():
    # CPU
    cpuStatus = "CPU-Core Quantities: " + str(psutil.cpu_count(logical=False)) + ",\n Usage: "  # number of cpu
    cpuStatus += str(psutil.cpu_percent(1, 0)) + ",\n Each Thread Usage Rate: \n"  # usage of cpu
    cpuStatus += str(psutil.cpu_percent(1, 1))  # usage rate of each cpu
    # status2.configure(text=cpuStatus)
    return cpuStatus


def getRAMStatus():
    # RAM
    ram = psutil.virtual_memory()  # ram
    ramStatus = "RAM-Total Memory: " + str(int(ram.total / 1024 / 1024)) + "M,\n Used RAM:"  # total ram
    ramStatus += str(int(ram.used / 1024 / 1024)) + "M,\n Remaining RAM: "  # used ram
    ramStatus += str(int(ram.free / 1024 / 1024)) + "M,\n Usage Rate: "  # remaining ram
    sumRam = str(int(ram.used / 1024 / 1024) / int(ram.total / 1024 / 1024) * 100)  # usage rate of ram
    ramStatus += sumRam[0:5] + "%"
    # status2.configure(text=ramStatus)
    return ramStatus


def getDISKStatus():
    # DISK
    disk = psutil.disk_usage('/')
    diskStatus = "Disk-Total capacity: " + str(int(disk.total / 1024 / 1024 / 1024)) + "G"  # total disk capacity
    diskStatus += ",\n Used Capacity: " + str(int(disk.used / 1024 / 1024 / 1024)) + "G"  # Used hard disk capacity
    diskStatus += ",\n Remaining Capacity: " + str(
        int(disk.free / 1024 / 1024 / 1024)) + "G"  # remaining hard disk capacity
    sumDisk = str(
        int(disk.used / 1024 / 1024 / 1024) / int(disk.total / 1024 / 1024 / 1024) * 100)  # usage rate of hard disk
    diskStatus += ",\n Usage Rate: " + sumDisk[0:5] + "%"
    # status2.configure(text=diskStatus)
    return diskStatus


def getHardwareStatus(status2):
    status2.configure(text='--------CPU--------\n'+getCPUStatus()+'\n\n--------RAM--------\n'+getRAMStatus()+'\n\n--------DISK--------\n'+getDISKStatus())