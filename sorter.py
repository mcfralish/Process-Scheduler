import sys
import csv


def sort(fname, rownnum):
    reader = csv.reader(open("tuples.csv"), delimiter=",")
    sortedlist = sorted(reader, key=lambda row: row[rownum])
    return sortedlist

sort("tuples.csv")

def FIFO():
    results = {"wait": 0, "turnaround": 0}

    # logic
    
    return results