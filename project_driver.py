import q1
import q2

# import q3
# import q4

file = "./processes.csv"
quantum = 5 * 10**9

q1.fifo(file)
q1.sjf(file)
q1.rr(file, quantum)
q2.FIFO(fname=file, num_slow=3, num_fast=3)
q2.SJF(fname=file, num_slow=3, num_fast=3)
q2.RR(fname=file, num_slow=3, num_fast=3, quantum=quantum)
