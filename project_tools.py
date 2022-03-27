import csv
import random
from statistics import mean
from math import sqrt


class Processor:
    def __init__(self, speed, memory):
        self.speed = speed
        self.time_elapsed = 0
        self.time_current = 0
        self.memory = memory


def generate(k, m, n, a, b, c, d):
    """
    Will generate a list of process tuples with the burst ranging between 10 * 10^n - 10 * 10^m and the memory between a - b
    """
    proccesses = []

    def burst_time():
        return random.randint(pow(10, m + 1), pow(10, n + 1))

    def mem():
        return random.randint(a, b)

    def arrival():
        return random.randint(c, d)

    for i in range(k):
        new_process = (i, burst_time(), mem(), arrival())
        proccesses.append(new_process)

    return proccesses


def write_to_file(processes, header, fname):
    """
    Writes a list of proccesses to a .csv file
    """
    f = open(fname, "w")
    w = csv.writer(f)

    w.writerow(header)
    for i in range(len(processes)):
        w.writerow(processes[i])

    f.close()


def sorted_processes(fname, column_index):
    """
    For use with .csv file to sort by column value. Returns a sorted list of lists
    """
    reader = csv.reader(open(fname), delimiter=",")
    sortedlist = sorted(reader, key=lambda row: row[column_index])
    sortedlist.pop(-1)
    return sortedlist


def unsorted_processes(fname):
    """
    For use with .csv file. Returns an unsorted list of lists.
    """
    with open(fname) as f:
        reader = csv.reader(f, delimiter=",")
        unsortedlist = list(reader)
        unsortedlist.pop(0)
        return unsortedlist


def slow_step(processors, slowps):
    """
    Steps the slow processors through running until the one with the least amount of time remaining is finished with its current process.
    """
    current_slows = []
    for i in range(slowps):
        current_slows.append(processors[i].time_current)

    mini = min(current_slows)

    for i in range(slowps):
        processors[i].time_current -= mini


def fast_step(processors, slowps, fastps):
    """
    Steps the fast processors through running until the one with the least amount of time remaining is finished with its current process.
    """
    current_fasts = []
    for i in range(fastps):
        current_fasts.append(processors[i + slowps].time_current)

    mini = min(current_fasts)

    for i in range(fastps):
        processors[i + slowps].time_current -= mini


def set_threshold(processes, slowps, fastps, reverse):
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

    ratio = (slowps * 2) / (slowps * 2 + fastps * 4)

    if reverse:
        ratio = 1 - ratio

    mean = total_burst / len(processes)

    def stdev():
        sd = 0
        for i in range(len(processes)):
            sd += (int(processes[i][1]) - mean) ** 2

        sd = sd / len(processes)
        sd = sqrt(sd)
        return sd

    return (ratio * mean) + stdev() * 1.5


def print_results(
    processors, processor_count, wait, turnaround, wait_times, turnaround_times, RR
):
    """
    Prints results for question 2.
    """
    print()
    for i in range(len(processors)):
        print("Processor ", i, ":")
        print("Time Elapsed: ", "{:e}".format(processors[i].time_elapsed))
        print("Processor ran: ", processor_count[i], " times.")
        if not RR:
            print("Mean Wait: ", "{:e}".format(wait[i] / processor_count[i]))
            print(
                "Mean Turnaround: ", "{:e}".format(turnaround[i] / processor_count[i])
            )
        print("")

    print("Overall Mean Wait: ", "{:e}".format(mean(wait_times)))
    print("Overall Mean Turnaround: ", "{:e}".format(mean(turnaround_times)))


if __name__ == "__main__":
    processes = generate(250, 6, 12, 1, 16000, 0, 1 * 10**14)
    header = ["PID", "Burst Time", "Memory in MB", "Arrival Time"]
    write_to_file(processes, header, "./processes.csv")
