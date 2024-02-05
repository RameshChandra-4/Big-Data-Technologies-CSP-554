import sys
import time
import datetime
inital_time = time.time()
#inital_time=('%02d:%02d.%d'%(inital_time_now.minute,inital_time_now.second,inital_time_now.microsecond))[:-4]
file1 = open('run_time_noted.txt', 'a')
file1.write("\n Dim 130X130 \n")
st= "Start Time: "+str(inital_time)+"\n"
#print("Start Time: "+str(inital_time)+"\n")
file1.write(st)
file1.close()
rowOfFirstMat, colOfSecondMat = 130,130 # dimensions of resultant matrix
for line in sys.stdin:
	matrix_index, row, col, value = line.rstrip().split(",")
	if matrix_index == "A":
		for i in range(0,colOfSecondMat):
			key = row + "," + str(i)
			print("%s\t%s\t%s"%(key,col,value))
	else:
		for j in range(0,rowOfFirstMat):
			key = str(j) + "," + col 
			print("%s\t%s\t%s"%(key,row,value))


