from statistics import mean
from project_tools import sorted_processes, unsorted_processes
from math import sqrt


class processor:
    def __init__(self, speed):
        self.speed = speed
        self.time_elapsed = 0
        self.time_current = 0


def set_threshold(processes, num_slow, num_fast):
    """
    Sets threshold proportionate to the amount of work expected from each set of processors. In a system with equal number fast and slow processors, with the slow running at half of the speed of the fast, the slow will be rewsponsible for 1/3 of the work.
    """
    total_burst = 0
    min = float("inf")
    for i in range(len(processes)):
        burst = int(processes[i][1])
        if burst < min:
            min = burst
        total_burst += burst

    ratio = (num_slow * 2) / (num_slow * 2 + num_fast * 4)

    mean = total_burst / len(processes)

    def stdev():
        sd = 0
        for i in range(len(processes)):
            sd += (int(processes[i][1]) - mean) ** 2

        sd = sd / len(processes)
        sd = sqrt(sd)
        print("Stand Dev: ", "{:e}".format(sd))
        return sd

    print("ratio = ", ratio)
    print("mean = ", "{:e}".format(mean))
    print("min =", "{:e}".format(min))

    return (ratio * mean) + stdev() * 1.4


def slow_step(processors, num_slow):
    """
    Steps the slow processors through running until the one with the least amount of time remaining is finished with its current process.
    """
    current_slows = []
    for i in range(num_slow):
        current_slows.append(processors[i].time_current)

    mini = min(current_slows)

    for i in range(num_slow):
        processors[i].time_current -= mini


def fast_step(processors, num_slow, num_fast):
    """
    Steps the fast processors through running until the one with the least amount of time remaining is finished with its current process.
    """
    current_fasts = []
    for i in range(num_fast):
        current_fasts.append(processors[i + num_slow].time_current)

    mini = min(current_fasts)

    for i in range(num_fast):
        processors[i + num_slow].time_current -= mini


def print_results(
    processors, processor_count, wait, turnaround, wait_times, turnaround_times
):
    print()
    for i in range(len(processors)):
        print("Processor ", i, ":")
        print("Time Elapsed: ", "{:e}".format(processors[i].time_elapsed))
        print("Processor ran: ", processor_count[i], " times.")
        print("Mean Wait: ", "{:e}".format(wait[i] / processor_count[i]))
        print("Mean Turnaround: ", "{:e}".format(turnaround[i] / processor_count[i]))
        print("")

    print("Overall Mean Wait: ", "{:e}".format(mean(wait_times)))
    print("Overall Mean Turnaround: ", "{:e}".format(mean(turnaround_times)))


def FIFO(fname, num_slow, num_fast):

    # Creates proccessors for assigned task, adding the slow ones, then the fast ones to create a bigLITTLE architecture
    processors = []
    for i in range(num_slow):
        processors.append(processor(2))

    for i in range(num_fast):
        processors.append(processor(4))

    # Creates a list of the processes from .csv file in order they are given
    processes = unsorted_processes(fname)

    # Sets threshold
    threshold = set_threshold(processes, num_slow, num_fast)
    print("Threshold set at: ", "{:e}".format(threshold))

    # Sets indices to iterate through proccessor list
    slow_index = 0
    fast_index = num_slow

    # Creates lists to track wait times and turnaround times
    wait_times = []
    turnaround_times = []

    # Creates and initiates lists to track how many times each processor ran and the total wait and turnaround times of each processor
    processor_count = []
    wait = []
    turnaround = []
    for i in range(len(processors)):
        processor_count.append(0)
        wait.append(0)
        turnaround.append(0)

    for i in range(len(processes)):
        burst_time = int(processes[i][1])

        #  Control for proccesses assigned to slow processors
        if burst_time < threshold:

            # find the next available slow processor
            while processors[slow_index].time_current != 0:
                slow_index += 1
                if slow_index == num_slow:
                    slow_index -= num_slow

            # Adds burst time to the selected processor's job queue
            processors[slow_index].time_current += burst_time

            # Steps forward to simulate the passage of time so that one slow processor will be available
            slow_step(processors, num_slow)

            # Adds wait time to list of all wait times and to the total wait time for the selected processor
            wait_times.append(processors[slow_index].time_elapsed)
            wait[slow_index] += processors[slow_index].time_elapsed

            # Adds burst time of current process to selected processor's elapsed time
            processors[slow_index].time_elapsed += burst_time

            # Adds turnaround time to list of all turnaround times and to the total turnaround time for the selected processor
            turnaround_times.append(processors[slow_index].time_elapsed)
            turnaround[slow_index] += processors[slow_index].time_elapsed

            # Increments the amount of times the processor ran
            processor_count[slow_index] += 1

        # Control for proccesses assigned to fast processors
        else:

            # Find next available fast processor
            while processors[fast_index].time_current != 0:
                fast_index += 1
                if fast_index == (num_slow + num_fast):
                    fast_index -= num_fast

            # Adds burst time to the selected processor's job queue
            processors[fast_index].time_current += burst_time

            # Steps forward to simulate the passage of time so that one slow processor will be available
            fast_step(processors, num_slow, num_fast)

            # Adds wait time to list of all wait times and to the total wait time for the selected processor
            wait_times.append(processors[fast_index].time_elapsed)
            wait[fast_index] += processors[fast_index].time_elapsed

            # Adds half the burst time of current process to selected processor's elapsed time
            # These proccessors run at twice the speed of the slower ones
            processors[fast_index].time_elapsed += burst_time / 2

            # Adds turnaround time to list of all turnaround times and to the total turnaround time for the selected processor
            turnaround_times.append(processors[fast_index].time_elapsed)
            turnaround[fast_index] += processors[fast_index].time_elapsed

            # Increments the amount of times the processor ran
            processor_count[fast_index] += 1

    # Print processor results
    print_results(
        processors, processor_count, wait, turnaround, wait_times, turnaround_times
    )


def SJF(fname, num_slow, num_fast):
    # Creates proccessors for assigned task, adding the slow ones, then the fast ones to create a bigLITTLE architecture
    processors = []
    for i in range(num_slow):
        processors.append(processor(2))

    for i in range(num_fast):
        processors.append(processor(4))

    # Creates a list of the processes from .csv file in sorted order to accomodate SJF
    processes = sorted_processes(fname, 1)

    # print(processes)

    # Sets threshold
    threshold = set_threshold(processes, num_slow, num_fast)
    print("Threshold set at: ", "{:e}".format(threshold))

    # Sets indices to iterate through proccessor list
    slow_index = 0
    fast_index = num_slow

    # Creates lists to track wait times and turnaround times
    wait_times = []
    turnaround_times = []

    # Creates and initiates lists to track how many times each processor ran and the total wait and turnaround times of each processor
    processor_count = []
    wait = []
    turnaround = []
    for i in range(len(processors)):
        processor_count.append(0)
        wait.append(0)
        turnaround.append(0)

    for i in range(len(processes)):
        burst_time = int(processes[i][1])

        #  Control for proccesses assigned to slow processors
        if burst_time < threshold:

            # find the next available slow processor
            while processors[slow_index].time_current != 0:
                slow_index += 1
                if slow_index == num_slow:
                    slow_index -= num_slow

            # Adds burst time to the selected processor's job queue
            processors[slow_index].time_current += burst_time

            # Steps forward to simulate the passage of time so that one slow processor will be available
            slow_step(processors, num_slow)

            # Adds wait time to list of all wait times and to the total wait time for the selected processor
            wait_times.append(processors[slow_index].time_elapsed)
            wait[slow_index] += processors[slow_index].time_elapsed

            # Adds burst time of current process to selected processor's elapsed time
            processors[slow_index].time_elapsed += burst_time

            # Adds turnaround time to list of all turnaround times and to the total turnaround time for the selected processor
            turnaround_times.append(processors[slow_index].time_elapsed)
            turnaround[slow_index] += processors[slow_index].time_elapsed

            # Increments the amount of times the processor ran
            processor_count[slow_index] += 1

        # Control for proccesses assigned to fast processors
        else:

            # Find next available fast processor
            while processors[fast_index].time_current != 0:
                fast_index += 1
                if fast_index == (num_slow + num_fast):
                    fast_index -= num_fast

            # Adds burst time to the selected processor's job queue
            processors[fast_index].time_current += burst_time

            # Steps forward to simulate the passage of time so that one slow processor will be available
            fast_step(processors, num_slow, num_fast)

            # Adds wait time to list of all wait times and to the total wait time for the selected processor
            wait_times.append(processors[fast_index].time_elapsed)
            wait[fast_index] += processors[fast_index].time_elapsed

            # Adds half the burst time of current process to selected processor's elapsed time
            # These proccessors run at twice the speed of the slower ones
            processors[fast_index].time_elapsed += burst_time / 2

            # Adds turnaround time to list of all turnaround times and to the total turnaround time for the selected processor
            turnaround_times.append(processors[fast_index].time_elapsed)
            turnaround[fast_index] += processors[fast_index].time_elapsed

            # Increments the amount of times the processor ran
            processor_count[fast_index] += 1

    # Print processor results
    print_results(
        processors, processor_count, wait, turnaround, wait_times, turnaround_times
    )


def RR(fname, num_slow, num_fast):
    
    return

FIFO("./processes.csv", 3, 3)
SJF("./processes.csv", 3, 3)
