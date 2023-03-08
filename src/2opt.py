import numpy as np
import random
import time

global n
global ub,lb,d,eld
global list_node

n = int(input()) #input number of customer
lb=[0] ##upper bound
ub=[0] ##lower bound
eld=[[0,0,0]]

for _ in range(n):
    temp=[int(x) for x in input().split()]
    eld.append(temp)
    ub.append(temp[0]) 
    lb.append(temp[1])

d = [[int(x) for x in input().split()] for i in range(n+1)] #input travel time array

list_node = [] #empty list
dict = {i: (lb[i] - d[0][i], ub[i] - d[0][i]) for i in range(1, n+1)}
sorted_dict = {key: val for key, val in sorted(dict.items(), key = lambda v: (v[1][0], v[1][1]), reverse = False)}
for i in list(sorted_dict.keys()):
    list_node.append(i)

#time constrain checker
#time constrain checker
def IsViolate(customer_time):
    for i in range(1,n+1):
        if eld[i][0] > customer_time[i] or eld[i][1] < customer_time[i]:
            return True
    return False


#calculate path time
def path_time(route):
    customer_time = [0 for i in range (n + 1)]
    time = 0
    
    for i in range(len(route)-1):
        time += d[int(route[i])][int(route[i+1])] + eld[int((route[i+1])) - 1][2]
        customer_time[int(route[i+1])] = time
    
    violate = IsViolate(customer_time)

    return time, False
        
#2-opt-swapper
two_opt_swap = lambda r,i,k: np.concatenate((r[0:i],r[k:-len(r)+i-1:-1],r[k+1:len(r)]))

def two_opt(improvement_threshold):
    violate = True
    while violate:                              # make initial route by shuffling customer (while startpoint is fixed), but if its
        route = list_node
        #random.shuffle(route)                    # violated we make a new one
        best_time, violate = path_time(route)   # calc the time of the initial path
        no_violate_best_route = route
    
    
    improvement_factor = 1 #init improvement factor
    
    
    while improvement_factor > improvement_threshold: # keep going if theres still improvement
        time_to_beat = best_time # Record the previous best time at the beginning of the loop
        for swap_first in range(1,len(route)-1): # from each customer except the first
            for swap_last in range(swap_first+1,len(route)): # to each of the customer following
                new_route = two_opt_swap(route,swap_first,swap_last) # try reversing the order of these cities
                new_time, violate2 = path_time(new_route) # and check the total time with this modification.
                if new_time < best_time: # if the time is improved
                    route = new_route # make this the accepted best route
                    best_time = new_time # and update the time corresponding to this route
                    if violate2 == False:
                        no_violate_best_route = route # remember the best route that wasnt violated

            improvement_factor = 1 - best_time/time_to_beat # calculate how much the route has improved

    return no_violate_best_route # when the route is no longer improving, stop searching and return the lastest accepted new row

print(n)
st = time.time()
print(*list(two_opt(0.1)))
print("{0:.5f} s".format(time.time()-st))