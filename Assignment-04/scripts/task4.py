# Task 4: Virtual Machine Detection (Python)
import subprocess

def detect_vm():
    try:
        result = subprocess.check_output(["systemd-detect-virt"], text=True).strip()
        if result == "none":
            print("No Virtual Machine detected.")
        else:
            print("Running inside a Virtual Machine:", result)
    except Exception:
        print("VM detection tool not available. Try installing systemd-detect-virt.")

if __name__ == "__main__":
    detect_vm()
