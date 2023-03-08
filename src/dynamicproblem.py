from sub.dynamic import *

N = int(input()) #input number of customer
eld = [[int(x) for x in input().split()] for i in range(N)] #input time constrain array
d = [[int(x) for x in input().split()] for i in range(N+1)] #input travel time array

