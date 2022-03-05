import csv
import random


def generate(k, burst_pow_min, burst_pow_max, mem_min, mem_max):
    """
    Will generate a list of process tuples with the burst ranging between 10 * 10^n - 10 * 10^m and the memory between given parameters
    """
    proccesses = []

    def burst_time():
        return random.randint(pow(10, burst_pow_min + 1), pow(10, burst_pow_max + 1))

    def mem():
        return random.randint(mem_min, mem_max)

    for i in range(k):
        new_process = (i, burst_time(), mem())
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


if __name__ == "__main__":
    processes = generate(250, 6, 12, 1, 16000)
    header = ["PID", "Burst Time", "Memory in MB"]
    write_to_file(processes, header, "./processes.csv")
