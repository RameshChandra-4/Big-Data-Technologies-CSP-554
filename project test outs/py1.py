# Import time module
import time

# record start time
start = time.time()

def factorial(n):
  # single line to find factorial
  return 1 if (n==1 or n==0) else n * factorial(n - 1);
 
# Driver Code
num = 90;
print("Factorial of",num,"is",factorial(num))

# record end time
end = time.time()

# print the difference between start
# and end time in milli. secs
print("The time of execution of above program is :",
	(end-start) * 10**3, "ms")


## Factorial of 90 is 1485715964481761497309522733620825737885569961284688766942216863704985393094065876545992131370884059645617234469978112000000000000000000000
## The time of execution of above program is : 0.1404285430908203 ms
<div class="icons8-sharingan"></div>

EEE | dd MMM Y | hh:mm a 