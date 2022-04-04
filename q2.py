from project_tools import (
    sorted_processes,
    unsorted_processes,
    print_results,
    slow_step,
    fast_step,
    set_threshold,
    Processor,
)
from fractions import Fraction


def FIFO(fname, slowps, fastps):
    """
    Schedules according to big.LITTLE architecture with FIFO (First in First out)
    """

    # Creates proccessors for assigned task, adding the slow ones, then the fast ones to create a bigLITTLE architecture
    processors = []
    for i in range(slowps):
        processors.append(Processor(2, 16))

    for i in range(fastps):
        processors.append(Processor(4, 16))

    # Creates a list of the processes from .csv file in order they are given
    processes = unsorted_processes(fname)

    # Sets threshold
    threshold = set_threshold(processes, slowps, fastps, reverse=False)

    # Sets indices to iterate through proccessor list
    slow_index = 0
    fast_index = slowps

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

    for process in processes:
        burst_time = int(process[1])

        #  Control for proccesses assigned to slow processors
        if burst_time < threshold:

            # find the next available slow processor
            while processors[slow_index].time_current != 0:
                slow_index += 1
                if slow_index == slowps:
                    slow_index -= slowps

            # Adds burst time to the selected processor's job queue
            processors[slow_index].time_current += burst_time

            # Steps forward to simulate the passage of time so that one slow processor will be available
            slow_step(processors, slowps)

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
                if fast_index == (slowps + fastps):
                    fast_index -= fastps

            # Adds burst time to the selected processor's job queue
            processors[fast_index].time_current += burst_time

            # Steps forward to simulate the passage of time so that one slow processor will be available
            fast_step(processors, slowps, fastps)

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
    print("\n\nQ2 FIFO Results")
    print_results(
        processors,
        processor_count,
        wait,
        turnaround,
        wait_times,
        turnaround_times,
        False,
    )

    give = {
        "processors": processors,
        "processor_count": processor_count,
        "wait": wait,
        "turnaround": turnaround,
        "wait_times": wait_times,
        "turnaround_times": turnaround_times,
    }

    return give


def SJF(fname, slowps, fastps):
    """
    Schedules according to big.LITTLE architecture with SJF (Shortest Job First)
    """
    # Creates proccessors for assigned task, adding the slow ones, then the fast ones to create a bigLITTLE architecture
    processors = []
    for i in range(slowps):
        processors.append(Processor(2, 16))

    for i in range(fastps):
        processors.append(Processor(4, 16))

    # Creates a list of the processes from .csv file in sorted order to accomodate SJF
    processes = sorted_processes(fname, 1)

    # print(processes)

    # Sets threshold
    threshold = set_threshold(processes, slowps, fastps, reverse=False)

    # Sets indices to iterate through proccessor list
    slow_index = 0
    fast_index = slowps

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

    for process in processes:
        burst_time = int(process[1])

        #  Control for proccesses assigned to slow processors
        if burst_time < threshold:

            # find the next available slow processor
            while processors[slow_index].time_current != 0:
                slow_index += 1
                if slow_index == slowps:
                    slow_index -= slowps

            # Adds burst time to the selected processor's job queue
            processors[slow_index].time_current += burst_time

            # Steps forward to simulate the passage of time so that one slow processor will be available
            slow_step(processors, slowps)

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
                if fast_index == (slowps + fastps):
                    fast_index -= fastps

            # Adds burst time to the selected processor's job queue
            processors[fast_index].time_current += burst_time

            # Steps forward to simulate the passage of time so that one slow processor will be available
            fast_step(processors, slowps, fastps)

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
    print("\n\nQ2 SJF Results")
    print_results(
        processors,
        processor_count,
        wait,
        turnaround,
        wait_times,
        turnaround_times,
        False,
    )

    give = {
        "processors": processors,
        "processor_count": processor_count,
        "wait": wait,
        "turnaround": turnaround,
        "wait_times": wait_times,
        "turnaround_times": turnaround_times,
    }

    return give


if __name__ == "__main__":
    quantum = 5 * 10**9
    print("Q2 FIFO Results\n")
    FIFO("./processes.csv", 3, 3)
    print("\n\nQ2 SJF Results\n")
    SJF("./processes.csv", 3, 3)
