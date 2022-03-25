import csv
from functools import cmp_to_key

class Process:
    
    def __init__(self, process_id, cycles, memory_footprint) -> None:
        self.PID = process_id
        self.clock_cycles = cycles
        self.memory_footprint = memory_footprint
        self.wait = 0
        self.turn_around = 0  

    def __str__(self) -> str:
        return (f'Process ID: {self.PID},'
                f' Clock cycles: {self.clock_cycles}, Memory'
                f' {self.memory_footprint} MB, Wait time: {self.wait}'
                f'ns, Turnaround time: {self.turn_around} ns')

    def increment_wait(self, time):
        """
        Increments wait and turnaround time
        """
        self.wait += time
        self.turn_around += time

    def comparator(a, b):
        if a.clock_cycles > b.clock_cycles:
            return 1
        elif a.clock_cycles < b.clock_cycles:
            return -1
        return 0

    def is_done(self) -> bool:
        return self.clock_cycles == 0


class Processor:
    def __init__(self, speed, memory) -> None:
        self.speed = speed  
        # measured in Ghz
        self.memory = memory
        self.curr_process = None
        self.timer = 0

    def add_process(self, new_process):
        if isinstance(new_process, Process):
            self.curr_process = new_process
            return
        else:
            raise TypeError('Must be a new process')

    def has_process(self):
        if self.curr_process is not None:
            return True
        return False

    def fits_mem(self):
        return self.curr_process.memory_footprint < self.memory

    def do_work(self, time):
        if not isinstance(self.curr_process, Process):
            raise TypeError("Must be a process")
        if self.fits_mem():
            completedCycles = time * self.speed
            self.curr_process.clock_cycles -= completedCycles
            self.curr_process.turn_around += time
        else:
            raise RuntimeError("Process doesn't fit on CPU")

    def time_to_complete(self):
        if isinstance(self.curr_process, Process):
            return self.curr_process.clock_cycles / self.speed 

lowPower_speed = 2
highPower_speed = 4
highpower_cpus = 3
lowPower_cps = 3
lowPower_mem = 8000
highPower_mem = 16000
processList_queue = []
lowPower_processList_queue = []
highpower_processList_queue = []
finished_processList = []
lowPower_processList = []
highpower_processList = []

for i in range(lowPower_cps):
    lowPower_processList.append(Processor(2, lowPower_mem))
i = 0
for i in range(highpower_cpus):
    highpower_processList.append(Processor(4, highPower_mem))
    """
    Reads csv file and uses data within the file 
    """
with open('./processes.csv', newline='') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        process_id = int(f'{row["PID"]}')
        burst_time = int(f'{row["Burst Time"]}')
        memory_footprint = int(f'{row["Memory in MB"]}')
        processList_queue.append(
            Process(process_id, burst_time, memory_footprint))

highPower_wait_time = 0
lowPower_wait_time = 0

for process in processList_queue:
    """
    Process is assigned to higher power CPU if it cannot fit in the lower power CPU
    """

    if process.memory_footprint > lowPower_mem:
        highpower_processList_queue.append(process)
        highPower_wait_time += (process.clock_cycles / highPower_speed)
        continue

    if (highPower_wait_time +
        (process.clock_cycles /
         (highpower_cpus * highPower_speed))) < (
             lowPower_wait_time +
             (process.clock_cycles /
              (lowPower_cps * lowPower_speed))):
        highpower_processList_queue.append(process)
        highPower_wait_time += (process.clock_cycles / highPower_speed)
    else:
        lowPower_processList_queue.append(process)
        lowPower_wait_time += (process.clock_cycles / lowPower_speed)

# Sorts processes to find shortest process
lowPower_processList_queue = sorted(lowPower_processList_queue,
                                      key = cmp_to_key(Process.comparator))
highpower_processList_queue = sorted(highpower_processList_queue,
                                       key = cmp_to_key(Process.comparator))

while len(lowPower_processList_queue) !=0 or len(
        highpower_processList_queue) != 0:

    for processor in lowPower_processList:
        if not processor.has_process() or processor.curr_process.is_done():
            if processor.has_process():
                finished_processList.append(processor.curr_process)

            if len(lowPower_processList_queue) != 0:
                processor.add_process(lowPower_processList_queue[0])
                lowPower_processList_queue.pop(0)
            else:
                processor.curr_process = None

    for processor in highpower_processList:
        if not processor.has_process() or processor.curr_process.is_done():
            if processor.has_process():
                finished_processList.append(processor.curr_process)

            if len(highpower_processList_queue) != 0:
                processor.add_process(highpower_processList_queue[0])
                highpower_processList_queue.pop(0)
            else:
                processor.curr_process = None

    shortest_time_left = 10**12 + 1
    # Find shortest time
    for processor in lowPower_processList:
        if processor.has_process():
            shortest_time_left = min(shortest_time_left,
                                     processor.time_to_complete());

    for processor in highpower_processList:
        if processor.has_process():
            shortest_time_left = min(shortest_time_left,
                                     processor.time_to_complete())

    for processor in lowPower_processList:
        if processor.has_process():
            processor.do_work(shortest_time_left)

    for processor in highpower_processList:
        if processor.has_process():
            processor.do_work(shortest_time_left)

    # Increments wait time for all processes in queue
    for process in lowPower_processList_queue:
        process.increment_wait(shortest_time_left)

    for process in highpower_processList_queue:
        process.increment_wait(shortest_time_left)

# Completes all processes left in queue
for processor in lowPower_processList:
    if processor.has_process() and (not processor.curr_process.is_done()):
        processor.do_work(processor.time_to_complete())
        finished_processList.append(processor.curr_process)
    elif processor.has_process():
        finished_processList.append(processor.curr_process)

for processor in highpower_processList:
    if processor.has_process() and (not processor.curr_process.is_done()):
        processor.do_work(processor.time_to_complete())
        finished_processList.append(processor.curr_process)
    elif processor.has_process():
        finished_processList.append(processor.curr_process)

total_wait_time = 0 
total_turnaround_time = 0
for process in finished_processList:
    total_wait_time += process.wait
    total_turnaround_time += process.turn_around

avg_wait = total_turnaround_time / len(finished_processList)
avg_turnaround = total_turnaround_time / len(finished_processList)

print(f"Average wait time: {round(avg_wait * (10**-9), 3)} s")
print(f"Average turnaround time: {round(avg_turnaround * (10**-9), 3)} s")