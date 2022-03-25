from project_tools import unsorted_processes, print_results, processor
import random


def step(processors, total_time_elapsed, step_amnt):

    for i in range(len(processors)):
        processors[i].time_current -= step_amnt
        if processor[i].time_current < 0:
            processor[i].time_current = 0

    total_time_elapsed += step_amnt


def SJF(fname):
    """
    Schedules with an adapted SJF approach to incorporate random arrival of processes
    """

    # Creates proccessors for assigned task with uniform speed.
    processors = []
    for i in range(6):
        processors.append(processor(1))

    # Creates a list of the processes from .csv file sorted by arrival time
    processes = unsorted_processes(fname)

    # If .csv does not already include arrival times, creates them
    if len(processes[0]) < 4:
        for i in range(len(processes)):
            processes[i].append(random.randint(0, 1 * 10**14))

    # Sorts processes based on arrival time
    processes.sort(key=lambda x: x[3])

    # Keeps track of time since we began running processors to determine whether a process has arrived yet.
    total_time_elapsed = 0

    # Creates a list to keep track of processes that have arrived, but have not been run yet
    arrived_queue = []

    # Will keep track of which processor to choose.
    pindex = 0

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

    # Does the scheduling
    for i in range(len(processes)):

        # Sets arrival time for i'th proccess
        arrival_time = int(processes[i][3])

        # Processes while i'th process has not yet arrived
        while total_time_elapsed < arrival_time:

            # Defference between when the process will arrive and current time
            time_diff = arrival_time - total_time_elapsed

            # If nothing in the queue, just moves time forwards until this process arives
            if not arrived_queue:
                step(processors, total_time_elapsed, time_diff)

            # If processes are in the queue
            else:

                # Puts all the current times for each processor in a list
                times_left = []
                for j in range(len(processors)):
                    times_left.append(processors[j].time_current)

                # Finds the minimum remaining time on a processor
                min_time_left = min(times_left)

                # If this min time is greater than time_diff
                if time_diff < min_time_left:
                    # Steps time forward until this processor arrives
                    step(processors, total_time_elapsed, time_diff)

                # If there is less time left for a processor to finish than for this process to arrive
                else:
                    # Steps time forward until one processor finishes with its current process
                    step(processors, total_time_elapsed, min_time_left)

                    # Finds next available processor
                    while processors[pindex].time_current != 0:
                        pindex += 1
                        if pindex == len(processors):
                            pindex = 0

                    # Sorts the arrived queue by burst time to accomodate SJF
                    arrived_queue.sort(key=lambda x: x[1])

                    # Removes the lowest burst time processor from the queue and saves it
                    adding = arrived_queue.pop(0)
                    aburst_time = int(adding[1])
                    aarrival_time = int(adding[3])

                    # Adds burst time to time current of the the selected processor
                    processors[pindex].time_current += aburst_time

                    # Adds wait time to list of all wait times and to the total wait time for the selected processor
                    wait_times.append((processors[pindex].time_elapsed) - aarrival_time)
                    wait[pindex] += processors[pindex].time_elapsed - aarrival_time

                    # Adds burst time of current process to selected processor's elapsed time
                    processors[pindex].time_elapsed += aburst_time

                    # Adds turnaround time to list of all turnaround times and to the total turnaround time for the selected processor
                    turnaround_times.append(
                        processors[pindex].time_elapsed - aarrival_time
                    )
                    turnaround[pindex] += (
                        processors[pindex].time_elapsed - aarrival_time
                    )

                    # Increments the amount of times the processor ran
                    processor_count[pindex] += 1

        # After all processes that will finish prior to the process arriving
        arrived_queue.append(processes[i])

    for i in range(len(arrived_queue)):
        burst_time = int(processes[i][1])

        times_left = []
        for j in range(len(processors)):
            times_left.append(processors[i].current_time)

        while processors[pindex]

    # Print processor results
    print_results(
        processors, processor_count, wait, turnaround, wait_times, turnaround_times
    )
