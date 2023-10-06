class CPU:
    def __init__(self, cores) -> None:
        self.cores = cores

class RAM:
    def __init__(self,size) -> None:
        self.size = size

class Harddrive:
    def __init__(self, capacity) -> None:
        self.capacity = capacity

class Computer:
    def __init__(self, cores, ram, hd_capacity) -> None:
        self.cpu = CPU(cores)
        self.ram = RAM(ram)
        self.hard_disc = Harddrive(hd_capacity)

mac =  Computer(8,16,512)
        