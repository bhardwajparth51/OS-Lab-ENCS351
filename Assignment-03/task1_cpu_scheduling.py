# Task 1: CPU Scheduling - Priority and Round Robin

def priority_scheduling():
    processes = []
    n = int(input("Enter number of processes: "))
    for i in range(n):
        bt = int(input(f"Enter Burst Time for P{i+1}: "))
        pr = int(input(f"Enter Priority (lower number = higher priority) for P{i+1}: "))
        processes.append((i+1, bt, pr))
    processes.sort(key=lambda x: x[2])
    wt = 0
    total_wt = 0
    total_tt = 0
    print("\nPriority Scheduling:")
    print("PID\tBT\tPriority\tWT\tTAT")
    for pid, bt, pr in processes:
        tat = wt + bt
        print(f"{pid}\t{bt}\t{pr}\t\t{wt}\t{tat}")
        total_wt += wt
        total_tt += tat
        wt += bt
    print(f"Average Waiting Time: {total_wt / n}")
    print(f"Average Turnaround Time: {total_tt / n}")

def round_robin():
    processes = []
    n = int(input("Enter number of processes: "))
    for i in range(n):
        bt = int(input(f"Enter Burst Time for P{i+1}: "))
        processes.append([i+1, bt])
    tq = int(input("Enter Time Quantum: "))
    rem_bt = [p[1] for p in processes]
    t = 0
    wt = [0]*n
    while True:
        done = True
        for i in range(n):
            if rem_bt[i] > 0:
                done = False
                if rem_bt[i] > tq:
                    t += tq
                    rem_bt[i] -= tq
                else:
                    t += rem_bt[i]
                    wt[i] = t - processes[i][1]
                    rem_bt[i] = 0
        if done:
            break
    print("\nRound Robin Scheduling:")
    print("PID\tWT\tTAT")
    total_wt = 0
    total_tt = 0
    for i in range(n):
        tat = wt[i] + processes[i][1]
        total_wt += wt[i]
        total_tt += tat
        print(f"{processes[i][0]}\t{wt[i]}\t{tat}")
    print(f"Average Waiting Time: {total_wt/n}")
    print(f"Average Turnaround Time: {total_tt/n}")

print("Choose CPU Scheduling Algorithm:\n1. Priority\n2. Round Robin")
choice = int(input("Enter choice: "))
if choice == 1:
    priority_scheduling()
elif choice == 2:
    round_robin()
else:
    print("Invalid choice")
