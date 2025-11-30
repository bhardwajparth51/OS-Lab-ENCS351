# Task 4: Contiguous Memory Allocation - First, Best, Worst fit
def allocate_memory(strategy):
    partitions = list(map(int, input("Enter partition sizes separated by space: ").split()))
    processes = list(map(int, input("Enter process sizes separated by space: ").split()))
    allocation = [-1] * len(processes)

    for i, psize in enumerate(processes):
        idx = -1
        if strategy == "first":
            for j, part in enumerate(partitions):
                if part >= psize:
                    idx = j
                    break
        elif strategy == "best":
            best_fit = float("inf")
            for j, part in enumerate(partitions):
                if part >= psize and part < best_fit:
                    best_fit = part
                    idx = j
        elif strategy == "worst":
            worst_fit = -1
            for j, part in enumerate(partitions):
                if part >= psize and part > worst_fit:
                    worst_fit = part
                    idx = j
        if idx != -1:
            allocation[i] = idx
            partitions[idx] -= psize

    for i, a in enumerate(allocation):
        if a != -1:
            print(f"Process {i+1} allocated in Partition {a+1}")
        else:
            print(f"Process {i+1} cannot be allocated")

print("First-fit Allocation:")
allocate_memory("first")
print("\nBest-fit Allocation:")
allocate_memory("best")
print("\nWorst-fit Allocation:")
allocate_memory("worst")
