# Task 5: CPU Scheduling Algorithms - FCFS, SJF, RR, Priority

# ---------------- FCFS -------------------
def fcfs(burst):
    n = len(burst)
    wt = [0] * n
    tat = [0] * n

    for i in range(1, n):
        wt[i] = wt[i - 1] + burst[i - 1]

    for i in range(n):
        tat[i] = wt[i] + burst[i]

    avg_wt = sum(wt) / n
    avg_tat = sum(tat) / n
    return wt, tat, avg_wt, avg_tat

# ---------------- SJF --------------------
def sjf(burst):
    n = len(burst)
    sorted_burst = sorted(burst)
    return fcfs(sorted_burst)

# ---------------- Priority ----------------
def priority_scheduling(burst, priority):
    n = len(burst)
    tasks = list(zip(priority, burst))
    tasks.sort()  # Sort by priority

    sorted_burst = [x[1] for x in tasks]
    return fcfs(sorted_burst)

# ---------------- Round Robin ------------
def round_robin(burst, quantum):
    n = len(burst)
    rem = burst.copy()
    t = 0
    wt = [0] * n

    while True:
        done = True

        for i in range(n):
            if rem[i] > 0:
                done = False
                if rem[i] > quantum:
                    t += quantum
                    rem[i] -= quantum
                else:
                    t += rem[i]
                    wt[i] = t - burst[i]
                    rem[i] = 0

        if done:
            break

    tat = [wt[i] + burst[i] for i in range(n)]
    return wt, tat, sum(wt)/n, sum(tat)/n

# ---------------- Main Program ------------
if __name__ == "__main__":
    burst = [10, 5, 8]
    priority = [2, 1, 3]
    quantum = 4

    print("\n--- FCFS Scheduling ---")
    print(fcfs(burst))

    print("\n--- SJF Scheduling ---")
    print(sjf(burst))

    print("\n--- Priority Scheduling ---")
    print(priority_scheduling(burst, priority))

    print("\n--- Round Robin Scheduling ---")
    print(round_robin(burst, quantum))
