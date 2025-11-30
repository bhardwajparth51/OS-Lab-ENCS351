# Task 3: System Calls and IPC (fork, exec, pipe)
import os

def main():
    r, w = os.pipe()
    pid = os.fork()

    if pid > 0:
        # Parent
        os.close(r)
        os.write(w, b"Hello from Parent Process using pipe!")
        os.close(w)
        os.wait()
    else:
        # Child
        os.close(w)
        msg = os.read(r, 1024)
        print("Child received:", msg.decode())
        os.close(r)

if __name__ == "__main__":
    main()
