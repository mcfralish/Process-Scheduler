from statistics import mean
from project_tools import sorted_processes, unsorted_processes
from math import sqrt


class processor:
    def __init__(self, speed):
        self.speed = speed
        self.time_elapsed = 0
        self.time_current = 0


def FIFO(fname, num_slow, num_fast):

    processors = []
    for i in range(num_slow):
        processors.append(processor(2))

    for i in range(num_fast):
        processors.append(processor(4))

    processes = unsorted_processes(fname)

    def set_threshold():
        """
        Sets threshold proportionate to the amount of work expected from each set of processors. In a system with equal number fast and slow processors, with the slow running at half of the speed of the fast, the slow will be rewsponsible for 1/3 of the work.
        """
        sum = 0
        for i in range(len(processes)):
            sum += int(processes[i][1])

        ratio = (num_slow * 2)/(num_slow * 2 + num_fast * 4)

        mean = sum/len(processes)
        
        def stdev():
            sd = 0
            for i in range(len(processes)):
                sd += (int(processes[i][1]) - mean)**2

            sd = sd/len(processes)
            sd = sqrt(sd)
            print("Stand Dev: ", sd)
            return sd


        print("ratio = ", ratio)
        print("mean = ", "{:e}".format(mean))

        return (ratio * mean) + stdev()

    def slow_step():
        """
        Steps the slow processors through running until the one with the least amount of time remaining is finished with its current process.
        """
        current_slows = []
        for i in range(num_slow):
            current_slows.append(processors[i].time_current)

        mini = min(current_slows)

        for i in range(num_slow):
            processors[i].time_current -= mini

    def fast_step():
        """
        Steps the fast processors through running until the one with the least amount of time remaining is finished with its current process.
        """
        current_fasts = []
        for i in range(num_fast):
            current_fasts.append(processors[i + num_slow].time_current)

        mini = min(current_fasts)

        for i in range(num_fast):
            processors[i + num_slow].time_current -= mini


    threshold = set_threshold()
    print("Threshold set at: ", "{:e}".format(threshold))


    slow_index = 0
    fast_index = num_slow

    wait_times = []
    turnaround_times = []
    processor_count = [0, 0, 0, 0, 0, 0]
    wait = [0, 0, 0, 0, 0, 0]
    turnaround = [0, 0, 0, 0, 0, 0]


    for i in range(len(processes)):
        burst_time = int(processes[i][1])
        # adds process to slow the slow proccessor queue if below set threshold
        if burst_time < threshold:

            # find the next available slow processor
            while processors[slow_index].time_current != 0:
                slow_index += 1
                if slow_index == num_slow:
                    slow_index -= num_slow

            # adds burst time to the selected processors job queue
            processors[slow_index].time_current += burst_time
            slow_step()
            wait_times.append(processors[slow_index].time_elapsed)
            wait[slow_index] += processors[slow_index].time_elapsed
            processors[slow_index].time_elapsed += burst_time
            turnaround_times.append(processors[slow_index].time_elapsed)
            turnaround[slow_index] += processors[slow_index].time_elapsed
            processor_count[slow_index] += 1

        else:
            while processors[fast_index].time_current != 0:
                fast_index += 1
                if fast_index == (num_slow + num_fast):
                    fast_index -= num_fast

            processors[fast_index].time_current =+ burst_time
            fast_step()
            wait_times.append(processors[fast_index].time_elapsed)
            wait[fast_index] += processors[fast_index].time_elapsed
            processors[fast_index].time_elapsed += burst_time / 2
            turnaround_times.append(processors[fast_index].time_elapsed)
            turnaround[fast_index] += processors[fast_index].time_elapsed
            processor_count[fast_index] += 1


    # Print processor results
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

    # print(wait_times)
    # print(turnaround_times)


FIFO("./processes.csv", 3, 3)
