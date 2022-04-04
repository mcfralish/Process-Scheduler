from project_tools import (
    sorted_processes,
    unsorted_processes,
    slow_step,
    print_results,
    Processor,
)


def fifo(fname):

    processes = unsorted_processes(fname)
    num_processors = 6
    # Creates proccessors for assigned task, adding the slow ones, then the fast ones to create a bigLITTLE architecture
    processors = []
    for i in range(num_processors):
        processors.append(Processor(1, 16))

    print("Processors length: ", len(processors))

    # Sets index that will be used to find next available processor
    pindex = 0

    # Creates lists to track wait times and turnaround times
    wait_times = []
    turnaround_times = []

    # Creates and initiates lists to track how many times each processor ran and the total wait and turnaround times of each processor
    processor_count = []
    wait = []
    turnaround = []
    for i in range(num_processors):
        processor_count.append(0)
        wait.append(0)
        turnaround.append(0)

    for process in processes:
        burst_time = int(process[1])

        # find the next available slow processor
        while processors[pindex].time_current != 0:
            pindex += 1
            if pindex == num_processors:
                pindex -= num_processors

        # Adds burst time to the selected processor's job queue
        processors[pindex].time_current += burst_time

        # Steps forward to simulate the passage of time so that one slow processor will be available
        slow_step(processors, num_processors)

        # Adds wait time to list of all wait times and to the total wait time for the selected processor
        wait_times.append(processors[pindex].time_elapsed)
        wait[pindex] += processors[pindex].time_elapsed

        # Adds burst time of current process to selected processor's elapsed time
        processors[pindex].time_elapsed += burst_time

        # Adds turnaround time to list of all turnaround times and to the total turnaround time for the selected processor
        turnaround_times.append(processors[pindex].time_elapsed)
        turnaround[pindex] += processors[pindex].time_elapsed

        # Increments the amount of times the processor ran
        processor_count[pindex] += 1

    print("Q1 FIFO Results")
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


def sjf(fname):

    processes = sorted_processes(fname, 1)
    num_processors = 6
    # Creates proccessors for assigned task, adding the slow ones, then the fast ones to create a bigLITTLE architecture
    processors = []
    for i in range(num_processors):
        processors.append(Processor(1, 16))

    # Sets index that will be used to find next available processor
    pindex = 0

    # Creates lists to track wait times and turnaround times
    wait_times = []
    turnaround_times = []

    # Creates and initiates lists to track how many times each processor ran and the total wait and turnaround times of each processor
    processor_count = []
    wait = []
    turnaround = []
    for i in range(num_processors):
        processor_count.append(0)
        wait.append(0)
        turnaround.append(0)

    for process in processes:
        burst_time = int(process[1])

        # find the next available slow processor
        while processors[pindex].time_current != 0:
            pindex += 1
            if pindex == num_processors:
                pindex -= num_processors

        # Adds burst time to the selected processor's job queue
        processors[pindex].time_current += burst_time

        # Steps forward to simulate the passage of time so that one slow processor will be available
        slow_step(processors, num_processors)

        # Adds wait time to list of all wait times and to the total wait time for the selected processor
        wait_times.append(processors[pindex].time_elapsed)
        wait[pindex] += processors[pindex].time_elapsed

        # Adds burst time of current process to selected processor's elapsed time
        processors[pindex].time_elapsed += burst_time

        # Adds turnaround time to list of all turnaround times and to the total turnaround time for the selected processor
        turnaround_times.append(processors[pindex].time_elapsed)
        turnaround[pindex] += processors[pindex].time_elapsed

        # Increments the amount of times the processor ran
        processor_count[pindex] += 1

    print("Q1 SJF Results")
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


def rr(fname, quantum):

    num_processors = 6
    # Creates proccessors for assigned task, adding the slow ones, then the fast ones to create a bigLITTLE architecture
    processors = []
    for i in range(num_processors):
        processors.append(Processor(1, 16))

    # Creates a list of the processes from .csv file in order they are given
    processes = unsorted_processes(fname)

    # Sets index to iterate through processor list
    pindex = 0

    # Creates lists to track wait times and turnaround times
    wait_times = []
    turnaround_times = []
    for i in range(len(processes)):
        wait_times.append(0)
        turnaround_times.append(0)

    # Creates and initiates lists to track how many times each processor ran and the total wait and turnaround times of each processor
    processor_count = []
    wait = []
    turnaround = []
    for i in range(num_processors):
        processor_count.append(0)
        wait.append(0)
        turnaround.append(0)

    i = 0
    context_switches = 0
    allEmpty = False
    firstEmpty = None
    pindex = 0
    remaining_time = []

    for process in processes:
        remaining_time.append(int(process[1]))

    while not allEmpty:
        # loops i when it goes over the number of processes to start back at the beginning
        if i == len(processes):
            i = 0

        burst_time = int(processes[i][1])
        remaining_burst = remaining_time[i]

        # Determines if every process has been run to 0 remaining burst time
        # then terminates the loop
        if (remaining_burst == 0) and (i == firstEmpty):
            allEmpty = True

        # Determines if this is the first time it has detected a zero'd burst time
        # then increments i and starts loop again
        elif (remaining_burst == 0) and firstEmpty is None:
            firstEmpty = i
            i += 1

        # Will trigger if current process has a remaining burst time of 0
        # and the one before was also 0.
        # Increments i and restarts
        elif remaining_burst == 0:
            i += 1

        # Triggers if all checks prior fail and the burst time is an integer greater than 0
        # Will execute a subtraction of the given
        else:

            # Will stop tracking firstEmpty if it is discovered that one is not empty
            firstEmpty = None

            # find the next available slow processor
            while processors[pindex].time_current != 0:
                pindex += 1
                if pindex == num_processors:
                    pindex -= num_processors

            # Determines if remaining burst time is less than a quantum or not
            if remaining_burst <= quantum:

                # Adds burst time to the selected processor's job queue
                processors[pindex].time_current += remaining_burst

                # Steps forward to simulate the passage of time so that one slow processor will be available
                slow_step(processors, num_processors)

                # Adds burst time of current process to selected processor's elapsed time
                processors[pindex].time_elapsed += remaining_burst

                # Adds wait time to list of all wait times and to the total wait time for the selected processor
                wait_times[i] = processors[pindex].time_elapsed - burst_time
                wait[pindex] += processors[pindex].time_elapsed - burst_time

                # Adds turnaround time to list of all turnaround times and to the total turnaround time for the selected processor
                turnaround_times[i] = processors[pindex].time_elapsed
                turnaround[pindex] += processors[pindex].time_elapsed

                remaining_time[i] = 0

            else:
                # Adds quantum to the selected processor's job queue
                processors[pindex].time_current += quantum

                # Steps forward to simulate the passage of time so that one slow processor will be available
                slow_step(processors, num_processors)

                # Adds quantum of current process to selected processor's elapsed time
                processors[pindex].time_elapsed += quantum

                # Resets the burst time to subtract the quantum
                remaining_time[i] = remaining_burst - quantum

            # Increments the amount of times the processor ran
            processor_count[pindex] += 1

            i += 1
            context_switches += 1

    # Print processor results
    print("\n\nQ1 RR Results")
    print_results(
        processors,
        processor_count,
        wait,
        turnaround,
        wait_times,
        turnaround_times,
        True,
    )
    print("Context Switches: ", context_switches)

    give = {
        "processors": processors,
        "processor_count": processor_count,
        "wait": wait,
        "turnaround": turnaround,
        "wait_times": wait_times,
        "turnaround_times": turnaround_times,
    }

    return give
