from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import ThreadPoolExecutor
import os, time

# if the work is CPU intensive, threads should be slower than processes
N = 1000000
JOBS = 20 

def work(n, N):
    pid = os.getpid()
    sum_ = 0
    for k in range(N):
        sum_ += (k/10)**(1/n**2)
    return pid, sum_


def compute(executor, name):
    start = time.time()
    futures = [executor.submit(work, n+1, N) for n in range(JOBS)]
    results = [futures[n].result() for n in range(JOBS)]
    print(f"\n\n{name} took {time.time() - start:.1f} secs")
    zippedResults = list(zip(*results))
    pids = set(zippedResults[0])
    totals = zippedResults[1]
    print(f"pids = {pids}")
    print(f"{len(totals)} results:")
    print([f"total = {total:6.2f}" for total in totals])

with ProcessPoolExecutor(max_workers=10) as executor: compute(executor, "processes")
with ThreadPoolExecutor(max_workers=10) as executor: compute(executor, "threads")
