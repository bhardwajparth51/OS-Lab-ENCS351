# # 🚀 System Calls, VM Detection & File System Operations – OS Lab Assignment 04

A complete Python, Bash, and (optional) C-based implementation demonstrating system calls, batch execution, process creation, IPC, VM detection, and CPU scheduling.

<p align="center"> <img src="https://img.shields.io/badge/Python-3.8%2B-blue" /> <img src="https://img.shields.io/badge/Linux-Required-success" /> <img src="https://img.shields.io/badge/System%20Calls-fork%2Cexecvp%2Cwait-orange" /> <img src="https://img.shields.io/badge/Status-Completed-brightgreen" /> </p>

---

## 📌 Overview

This repository contains Assignment-04 of the Operating System Lab (ENCS351).
It demonstrates essential OS-level concepts using Python, Shell Scripting, and low-level system calls:

⚡ Batch Processing (Sequential execution of `.py` scripts)
🖥️ Process Creation & System Logging
🔌 Inter-Process Communication using `fork(), exec(), wait(), pipe()`
🖥️ Virtual Machine Detection
📂 Simulated CPU Scheduling Algorithms (FCFS, SJF, RR, Priority)

This assignment bridges theory with practical OS-level programming.
---

## 🗂 Repository Structure

```
📦 Assignment-04
├── scripts/
│   ├── script1.py               # Test script for batch execution
│   ├── script2.py
│   ├── script3.py
│   ├── task1.py                 # Batch processing controller
│   ├── task2.py                 # System boot simulation + logging
│   ├── task3.py                 # System calls + IPC using fork/pipe
│   ├── task3.c                  # (Optional) C program using fork/exec/pipe
│   ├── task4.py                 # VM detection (Python)
│   ├── task4.sh                 # Shell script for system info
│   └── task5.py                 # CPU Scheduling Algorithms
│
├── output/                      # Log files + Screenshots
│   ├── task1_output.png
│   ├── task2_output.png
│   ├── task3_output.png
│   ├── task3.c_output.png
│   ├── task4_output.png
│   ├── task4.sh_output.png
│   ├── task5_output.png
│   
│
└── README.md                    

```

---

## 🧰 Features

### ✔ Task 1 — Batch Processing Simulation

Runs multiple scripts sequentially using:

`subprocess.call(['python3', script])`

### ✔ Task 2 — System Startup & Logging

Simulates booting and shutdown using multiprocessing and logs to system_log.txt.

### ✔ Task 3 — System Calls & IPC

Implements:
```
fork()

exec()

wait()
```
Pipes for IPC

In Python and optionally C.

### ✔ Task 4 — VM Detection

Python script checks:

Virtualization type

CPU flags

Hypervisor presence

Shell script displays kernel, user, and virtualization info.

### ✔ Task 5 — CPU Scheduling

Implements:

FCFS

SJF

Priority Scheduling

Round Robin

Outputs WT & TAT for each process.
### ⚙️ Requirements

Python 3.x

Linux OS

Basic shell utilities

GCC (only if using task3.c)

### 📦 Setup & Installation

Clone the repository:

```
git clone https://github.com/bhardwajparth51/OS-Lab-ENCS351.git
cd Assignment-04
```

▶️ How to Run

Open terminal/command prompt and navigate to repository:

`cd scripts`


Run any task:
Run batch processing (Task 1)

`python3 task1.py`

Run system startup logger (Task 2)
`python3 task2.py`

Run system call + IPC (Task 3 - Python)
`python3 task3.py`

Compile and run C version of Task 3
`gcc task3.c -o ipc`
`./ipc`

Run VM detection (Task 4)
`bash task4.sh`
`python3 task4.py`

Run CPU Scheduling algorithms (Task 5)
`python3 task5.py`

Follow input prompts to simulate processes, file allocations, or memory allocations.

🔍 Sample Output

Task 1 Output
```
Executing script1.py...
Executing script2.py...
Executing script3.py...
```

Task 2 Log Example
```
2025-11-30 10:25:32 - Process-1 started
2025-11-30 10:25:34 - Process-1 terminated
```

Task 3 IPC Example
`Child received: Hello from parent`

Task 4 VM Detection Example
```
Hypervisor detected: KVM
Running inside a virtual machine
```

### 📝 What This Project Demonstrates
Concept	Implemented Through
Batch Processing	Python `subprocess`
Process Creation	`fork()`, `multiprocessing`
IPC	Pipes, message passing
VM Detection	`cpuinfo`, virtualization flags
Scheduling	FCFS, SJF, Priority, RR
Logging	Python `logging` module
### 🧑‍💻 Author

**Parth Bhardwaj**  
**B.Tech CSE (AIML)**  
**2301730289**  
**Section - E**


_A Python-based demonstration of process creation, scheduling, zombie/orphan processes, `/proc` inspection, and command execution using `fork()` and `execvp()`._

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.6%2B-blue" />
  <img src="https://img.shields.io/badge/Linux-Required-success" />
  <img src="https://img.shields.io/badge/OS-Lab%20Experiment-orange" />
  <img src="https://img.shields.io/badge/Status-Completed-brightgreen" />
</p>

---

## 📌 Overview

This repository demonstrates the simulation of key operating system concepts using Python:

⚡ CPU Scheduling (Priority & Round Robin)

🗂 File Allocation Techniques (Sequential & Indexed)

🖥 Memory Management (MFT, MVT, First-fit, Best-fit, Worst-fit)

📝 Calculation of Waiting Time, Turnaround Time, and allocation logs

This project helps understand theoretical OS concepts through practical coding exercises.

---

## 🗂 Repository Structure

```
📦 Lab3-OS-Simulation
├── task1_cpu_scheduling.py        # CPU Scheduling simulation
├── task2_sequential_allocation.py # Sequential File Allocation
├── task3_indexed_allocation.py    # Indexed File Allocation
├── task4_memory_allocation.py     # Contiguous Memory Allocation (First, Best, Worst-fit)
├── task5_mft_mvt.py               # MFT & MVT Memory Management
├── README.md                      # This file
└── outputs/                       # Optional folder for screenshots or log files
```

---

## 🧰 Features

### ✔ CPU Scheduling

Simulates Round Robin Scheduling with a user-defined time quantum

Calculates Average Waiting Time (AWT) and Average Turnaround Time (TAT)

### ✔ File Allocation

Sequential Allocation: Contiguous storage allocation for files

Indexed Allocation: Index blocks point to data blocks to simulate dynamic allocation

### ✔ Memory Management

Contiguous Memory Allocation: First-fit, Best-fit, Worst-fit strategies

MFT (Fixed Partition): Allocates processes to fixed-sized partitions

MVT (Variable Partition): Dynamically allocates memory to processes

### ⚙️ Requirements

Python 3.x

OS: Linux, Windows, or MacOS

Only uses Python standard libraries (`os, time, multiprocessing`)

### 📦 Setup & Installation

Clone the repository:

```
git clone https://github.com/bhardwajparth51/OS-Lab-ENCS351.git
cd Assignment-03
```

▶️ How to Run

Open terminal/command prompt and navigate to repository:

`cd Lab3-OS-Simulation`


Run any task:
```
python3 task1_cpu_scheduling.py
python3 task2_sequential_allocation.py
python3 task3_indexed_allocation.py
python3 task4_memory_allocation.py
python3 task5_mft_mvt.py
```

Follow input prompts to simulate processes, file allocations, or memory allocations.

🔍 Sample Output

CPU Scheduling Example:
```
Enter number of processes: 3
Enter Burst Time for P1: 10
Enter Priority (lower number = higher priority) for P1: 2
...
Average Waiting Time: 5.0
Average Turnaround Time: 12.0
```

Sequential File Allocation Example:
```
File 1 allocated from block 0 to 4
File 2 cannot be allocated
```

### 📝 What This Project Demonstrates
Concept	Demonstrated Through
CPU Scheduling	Priority, Round Robin
File Allocation Techniques	Sequential, Indexed
Memory Management	MFT, MVT, First/Best/Worst-fit
Metrics Calculation	Waiting Time, Turnaround Time

### 🧑‍💻 Author

**Parth Bhardwaj**  
**B.Tech CSE (AIML)**  
**2301730289**  
**Section - E**
