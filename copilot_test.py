import os
import platform
import subprocess

def get_uptime():
    system = platform.system()
    if system == "Linux" or system == "Darwin":
        # For Linux or macOS
        try:
            with open('/proc/uptime', 'r') as f:
                uptime_seconds = float(f.readline().split()[0])
                hours = int(uptime_seconds // 3600)
                minutes = int((uptime_seconds % 3600) // 60)
                seconds = int(uptime_seconds % 60)
                print(f"System Uptime: {hours} hours, {minutes} minutes, {seconds} seconds")
        except FileNotFoundError:
            # macOS does not have /proc/uptime, use 'uptime' command
            output = subprocess.check_output(['uptime']).decode()
            print(f"System Uptime: {output.strip()}")
    elif system == "Windows":
        # For Windows
        try:
            output = subprocess.check_output('net stats srv', shell=True).decode()
            for line in output.splitlines():
                if "Statistics since" in line:
                    print(f"System Uptime: {line.strip()}")
                    break
        except Exception as e:
            print(f"Error retrieving uptime: {e}")
    else:
        print("Unsupported operating system.")

if __name__ == "__main__":
    get_uptime()
