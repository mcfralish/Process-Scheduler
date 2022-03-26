import q1
import q2
import q3

# import q4

file = "./processes.csv"
quantum = 5 * 10**9

q1.fifo(fname=file)
q1.sjf(fname=file)
q1.rr(fname=file, time_quantum=quantum)
q2.FIFO(fname=file, num_slow=3, num_fast=3)
q2.SJF(fname=file, num_slow=3, num_fast=3)
q2.RR(fname=file, num_slow=3, num_fast=3, quantum=quantum)
q3.SJF(fname=file)
# q4.SJF(fname=file)
