from project_tools import unsorted_processes, print_results, Processor
import random


def run(fname):
    """
    Schedules with an adapted SJF approach to incorporate random arrival of processes
    """

    # Creates proccessors for assigned task with uniform speed.
    processors = []
    for i in range(6):
        processors.append(Processor(1, 16))

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

    def step(processors, step_amnt):

        for i in range(len(processors)):
            processors[i].time_current -= step_amnt
            if processors[i].time_current < 0:
                processors[i].time_current = 0

        nonlocal total_time_elapsed
        total_time_elapsed += step_amnt
        # print("TTE in method after step: ", total_time_elapsed)

    # Creates a list to keep track of processes that have arrived, but have not been run yet
    arrived_queue = []

    # Will keep track of which processor to choose.
    pindex = 0

    def find_min_time():
        times_left = []
        for j in range(len(processors)):
            times_left.append(processors[j].time_current)

        return min(times_left)

    def find_max_time():
        times_left = []
        for j in range(len(processors)):
            times_left.append(processors[j].time_elapsed)

        return max(times_left) + gap_time

    # Creates lists to track wait times and turnaround times
    wait_times = []
    turnaround_times = []

    # Keeps track of time that processes are not actively running a process
    gap_time = 0

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
        while find_max_time() < arrival_time:
            print("Max Time(while max < arrival", find_max_time())

            # Defference between when the process will arrive and current time
            time_diff = arrival_time - find_max_time()

            # If nothing in the queue, just moves time forwards until this process arives
            if not arrived_queue:
                gap_time += time_diff
                step(processors, time_diff)
                # print("TTE after step out of method (no queue): ", find_max_time())

            # If processes are in the queue
            else:
                min_time = find_min_time()

                # If this min time is greater than time_diff
                if time_diff < min_time:
                    # Steps time forward until this processor arrives
                    step(processors, time_diff)
                    # print(
                    #     "TTE after step out of method (timediff < min): ",
                    #     find_max_time(),
                    # )

                # If there is less time left for a processor to finish than for this process to arrive
                else:
                    # Steps time forward until one processor finishes with its current process
                    step(processors, min_time)
                    # print(
                    #     "TTE after step out of method (timediff >= min): ",
                    #     find_max_time(),
                    # )

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
                    # print("Arrival Time: %d    TTE: %d   Wait Time: %d" % (aarrival_time, find_max_time(), processor.))

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

    # After all processes have been added to queue, step to free up the closest proccessor to being done
    step(processors, find_min_time())
    # print(
    #     "TTE after step out of method (prior to starting remainder): ",
    #     find_max_time(),
    # )

    # Processes all remaining processes in arrived queue
    for i in range(len(arrived_queue)):
        burst_time = int(arrived_queue[i][1])
        arrival_time = int(arrived_queue[i][3])

        # Finds next available processor
        while processors[pindex].time_current != 0:
            pindex += 1
            if pindex == len(processors):
                pindex = 0

        # Adds burst time to the selected processor's job queue
        processors[pindex].time_current += burst_time

        # Steps forward until first processor is finished
        step(processors, find_min_time())
        # print("TTE after step out of method (in remainder): ", find_max_time())

        # Adds wait time to list of all wait times and to the total wait time for the selected processor
        wait_times.append(processors[pindex].time_elapsed - arrival_time)
        wait[pindex] += processors[pindex].time_elapsed - arrival_time

        # Adds burst time of current process to selected processor's elapsed time
        processors[pindex].time_elapsed += burst_time

        # Adds turnaround time to list of all turnaround times and to the total turnaround time of the selected processor
        turnaround_times.append((processors[pindex].time_elapsed) - arrival_time)
        turnaround[pindex] += processors[pindex].time_elapsed - arrival_time

        # Increments the number of times the processor ran
        processor_count[pindex] += 1

    # Print processor results
    print("\n\nQ4 Results")

    print("Wait Times: ", wait_times)
    print("TA Times: ", turnaround_times)

    # print("TTE afterwards: ", "{:e}".format(find_max_time()))
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
