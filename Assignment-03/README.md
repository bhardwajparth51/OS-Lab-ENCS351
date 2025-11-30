# 🚀 Process Management Lab (Linux OS) - Assignment 03

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
