import cothread
import random

pulse = cothread.Pulse()

def worker(n, pulse):
    pulse.Wait()
    for i in range(25):
        print(f"{n}", end="")
        cothread.Sleep(random.random() * 0.5) # suspend cothread   
    print()

threads = []
for n in range(1, 5):
    t = cothread.Spawn(worker, n, pulse)
    threads.append(t)

delay = 10
print(f"main cothread waiting for {delay} seconds")
cothread.Sleep(delay)

pulse.Signal()

for t in threads:
    t.Wait()
