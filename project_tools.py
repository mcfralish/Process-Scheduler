import csv
import random
from statistics import mean


class processor:
    def __init__(self, speed):
        self.speed = speed
        self.time_elapsed = 0
        self.time_current = 0


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


def print_results(
    processors, processor_count, wait, turnaround, wait_times, turnaround_times
):
    """
    Prints results for question 2.
    """
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


if __name__ == "__main__":
    processes = generate(250, 6, 12, 1, 16000, 0, 1 * 10**14)
    header = ["PID", "Burst Time", "Memory in MB", "Arrival Time"]
    write_to_file(processes, header, "./processes.csv")
