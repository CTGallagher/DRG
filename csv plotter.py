import math
import csv
import scipy.signal as sig
import numpy as np
import matplotlib.pyplot as plt

def raw_convert(input_string):
    new_string = input_string.encode('unicode-escape').decode()
    return new_string

print("format: first column = time series; second column starts trace no ROI #")
r_before = input("Input file path1: ")
r_before = raw_convert(r_before)
r_after = input("Input file path2: ")
r_after = raw_convert(r_after)
timestamp = input("input timestamp: ")
timestamp = raw_convert(timestamp)
name1 = input("Input the base name for the plots: ")

def read_file(read_file):
    data = {}
    with open(read_file, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            col_num = 0
            for col in row:
                col_num += 1
                if col_num in data:
                    data[col_num].append(col)
                else:
                    ls = col
                    ls = [ls]
                    data[col_num] = ls
    return data

def debug_delete(list):
    new_list = []
    for i in range((len(list))//10):
        new_list.append(list[i])
    return new_list

def double_plot():
    before = read_file(r_before)
    after = read_file(r_after)
    time = read_file(timestamp)
    if len(before) == len(after):
        for i in range(len(before)):
            if i != 0:
                name = name1 + str(i)
                b_array = np.asarray(np.float_(before[i]))
                a_array = np.asarray(np.float_(after[i]))
                t_array = np.asarray(np.float_(time[1]))
                plt.plot(t_array, b_array)
                plt.plot(t_array, a_array)
                plt.savefig(name)
                plt.clf()
    else:
        print(len(before))
        print(len(after))
        print("dimension failure")



double_plot()
