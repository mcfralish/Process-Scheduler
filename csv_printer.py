import csv
import q1_v2 as q1
import q2
import q3_v2 as q3
import q4
from statistics import mean


input = "./processes.csv"
output = "./q4avgs.csv"
quantum = 5 * 10**9

q1_fifo = q1.fifo(input)
q1_sjf = q1.sjf(input)
q1_rr = q1.rr(input, quantum)
q2_fifo = q2.FIFO(input, 3, 3)
q2_sjf = q2.SJF(input, 3, 3)
q2_rr = q2.RR(input, 3, 3, quantum)
q3_data = q3.run(input)
q4_data = q4.run(input)


qnum = ["Q4"]
header = [
    "avg wait times",
    "avg turnaround times",
]
c1 = mean(q4_data["wait_times"])
c2 = mean(q4_data["turnaround_times"])


f = open(output, "w")
w = csv.writer(f)
w.writerow(qnum)
w.writerow(header)
w.writerow([c1, c2])
# for i in range(len(c1)):
#     w.writerow([c1[i], c2[i], c3[i], c4[i]])

f.close()
