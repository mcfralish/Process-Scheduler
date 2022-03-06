from audioop import avg
from statistics import mean
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

    def set_threshold():
        sum = 0
        for i in range(len(processes)):
            sum += int(processes[i][1])

        mean = sum / len(processes)

        return mean - (mean / 6)

    # threshold = pow(10, 13) - 5000000000000

    threshold = set_threshold()

    slow_index = 0
    fast_index = num_slow

    wait_times = []
    turnaround_times = []
    processor_count = [0, 0, 0, 0, 0, 0, 0]
    wait = [0, 0, 0, 0, 0, 0, 0]
    turnaround = [0, 0, 0, 0, 0, 0]

    for i in range(len(processes)):
        if int(processes[i][1]) < threshold:
            wait_times.append(processors[slow_index].time_elapsed)
            wait[slow_index] += processors[slow_index].time_elapsed
            processors[slow_index].time_elapsed += int(processes[i][1])
            turnaround_times.append(processors[slow_index].time_elapsed)
            turnaround[slow_index] += processors[slow_index].time_elapsed
            processor_count[slow_index] += 1
            slow_index += 1
            if slow_index == num_slow:
                slow_index -= num_slow

        else:
            wait_times.append(processors[fast_index].time_elapsed)
            wait[fast_index] += processors[fast_index].time_elapsed
            processors[fast_index].time_elapsed += int(processes[i][1]) / 2
            turnaround_times.append(processors[fast_index].time_elapsed)
            turnaround[fast_index] += processors[fast_index].time_elapsed
            processor_count[fast_index] += 1
            fast_index += 1
            if fast_index == (num_slow + num_fast):
                fast_index -= num_fast

    for i in range(len(processors)):
        print("Processor ", i, ":")
        print("Time Elapsed: ", "{:e}".format(processors[i].time_elapsed))
        print("Processor ran: ", processor_count[i], " times.")
        print("Mean Wait: ", "{:e}".format(wait[i] / processor_count[i]))
        print("Mean Turnaround: ", "{:e}".format(turnaround[i] / processor_count[i]))
        print("")

    print("Overall Mean Wait: ", "{:e}".format(mean(wait_times)))
    print("Overall Mean Turnaround: ", "{:e}".format(mean(turnaround_times)))

    # print(wait_times)
    # print(turnaround_times)


FIFO("./processes.csv", 3, 3)
