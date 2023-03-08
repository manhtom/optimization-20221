import math

global n
global ub,lb,d,eld,list_node,res

n = int(input()) #input number of customer
ub=[0] ##upper bound
lb=[0] ##lower bound
eld=[[0,0,0]]

for _ in range(n):
    temp=[int(x) for x in input().split()]
    eld.append(temp)
    lb.append(temp[0]) 
    ub.append(temp[1])

d = [[int(x) for x in input().split()] for i in range(n+1)] #input travel time array
N = [i for i in range(1, n+1)]

arc = [[False]*(n+1)]*(n+1)
for i in range(1, n+1):
	for j in range(1, n+1):
		if lb[i]+eld[i][2]+d[i][j] <= ub[j]: arc[i][j] = True

tim = [[math.inf]*(n+1)]*(n+1)
order = [[""]*(n+1)]*(n+1)

def F(S, i, j):
	#time cost going from node i to node j in set S
	time_between = [[math.inf]*(n+1)]*(n+1)
	result = math.inf

	if len(S) == 2:
		if arc[i][j]: 
			time_between[i][j] = max(max(d[0][i], lb[i]) + eld[i][2] + d[i][j], lb[j])
			order[2][j] = f"{i}{j}"
			result = time_between[i][j]
	else:
		for k in S:
			if k == i or k == j: continue
			if arc[k][j]: 
				S2 = S[:]
				S2.remove(j)
				time_between[i][j] = max(F(S2, i, k) + eld[k][2] + d[k][j], lb[j])
				
				if time_between[i][j] < result:
					result = time_between[i][j]
					order[len(S)][j] = order[len(S)-1][k] + f"{j}"

	return result

def recheck(S, i, j):
	#check whether the path sastifies constraints or not
	current_time = max(d[0][i], lb[i])
	for k in range(1, len(S)):
		prev = int(order[len(S)][j][k-1])
		curr = int(order[len(S)][j][k])
		if k == 1: current_time = max(current_time + eld[i][2] + d[i][curr], lb[curr])
		else: current_time = max(current_time + eld[prev][2] + d[prev][curr], lb[curr])
	
	if S == N:
		if current_time <= ub[j]: return True
		else: return False

	for x in N:
		if x not in S:
			if current_time + eld[j][2] + d[j][x] > ub[x]: return False

	return True

def subsets(numbers):
	#find all subsets of a set
	if numbers == []: return [[]]
	lis = subsets(numbers[1:])
	return lis + [[numbers[0]] + y for y in lis]

def subsets_of_size(numbers, size):
	return [lis for lis in subsets(numbers) if len(lis) == size]

flag = True
x = 2
while flag:
	subset =subsets_of_size(N, x)
	
	for S in subset:
		for i in S:
			save = [""]*(n+1)
			for j in S:
				if j == i: continue
				save[j] = order[len(S)][j]

				t = F(S, i, j)
				if t == math.inf or not recheck(S, i, j):
					order[len(S)][j] = save[j]
					continue
				time_cost = float(t + eld[j][2])

				#compare and update
				if time_cost > tim[len(S)][j]: order[len(S)][j] = save[j]
				else: tim[len(S)][j] = time_cost

	if x == n: flag = False #check status of flag
	x += 1 #increasing loop count

def ORDER(i, j):
	tempo=[]
	#print out the solution
	for x in order[n][j]:
		tempo.append(x)
	res.append(tempo)

print(n)

#Find the optimal solution
min_path = math.inf
min_coor_x = 0
min_coor_y = 0
res=[]
for i in range(1, n+1):
	for j in range(1, n+1):
		if j == i: continue
		t = F(N, i, j)
		if t == math.inf or not recheck(N, i, j): continue
		time_cost = float(t + eld[j][2])
		if time_cost <= min_path:
			min_path = time_cost
			min_coor_x = i
			min_coor_y = j
			ORDER(min_coor_x, min_coor_y) #optimal solution is the last one appear
print(*res[len(res)-1])