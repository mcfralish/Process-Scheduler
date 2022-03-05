from project_tools import sorted_processes, unsorted_processes


class processor:
    def __init__(self, speed):
        self.speed = speed
        self.time_elapsed = 0


def FIFO(fname, num_slow, num_fast):

    processors = []
    for i in range(num_slow):
        processors.append(processor(2))

    for i in range(num_fast):
        processors.append(processor(4))

    processes = unsorted_processes(fname)

    threshold = pow(10, 11)

    slow_index = 0
    fast_index = num_slow

    wait_times = []
    turnaround_times = []

    for i in range(len(processes)):
        if int(processes[i][1]) < threshold:
            wait_times.append(processors[slow_index].time_elapsed)
            processors[slow_index].time_elapsed += int(processes[i][1])
            turnaround_times.append(processors[slow_index].time_elapsed)
            slow_index += 1
            if slow_index == num_slow:
                slow_index -= num_slow

        else:
            wait_times.append(processors[fast_index].time_elapsed)
            processors[fast_index].time_elapsed += int(processes[i][1])
            turnaround_times.append(processors[fast_index].time_elapsed)
            fast_index += 1
            if fast_index == (num_slow + num_fast):
                fast_index -= num_fast

    for i in range(len(processors)):
        print("Processor ", i, ":")
        print("Time Elapsed: ", processors[i].time_elapsed)

    print(wait_times)
    print(turnaround_times)


FIFO("./processes.csv", 3, 3)
