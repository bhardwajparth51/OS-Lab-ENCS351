# 🚀 Process Management Lab (Linux OS) - Assignment 01

_A Python-based demonstration of process creation, scheduling, zombie/orphan processes, `/proc` inspection, and command execution using `fork()` and `execvp()`._

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.6%2B-blue" />
  <img src="https://img.shields.io/badge/Linux-Required-success" />
  <img src="https://img.shields.io/badge/OS-Lab%20Experiment-orange" />
  <img src="https://img.shields.io/badge/Status-Completed-brightgreen" />
</p>

---

## 📌 Overview

This repository contains a complete implementation of system startup and process lifecycle simulation using Python. It covers:

🖥 System Startup Simulation

👶 Child Process Creation using multiprocessing

📝 Logging Process Start and End

🛑 Process Termination & Joining

📂 Generating process_log.txt to track process lifecycle

This project is ideal for OS lab submissions, process management learners, and Python scripting exercises.

---

## 🗂 Repository Structure

```
📦 System-Startup-Lab
├── main.py  # Main program implementing all tasks
├── process_log.txt       # Generated log file showing process lifecycle
├── README.md             # Instructions, usage, requirements
└── report.pdf/           # Lab report explaining implementation
```

---

## 🧰 Features

### ✔ System Startup

Prints `"System Starting..."` on the console.

### ✔ Multiprocessing

Creates multiple child processes that execute dummy tasks concurrently.

### ✔ Process Logging

Logs the start and end of each process with timestamps:

```
2025-11-30 18:12:01,123 - Process-1 - Process-1 started
2025-11-30 18:12:03,125 - Process-1 - Process-1 ended

```

✔ Process Termination

Ensures processes terminate properly using `join()` and prints `"System Shutdown..."`.

## ⚙️ Requirements

#### 🐧 OS

Works on Linux, Windows, or MacOS — no special OS-level dependencies.

#### 🐍 Python

`Python 3.6` or above.

✔ No external libraries required
Only uses Python standard libraries:

```
import multiprocessing
import time
import logging
```

### 📦 Setup & Installation

Clone the repository:

```
git clone https://github.com/bhardwajparth51/OS-Lab-ENCS351.git
cd Assignment-01
```

### ▶️ How to Run

Run the program:

`python3 main.py`
All output will be saved to `output.txt`.

-console output:

```
System Starting...
System Shutdown.
```

Check the 1process_log.txt` file to see detailed process start and end times.

### 🔍 Verify Logs

Sample `process_log.txt` content:
Check Zombie:

```
2025-11-30 18:12:01,123 - Process-1 - Process-1 started
2025-11-30 18:12:01,124 - Process-2 - Process-2 started
2025-11-30 18:12:03,125 - Process-1 - Process-1 ended
2025-11-30 18:12:03,126 - Process-2 - Process-2 ended
```

### 📘 Code Snippets

Running tasks:

```
print("System Starting...")

p1 = multiprocessing.Process(target=system_process, args=('Process-1',))
p2 = multiprocessing.Process(target=system_process, args=('Process-2',))

p1.start()
p2.start()

p1.join()
p2.join()

print("System Shutdown.")
```

### 📝 What This Project Demonstrates

| Concept                    | Demonstrated Through        |
| -------------------------- | --------------------------- |
| System Startup & Shutdown  | `print()` statements        |
| Process Creation           | `multiprocessing.Process()` |
| Logging Process Lifecycle  | `logging` module            |
| Process Termination & Join | `join()` method             |
| File Logging               | `process_log.txt`           |

### 🧑‍💻 Author

**Parth Bhardwaj**  
**B.Tech CSE (AIML)**  
**2301730289**  
**Section - E**
