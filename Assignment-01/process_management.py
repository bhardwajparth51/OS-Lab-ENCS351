#!/usr/bin/env python3
import os
import time
import subprocess
import sys

# ================================================================
# Task 1: Process Creation Utility
# ================================================================

def task1_create_processes(n):
    print("\n===== Task 1: Creating Child Processes =====")

    children = []

    for i in range(n):
        pid = os.fork()

        if pid == 0:   # Child process
            print(f"[Child] PID: {os.getpid()}, PPID: {os.getppid()}, Message: Child {i} created.")
            os._exit(0)

        else:  # Parent process
            children.append(pid)

    # Parent waits for all children
    for child in children:
        os.waitpid(child, 0)
    print("All child processes completed.\n")


# ================================================================
# Task 2: Executing Linux Commands Using execvp() or subprocess.run()
# ================================================================

def task2_execute_commands(commands):
    print("\n===== Task 2: Executing Commands in Child Processes =====")

    for cmd in commands:
        pid = os.fork()

        if pid == 0:   # Child
            print(f"\n[Child Process Executing Command] {cmd}")
            try:
                os.execvp(cmd[0], cmd)
            except Exception as e:
                print("execvp failed:", e)
                os._exit(1)
        else:
            os.waitpid(pid, 0)

    print("\nAll commands executed.\n")


# ================================================================
# Task 3: Zombie & Orphan Process Demonstration
# ================================================================

def task3_zombie_orphan():
    print("\n===== Task 3: Zombie & Orphan Processes =====")

    # Zombie Process
    print("\n--- Zombie Process Demo ---")
    pid = os.fork()

    if pid == 0:  # Child
        print(f"[Zombie Child] PID: {os.getpid()} exiting...")
        os._exit(0)
    else:
        print(f"[Parent] Created child {pid}, NOT waiting (zombie created)")
        time.sleep(5)  # give time to observe with: ps -el | grep defunct

    # Orphan Process
    print("\n--- Orphan Process Demo ---")
    pid2 = os.fork()

    if pid2 == 0:  # Child
        print(f"[Orphan Child] Original PPID: {os.getppid()}")
        time.sleep(4)
        print(f"[Orphan Child] New PPID after parent exited: {os.getppid()}")
        os._exit(0)
    else:
        print("[Parent] Exiting immediately, child will become orphan.\n")
        time.sleep(1)
        return  # Parent exits


# ================================================================
# Task 4: Inspecting /proc Information
# ================================================================

def task4_inspect_proc(pid):
    print("\n===== Task 4: Inspecting /proc Information =====")

    try:
        with open(f"/proc/{pid}/status", "r") as f:
            status_data = f.read()

        exe_path = os.readlink(f"/proc/{pid}/exe")
        fd_list = os.listdir(f"/proc/{pid}/fd")

        print("\n--- /proc/[pid]/status ---")
        print(status_data)

        print("--- Executable Path ---")
        print(exe_path)

        print("--- Open File Descriptors ---")
        print(fd_list)

    except Exception as e:
        print("Error reading /proc:", e)


# ================================================================
# Task 5: Process Prioritization Using nice()
# ================================================================

def cpu_intensive_task(index, nice_value):
    os.nice(nice_value)
    print(f"[Child {index}] PID {os.getpid()} started with nice = {nice_value}")

    x = 0
    for i in range(10_000_000):  # CPU work
        x += i

    print(f"[Child {index}] Completed.")


def task5_priorities():
    print("\n===== Task 5: Process Prioritization =====")

    priorities = [0, 5, 10, 15]
    children = []

    for i, nv in enumerate(priorities):
        pid = os.fork()

        if pid == 0:  # Child
            cpu_intensive_task(i, nv)
            os._exit(0)
        else:
            children.append(pid)

    for c in children:
        os.waitpid(c, 0)

    print("Priority demo completed.\n")


# ================================================================
# MAIN PROGRAM
# ================================================================

if __name__ == "__main__":
    sys.stdout = open("output.txt", "w")
    print("\n==================== PROCESS MANAGEMENT LAB ====================")

    # Task 1
    task1_create_processes(3)

    # Task 2
    task2_execute_commands([
        ["ls", "-l"],
        ["date"],
        ["ps"]
    ])

    # Task 3
    task3_zombie_orphan()

    # Task 4
    my_pid = os.getpid()
    task4_inspect_proc(my_pid)

    # Task 5
    task5_priorities()

    print("All tasks completed.")
