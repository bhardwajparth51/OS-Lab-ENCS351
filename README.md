# 🚀 Process Management Lab (Linux OS) - Assignment 01
*A Python-based demonstration of process creation, scheduling, zombie/orphan processes, `/proc` inspection, and command execution using `fork()` and `execvp()`.*

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.6%2B-blue" />
  <img src="https://img.shields.io/badge/Linux-Required-success" />
  <img src="https://img.shields.io/badge/OS-Lab%20Experiment-orange" />
  <img src="https://img.shields.io/badge/Status-Completed-brightgreen" />
</p>

---

## 📌 Overview

This repository contains a complete implementation of **Linux process management concepts** using Python. It covers:

- 👶 **Process Creation** using `fork()`
- 🏗 **Executing commands** using `execvp()`
- 🧟 **Zombie Process Demonstration**
- 🍼 **Orphan Process Demonstration**
- 📂 **Inspecting `/proc/[pid]` entries**
- 🎚 **Process Priority Management** using `nice()`
- 📄 **Redirection of all output** to `output.txt`

This project is ideal for OS lab submissions, system programming learners, and Linux-based academic projects.

---

## 🗂 Repository Structure

```
📦 Process-Management-Lab
├── process_management.py # Main program with all 5 tasks
├── output.txt # Generated output for all tasks
├── README.md # Instructions, usage, requirements
└── report.pdf/ # Lab report
```

---

## 🧰 Features

### ✔ Process Creation
Demonstrates parent-child relationship using `fork()`.

### ✔ Execute System Commands
Uses `execvp()` to run:


```
ls -l
date
ps
```
✔ Zombie & Orphan Processes
Shows real kernel-level behavior of process states.

✔ /proc Filesystem Inspection
Reads:

```
/proc/<pid>/status
/proc/<pid>/exe
/proc/<pid>/fd
```
✔ Process Priority Scheduling
Runs CPU-intensive tasks at different priority levels using:


`os.nice()`
## ⚙️ Requirements
#### 🐧 Linux OS — Must Have
This program requires Linux because it relies on:

```
fork()

execvp()

/proc filesystem

nice()
```

UNIX scheduling behavior

#### 🎯 Windows users must use WSL or a Linux VM.

#### 🐍 Python
Python 3.6 or above.

✔ No external libraries required
Only uses Python standard libraries:

```
import os
import time
import subprocess
import sys
```
###📦 Setup & Installation
Clone the repository:

```
git clone https://github.com/bhardwajparth51/OS-Lab-ENCS351/Assignment-01.git
cd Process-Management-Lab
```

### ▶️ How to Run
Run the program:


Copy code
python3 prcoess_management.py
All output will be saved to output.txt.

Nothing prints on the terminal because sys.stdout is redirected.

### 🔍 Verify Zombie & Orphan Processes
While Task 3 executes, open another terminal:

Check Zombie:

`ps -el | grep defunct`

Check Orphan:
In output.txt, observe:

Original PPID

New PPID (usually 1 → adopted by systemd)

<p align="center"> <img src="screenshots/zombie_demo.png" width="600"> </p>
### 📘 Code Snippets
Running tasks:

```
print("\n==================== PROCESS MANAGEMENT LAB ====================")

task1_create_processes(3)
task2_execute_commands([["ls", "-l"], ["date"], ["ps"]])
task3_zombie_orphan()

mypid = os.getpid()
task4_inspect_proc(mypid)

task5_priorities()
```
### 📝 What This Project Demonstrates
Concept	Demonstrated Through
Process Creation	fork()
Command Execution	execvp()
Zombie Process	Parent not calling wait()
Orphan Process	Parent exits before child
Kernel Process Info	/proc/<pid>/...
Priority Scheduling	nice()
CPU-bound processes	Heavy loop of 10M iterations

### 🧑‍💻 Author
Parth Bhardwaj
B.Tech CSE (AIML)
2301730289
SECTION - E 
Operating Systems Lab – Process Management

