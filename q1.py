from concurrent.futures import process
from project_tools import sorted_processes, unsorted_processes


def fifo(fname):
    processes = unsorted_processes(fname)
    for i in range(len(processes)):
        print(processes[i][1])
    wait_times = []
    for i in range(250):
        for j in range(i):
            wait_time = int(processes[j][1])
        wait_times.append(wait_time)
        wait_time = len(processes)
    print("Average Wait Time for FIFO: " + str(sum(wait_times) / len(wait_times)))
    turnaround_times = []
    turnaround_time = int(processes[0][1])
    for i in range(250):
        for j in range(i):
            turnaround_time += int(processes[j + 1][1])
        turnaround_times.append(turnaround_time)
        turnaround_time = int(processes[0][1])
    print(
        "Average Turnaround Time for FIFO: "
        + str(sum(turnaround_times) / len(turnaround_times))
    )


def sjf(fname):
    processes = sorted_processes(fname, 1)
    for i in range(len(processes)):
        print(processes[i][1])
    wait_times = []
    wait_time = 0
    for i in range(250):
        for j in range(i):
            wait_time += int(processes[j][1])
        wait_times.append(wait_time)
        wait_time = 0
    print("Average Wait Time for SJF: " + str(sum(wait_times) / len(wait_times)))
    turnaround_times = []
    turnaround_time = int(processes[0][1])
    for i in range(250):
        for j in range(i):
            turnaround_time += int(processes[j + 1][1])
        turnaround_times.append(turnaround_time)
        turnaround_time = int(processes[0][1])
    print(
        "Average Turnaround Time for SJF: "
        + str(sum(turnaround_times) / len(turnaround_times))
    )


def rr(processes, time_quantum):
    print(processes)
    count = 0
    while sum(processes) > 0:
        for i in range(250):
            if processes[i] - time_quantum > 0:
                processes[i] = processes[i] - time_quantum
            else:
                processes[i] = 0
        count = count + 1
        print("Iteration " + str(count) + ": " + str(processes))


if __name__ == "__main__":
    file = "./processes.csv"
    time_quantum = 1 * 10**9
    fifo(file)
    sjf(file)
    # rr(processes, time_quantum)
