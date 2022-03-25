from concurrent.futures import process
from project_tools import sorted_processes, unsorted_processes


def fifo(fname):
    processes = unsorted_processes(fname)
    p1 = []
    p2 = []
    p3 = []
    p4 = []
    p5 = []
    p6 = []
    wait_times_p1 = []
    wait_time_p1 = 0
    turnaround_times_p1 = []
    turnaround_time_p1 = int(processes[0][1])
    wait_times_p2 = []
    wait_time_p2 = 0
    turnaround_times_p2 = []
    turnaround_time_p2 = int(processes[1][1])
    wait_times_p3 = []
    wait_time_p3 = 0
    turnaround_times_p3 = []
    turnaround_time_p3 = int(processes[2][1])
    wait_times_p4 = []
    wait_time_p4 = 0
    turnaround_times_p4 = []
    turnaround_time_p4 = int(processes[3][1])
    wait_times_p5 = []
    wait_time_p5 = 0
    turnaround_times_p5 = []
    turnaround_time_p5 = int(processes[4][1])
    wait_times_p6 = []
    wait_time_p6 = 0
    turnaround_times_p6 = []
    turnaround_time_p6 = int(processes[5][1])
    for i in range(41):
        p1.append(int(processes[6 * i][1]))
        p2.append(int(processes[6 * i + 1][1]))
        p3.append(int(processes[6 * i + 2][1]))
        p4.append(int(processes[6 * i + 3][1]))
        p5.append(int(processes[6 * i + 4][1]))
        p6.append(int(processes[6 * i + 5][1]))
    p1.append(int(processes[246][1]))
    p2.append(int(processes[247][1]))
    p3.append(int(processes[248][1]))
    p4.append(int(processes[249][1]))
    for i in range(len(p1)):
        for j in range(i):
            wait_time_p1 += p1[j]
            turnaround_time_p1 += p1[j + 1]
        wait_times_p1.append(wait_time_p1)
        wait_time_p1 = 0
        turnaround_times_p1.append(turnaround_time_p1)
        turnaround_time_p1 = p1[0]
    for i in range(len(p2)):
        for j in range(i):
            wait_time_p2 += p2[j]
            turnaround_time_p2 += p2[j + 1]
        wait_times_p2.append(wait_time_p2)
        wait_time_p2 = 0
        turnaround_times_p2.append(turnaround_time_p2)
        turnaround_time_p2 = p2[0]
    for i in range(len(p3)):
        for j in range(i):
            wait_time_p3 += p3[j]
            turnaround_time_p3 += p3[j + 1]
        wait_times_p3.append(wait_time_p3)
        wait_time_p3 = 0
        turnaround_times_p3.append(turnaround_time_p3)
        turnaround_time_p3 = p3[0]
    for i in range(len(p4)):
        for j in range(i):
            wait_time_p4 += p4[j]
            turnaround_time_p4 += p4[j + 1]
        wait_times_p4.append(wait_time_p4)
        wait_time_p4 = 0
        turnaround_times_p4.append(turnaround_time_p4)
        turnaround_time_p4 = p4[0]
    for i in range(len(p5)):
        for j in range(i):
            wait_time_p5 += p5[j]
            turnaround_time_p5 += p5[j + 1]
        wait_times_p5.append(wait_time_p5)
        wait_time_p5 = 0
        turnaround_times_p5.append(turnaround_time_p5)
        turnaround_time_p5 = p5[0]
    for i in range(len(p6)):
        for j in range(i):
            wait_time_p6 += p6[j]
            turnaround_time_p6 += p6[j + 1]
        wait_times_p6.append(wait_time_p6)
        wait_time_p6 = 0
        turnaround_times_p6.append(turnaround_time_p6)
        turnaround_time_p6 = p6[0]
    print(
        "Average Wait Time for FIFO in Processor 1: "
        + str(sum(wait_times_p1) / len(wait_times_p1))
    )
    print(
        "Average Wait Time for FIFO in Processor 2: "
        + str(sum(wait_times_p2) / len(wait_times_p2))
    )
    print(
        "Average Wait Time for FIFO in Processor 3: "
        + str(sum(wait_times_p3) / len(wait_times_p3))
    )
    print(
        "Average Wait Time for FIFO in Processor 4: "
        + str(sum(wait_times_p4) / len(wait_times_p4))
    )
    print(
        "Average Wait Time for FIFO in Processor 5: "
        + str(sum(wait_times_p5) / len(wait_times_p5))
    )
    print(
        "Average Wait Time for FIFO in Processor 6: "
        + str(sum(wait_times_p6) / len(wait_times_p6))
    )
    print(
        "Average Turnaround Time for FIFO in Processor 1: "
        + str(sum(turnaround_times_p1) / len(turnaround_times_p1))
    )
    print(
        "Average Turnaround Time for FIFO in Processor 2: "
        + str(sum(turnaround_times_p2) / len(turnaround_times_p2))
    )
    print(
        "Average Turnaround Time for FIFO in Processor 3: "
        + str(sum(turnaround_times_p3) / len(turnaround_times_p3))
    )
    print(
        "Average Turnaround Time for FIFO in Processor 4: "
        + str(sum(turnaround_times_p4) / len(turnaround_times_p4))
    )
    print(
        "Average Turnaround Time for FIFO in Processor 5: "
        + str(sum(turnaround_times_p5) / len(turnaround_times_p5))
    )
    print(
        "Average Turnaround Time for FIFO in Processor 6: "
        + str(sum(turnaround_times_p6) / len(turnaround_times_p6))
    )


def sjf(fname):
    processes = sorted_processes(fname, 1)
    p1 = []
    p2 = []
    p3 = []
    p4 = []
    p5 = []
    p6 = []
    wait_times_p1 = []
    wait_time_p1 = 0
    turnaround_times_p1 = []
    turnaround_time_p1 = int(processes[0][1])
    wait_times_p2 = []
    wait_time_p2 = 0
    turnaround_times_p2 = []
    turnaround_time_p2 = int(processes[1][1])
    wait_times_p3 = []
    wait_time_p3 = 0
    turnaround_times_p3 = []
    turnaround_time_p3 = int(processes[2][1])
    wait_times_p4 = []
    wait_time_p4 = 0
    turnaround_times_p4 = []
    turnaround_time_p4 = int(processes[3][1])
    wait_times_p5 = []
    wait_time_p5 = 0
    turnaround_times_p5 = []
    turnaround_time_p5 = int(processes[4][1])
    wait_times_p6 = []
    wait_time_p6 = 0
    turnaround_times_p6 = []
    turnaround_time_p6 = int(processes[5][1])
    for i in range(41):
        p1.append(int(processes[6 * i][1]))
        p2.append(int(processes[6 * i + 1][1]))
        p3.append(int(processes[6 * i + 2][1]))
        p4.append(int(processes[6 * i + 3][1]))
        p5.append(int(processes[6 * i + 4][1]))
        p6.append(int(processes[6 * i + 5][1]))
    p1.append(int(processes[246][1]))
    p2.append(int(processes[247][1]))
    p3.append(int(processes[248][1]))
    p4.append(int(processes[249][1]))
    for i in range(len(p1)):
        for j in range(i):
            wait_time_p1 += p1[j]
            turnaround_time_p1 += p1[j + 1]
        wait_times_p1.append(wait_time_p1)
        wait_time_p1 = 0
        turnaround_times_p1.append(turnaround_time_p1)
        turnaround_time_p1 = p1[0]
    for i in range(len(p2)):
        for j in range(i):
            wait_time_p2 += p2[j]
            turnaround_time_p2 += p2[j + 1]
        wait_times_p2.append(wait_time_p2)
        wait_time_p2 = 0
        turnaround_times_p2.append(turnaround_time_p2)
        turnaround_time_p2 = p2[0]
    for i in range(len(p3)):
        for j in range(i):
            wait_time_p3 += p3[j]
            turnaround_time_p3 += p3[j + 1]
        wait_times_p3.append(wait_time_p3)
        wait_time_p3 = 0
        turnaround_times_p3.append(turnaround_time_p3)
        turnaround_time_p3 = p3[0]
    for i in range(len(p4)):
        for j in range(i):
            wait_time_p4 += p4[j]
            turnaround_time_p4 += p4[j + 1]
        wait_times_p4.append(wait_time_p4)
        wait_time_p4 = 0
        turnaround_times_p4.append(turnaround_time_p4)
        turnaround_time_p4 = p4[0]
    for i in range(len(p5)):
        for j in range(i):
            wait_time_p5 += p5[j]
            turnaround_time_p5 += p5[j + 1]
        wait_times_p5.append(wait_time_p5)
        wait_time_p5 = 0
        turnaround_times_p5.append(turnaround_time_p5)
        turnaround_time_p5 = p5[0]
    for i in range(len(p6)):
        for j in range(i):
            wait_time_p6 += p6[j]
            turnaround_time_p6 += p6[j + 1]
        wait_times_p6.append(wait_time_p6)
        wait_time_p6 = 0
        turnaround_times_p6.append(turnaround_time_p6)
        turnaround_time_p6 = p6[0]
    print(
        "Average Wait Time for SJF in Processor 1: "
        + str(sum(wait_times_p1) / len(wait_times_p1))
    )
    print(
        "Average Wait Time for SJF in Processor 2: "
        + str(sum(wait_times_p2) / len(wait_times_p2))
    )
    print(
        "Average Wait Time for SJF in Processor 3: "
        + str(sum(wait_times_p3) / len(wait_times_p3))
    )
    print(
        "Average Wait Time for SJF in Processor 4: "
        + str(sum(wait_times_p4) / len(wait_times_p4))
    )
    print(
        "Average Wait Time for SJF in Processor 5: "
        + str(sum(wait_times_p5) / len(wait_times_p5))
    )
    print(
        "Average Wait Time for SJF in Processor 6: "
        + str(sum(wait_times_p6) / len(wait_times_p6))
    )
    print(
        "Average Turnaround Time for SJF in Processor 1: "
        + str(sum(turnaround_times_p1) / len(turnaround_times_p1))
    )
    print(
        "Average Turnaround Time for SJF in Processor 2: "
        + str(sum(turnaround_times_p2) / len(turnaround_times_p2))
    )
    print(
        "Average Turnaround Time for SJF in Processor 3: "
        + str(sum(turnaround_times_p3) / len(turnaround_times_p3))
    )
    print(
        "Average Turnaround Time for SJF in Processor 4: "
        + str(sum(turnaround_times_p4) / len(turnaround_times_p4))
    )
    print(
        "Average Turnaround Time for SJF in Processor 5: "
        + str(sum(turnaround_times_p5) / len(turnaround_times_p5))
    )
    print(
        "Average Turnaround Time for SJF in Processor 6: "
        + str(sum(turnaround_times_p6) / len(turnaround_times_p6))
    )


def rr(fname, time_quantum):
    processes = unsorted_processes(fname)
    p1 = []
    p2 = []
    p3 = []
    p4 = []
    p5 = []
    p6 = []
    for i in range(41):
        p1.append(int(processes[6 * i][1]))
        p2.append(int(processes[6 * i + 1][1]))
        p3.append(int(processes[6 * i + 2][1]))
        p4.append(int(processes[6 * i + 3][1]))
        p5.append(int(processes[6 * i + 4][1]))
        p6.append(int(processes[6 * i + 5][1]))
    p1.append(int(processes[246][1]))
    p2.append(int(processes[247][1]))
    p3.append(int(processes[248][1]))
    p4.append(int(processes[249][1]))
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    count5 = 0
    count6 = 0
    while sum(p1) > 0:
        for i in range(len(p1)):
            if p1[i] - time_quantum > 0:
                p1[i] = p1[i] - time_quantum
            else:
                p1[i] = 0
        count1 = count1 + 1
    while sum(p2) > 0:
        for i in range(len(p2)):
            if p2[i] - time_quantum > 0:
                p2[i] = p2[i] - time_quantum
            else:
                p2[i] = 0
        count2 = count2 + 1
    while sum(p3) > 0:
        for i in range(len(p3)):
            if p3[i] - time_quantum > 0:
                p3[i] = p3[i] - time_quantum
            else:
                p3[i] = 0
        count3 = count3 + 1
    while sum(p4) > 0:
        for i in range(len(p4)):
            if p4[i] - time_quantum > 0:
                p4[i] = p4[i] - time_quantum
            else:
                p4[i] = 0
        count4 = count4 + 1
    while sum(p5) > 0:
        for i in range(len(p5)):
            if p5[i] - time_quantum > 0:
                p5[i] = p5[i] - time_quantum
            else:
                p5[i] = 0
        count5 = count5 + 1
    while sum(p6) > 0:
        for i in range(len(p6)):
            if p6[i] - time_quantum > 0:
                p6[i] = p6[i] - time_quantum
            else:
                p6[i] = 0
        count6 = count6 + 1
    print(str(count1))
    print(str(count2))
    print(str(count3))
    print(str(count4))
    print(str(count5))
    print(str(count6))


if __name__ == "__main__":
    file = "./processes.csv"
    time_quantum = 5 * 10**9
    fifo(file)
    sjf(file)
    rr(file, time_quantum)
