import q1_v2 as q1
import q2
import q3_v2 as q3
import q4

file = "./processes.csv"
quantum = 5 * 10**9

q1.fifo(fname=file)
print()
q1.sjf(fname=file)
print()
q1.rr(fname=file, quantum=quantum)
print()
q2.FIFO(fname=file, slowps=3, fastps=3)
print()
q2.SJF(fname=file, slowps=3, fastps=3)
print()
q2.RR(fname=file, slowps=3, fastps=3, quantum=quantum)
print()
q3.run(fname=file)
print()
q4.run(fname=file)
