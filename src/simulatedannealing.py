import numpy as np
import random
import time
import math

global n
global ub,lb,d,eld

n = int(input()) #input number of customer
ub=[0] ##upper bound
lb=[0] ##lower bound
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
        time += d[route[i]][route[i+1]] + eld[(route[i+1]) - 1][2]
        customer_time[route[i+1]] = time
    
    violate = IsViolate(customer_time)
    return time, violate


def neighbour(route): # create neighbour route by swapping two random customer
    n = len(route)
    result = np.copy(route)
    i = random.randint(0,n-1)
    j = random.randint(0,n-1)
    tmp = result[i]
    result[i] = result[j]
    result[j] = tmp
    return result

def solve(N, max_iter, starting_temperature, min_temperature, alpha):
    best_route = list_node      # violated we make a new one
    energy, violate = path_time(best_route)
    no_violate_best_route = None
    current_temperature = starting_temperature
    iter = 0
    violate2=True 

    while iter < max_iter:
        neighbour_route = neighbour(best_route) # generate neighbour route
        neighbour_energy, violate2 = path_time(neighbour_route)

        if neighbour_energy < energy:                                              # if neighbour route is better,
            best_route = neighbour_route
            energy = neighbour_energy
            if not violate2:                                                       # also update if not violated
                no_violate_best_route = best_route
        else:         
            accept_p = (math.e**(-(energy - neighbour_energy) / current_temperature))  
            p = random.random()
            if accept_p >= p:
                    best_route = neighbour_route
                    energy = neighbour_energy   
                    if not violate2:                                                       # also update if not violated
                        no_violate_best_route = best_route          # we still take it

        if current_temperature < min_temperature:                                  # reset the temperature to min if its too low
            current_temperature = min_temperature
        else:
            current_temperature *= alpha   
        iter+=1
    return no_violate_best_route                              

print(n)
def main():
    
    total=[]
    st = time.time()
    temp=solve(n,10,2000,0.001,0.999)

    print(*temp)
    ed = time.time()
    print(ed-st)

main()
