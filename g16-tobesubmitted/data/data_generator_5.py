import os

temppath=str(os.path.dirname(__file__))+"\\"+"data5.txt"
with open(temppath, "rt") as f:
    n = f.readline()
    n = int(n)-1
    matrix_row = [None]*(n+1)
    for i in range(n+1):
        matrix_row[i] = f.readline().strip()
    el = [None]*(n)
    eld = [None]*(n)
    f.readline()
    for i in range(n):
        el[i] = f.readline()
        eld[i] = " ".join(el[i].split()) + " 0"

with open(temppath, "wt") as f:
    f.write(f"{n}")
    for i in range(n):
        f.write(f"\n{eld[i]}")
    for i in range(n+1):
        f.write(f"\n{matrix_row[i]}")