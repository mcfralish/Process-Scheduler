from project_tools import sorted_processes, print_results, processor


def step(processors, total_time_elapsed, step_amnt):

    for i in range(len(processors)):
        processors[i].time_current -= step_amnt
        if processor[i].time_current < 0:
            processor[i].time_current = 0

    total_time_elapsed += step_amnt


def SJF(fname):

    processors = []
    total_time_elapsed = 0

    for i in range(6):
        processors.append(processor(1))

    processes = sorted_processes(fname, 3)
    arrived_queue = []

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

    for i in range(len(processes)):

        arrival_time = int(processes[i][3])

        while total_time_elapsed < arrival_time:

            time_diff = arrival_time - total_time_elapsed
            if not arrived_queue:
                step(processors, total_time_elapsed, time_diff)

            else:
                times_left = []
                for j in range(len(processors)):
                    times_left.append(processors[j].time_current)

                min_time_left = min(times_left)

                if time_diff < min_time_left:
                    step(processors, total_time_elapsed, time_diff)

                else:
                    step(processors, total_time_elapsed, min_time_left)

                    while processors[pindex].time_current != 0:
                        pindex += 1
                        if pindex == len(processors):
                            pindex = 0

                    arrived_queue.sort(key=lambda x: x[1])
                    adding = arrived_queue.pop(0)
                    burst_time = int(adding[1])

                    processors[pindex].time_current += burst_time

                    wait_times.append(processors[pindex].time_elapsed)
                    wait[pindex] += processors[pindex].time_elapsed

                    processors[pindex].time_elapsed += burst_time

                    turnaround_times.append(processors[pindex].time_elapsed)
                    turnaround[pindex] += processors[pindex].time_elapsed

                    processor_count[pindex] += 1

        arrived_queue.append(processes[i])

    # Print processor results
    print_results(
        processors, processor_count, wait, turnaround, wait_times, turnaround_times
    )
