import csv
from functools import cmp_to_key
from project_tools import (
    sorted_processes,
    print_results,
    slow_step,
    fast_step,
    set_threshold,
    Processor,
)


def SJF(fname):
    lowPower_speed = 2
    highPower_speed = 4
    highpower_cpus = 3
    lowPower_cpus = 3
    lowPower_mem = 8000
    highPower_mem = 16000

    processors = []
    for i in range(lowPower_cpus):
        processors.append(Processor(lowPower_speed, lowPower_mem))

    for i in range(highpower_cpus):
        processors.append(Processor(highPower_speed, highPower_mem))

    processes = sorted_processes(fname, 1)

    threshold = set_threshold(processes, lowPower_cpus, highpower_cpus, reverse=True)
    low_index = 0
    high_index = lowPower_cpus

    wait_times = []
    turnaround_times = []

    processor_count = []
    wait = []
    turnaround = []
    for i in range(len(processors)):
        processor_count.append(0)
        wait.append(0)
        turnaround.append(0)

    for process in processes:
        """
        Process is assigned to higher power CPU if it cannot fit in the lower power CPU
        """
        burst_time = process[1]
        memory_footprint = process[2]

        if memory_footprint > lowPower_mem:

            # Find next available fast processor
            while processors[high_index].time_current != 0:
                high_index += 1
                if high_index == (lowPower_cpus + highpower_cpus):
                    high_index -= highpower_cpus

            # Adds burst time to the selected processor's job queue
            processors[high_index].time_current += burst_time

            # Steps forward to simulate the passage of time so that one slow processor will be available
            fast_step(processors, lowPower_cpus, highpower_cpus)

            # Adds wait time to list of all wait times and to the total wait time for the selected processor
            wait_times.append(processors[high_index].time_elapsed)
            wait[high_index] += processors[high_index].time_elapsed

            # Adds half the burst time of current process to selected processor's elapsed time
            # These proccessors run at twice the speed of the slower ones
            processors[high_index].time_elapsed += burst_time / 2

            # Adds turnaround time to list of all turnaround times and to the total turnaround time for the selected processor
            turnaround_times.append(processors[high_index].time_elapsed)
            turnaround[high_index] += processors[high_index].time_elapsed

            # Increments the amount of times the processor ran
            processor_count[high_index] += 1

        elif burst_time > threshold:

            # Find next available fast processor
            while processors[high_index].time_current != 0:
                high_index += 1
                if high_index == (lowPower_cpus + highpower_cpus):
                    high_index -= highpower_cpus

            # Adds burst time to the selected processor's job queue
            processors[high_index].time_current += burst_time

            # Steps forward to simulate the passage of time so that one slow processor will be available
            fast_step(processors, lowPower_cpus, highpower_cpus)

            # Adds wait time to list of all wait times and to the total wait time for the selected processor
            wait_times.append(processors[high_index].time_elapsed)
            wait[high_index] += processors[high_index].time_elapsed

            # Adds half the burst time of current process to selected processor's elapsed time
            # These proccessors run at twice the speed of the slower ones
            processors[high_index].time_elapsed += burst_time / 2

            # Adds turnaround time to list of all turnaround times and to the total turnaround time for the selected processor
            turnaround_times.append(processors[high_index].time_elapsed)
            turnaround[high_index] += processors[high_index].time_elapsed

            # Increments the amount of times the processor ran
            processor_count[high_index] += 1

        else:
            # find the next available slow processor
            while processors[low_index].time_current != 0:
                low_index += 1
                if low_index == lowPower_cpus:
                    low_index -= lowPower_cpus

            # Adds burst time to the selected processor's job queue
            processors[low_index].time_current += burst_time

            # Steps forward to simulate the passage of time so that one slow processor will be available
            slow_step(processors, low_index)

            # Adds wait time to list of all wait times and to the total wait time for the selected processor
            wait_times.append(processors[low_index].time_elapsed)
            wait[low_index] += processors[low_index].time_elapsed

            # Adds burst time of current process to selected processor's elapsed time
            processors[low_index].time_elapsed += burst_time

            # Adds turnaround time to list of all turnaround times and to the total turnaround time for the selected processor
            turnaround_times.append(processors[low_index].time_elapsed)
            turnaround[low_index] += processors[low_index].time_elapsed

            # Increments the amount of times the processor ran
            processor_count[low_index] += 1

    # Print processor results
    print_results(
        processors, processor_count, wait, turnaround, wait_times, turnaround_times
    )
