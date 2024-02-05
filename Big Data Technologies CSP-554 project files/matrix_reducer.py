
import sys
from operator import itemgetter
import time
import datetime
prev_index = None
value_list = []

for line in sys.stdin:
    curr_index, index, value = line.rstrip().split("\t")
    index, value = map(int,[index,value])
    if curr_index == prev_index:
        value_list.append((index,value))
    else:
        if prev_index:
            value_list = sorted(value_list,key=itemgetter(0))
            i = 0
            result = 0
            while i < len(value_list) - 1:
                if value_list[i][0] == value_list[i + 1][0]:
                    result += value_list[i][1]*value_list[i + 1][1]
                    i += 2
                else:
                    i += 1
            print("%s,%s"%(prev_index,str(result)))
        prev_index = curr_index
        value_list = [(index,value)]

if curr_index == prev_index:
    value_list = sorted(value_list,key=itemgetter(0))
    i = 0
    result = 0
    while i < len(value_list) - 1:
        if value_list[i][0] == value_list[i + 1][0]:
            result += value_list[i][1]*value_list[i + 1][1]
            i += 2
        else:
            i += 1
    print("%s,%s"%(prev_index,str(result)))

file1 = open('run_time_noted.txt', 'a')#print("End Time: "+str(finished_time)+"\n")
finished_time = time.time()#finished_time=('%02d:%02d.%d'%(end_time_now.minute,end_time_now.second,end_time_now.microsecond))[:-4]
et= "End Time: "+str(finished_time)+"\n"
file1.write(et)
file1.close()
