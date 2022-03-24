import random


processes = []
for i in range(250):
    process = random.randint(1, 16000)
    processes.append(process)

time_quantum = 8000


def fifo(processes):
    print(processes)
    wait_times = []
    wait_time = 0
    for i in range(250):
        for j in range(i):
            wait_time += processes[j]
        wait_times.append(wait_time)
        wait_time = 0
    print("Average Wait Time for FIFO: " + str(sum(wait_times) / len(wait_times)))
    turnaround_times = []
    turnaround_time = processes[0]
    for i in range(250):
        for j in range(i):
            turnaround_time += processes[j + 1]
        turnaround_times.append(turnaround_time)
        turnaround_time = processes[0]
    print(
        "Average Turnaround Time for FIFO: "
        + str(sum(turnaround_times) / len(turnaround_times))
    )


def sjf(processes):
    processes.sort()
    print(processes)
    wait_times = []
    wait_time = 0
    for i in range(250):
        for j in range(i):
            wait_time += processes[j]
        wait_times.append(wait_time)
        wait_time = 0
    print("Average Wait Time for SJF: " + str(sum(wait_times) / len(wait_times)))
    turnaround_times = []
    turnaround_time = processes[0]
    for i in range(250):
        for j in range(i):
            turnaround_time += processes[j + 1]
        turnaround_times.append(turnaround_time)
        turnaround_time = processes[0]
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


# fifo(processes)
# sjf(processes)
rr(processes, time_quantum)
