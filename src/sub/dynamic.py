def F(S, start, end, t):
    distance = [[float("inf") for j in range(len(S))] for i in range(len(S))]
    if e[end] <= t <= l[end]:
        if S == {start, end}:
            if t == max(e[start] + d[start] + t_ij[start][end], e[end]) and (start, end) in A:
                distance[start][end] = c[start][end]
                order[end][len(S) - 1] = "1" + str(end)
                return distance[start][end]
            else:
                return float("inf")
        else:
            for i in S - {start, end}:
                if (i, end) in A and e[i] <= t - d[i] - t_ij[i][end] <= l[i]:
                    distance[i][end] = F(S - {end}, start, i, t - d[i] - t_ij[i][end]) + c[i][end]
            result = min([distance[i][end] for i in S - {start, end}])
            for x in S - {start, end}:
                if distance[x][end] == result:
                    order[end][len(S) - 1] = order[x][len(S) - 2] + str(end)
            return result
    else:
        return float("inf")

def ORDER(N, start, end):
    N_ = N - {end}
    for S in powerset(N_):
        if start in S:
            save = [None for i in range(len(S))]
            for x in S - {start}:
                if order[x][len(S) - 2] is not None:
                    save[x] = order[x][len(S) - 2]
                    order[x][len(S) - 2] = None
            for j in S - {start}:
                for t in range(e[j], l[j] + 1):
                    dis[j][len(S) - 1] = min(dis[j][len(S) - 1], F(S, start, j, t))
                if dis[j][len(S) - 1] > dis[j][len(S) - 2]:
                    order[j][len(S) - 1] = save[j]
                else:
                    dis[j][len(S) - 2] = dis[j][len(S) - 1]
    distance = [float("inf") for i in range(len(N))]
    for j in N_:
        if (j, end) in A:
            for t in range(e[j], l[j] + 1):
                distance[j] = min(distance[j], F(N_, start, j, t) + c[j][end])
    result = min(distance)
    for x in N_:
        if distance[x] == result:
            order[end][len(N) - 1] = order[x][len(N) - 2] + str(end)
    return result

