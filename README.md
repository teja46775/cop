# Copilot Test Script

This repository contains a script, `copilot_test.py`, that displays the system uptime across Linux, macOS, and Windows platforms.

## Experience Using Copilot

I used GitHub Copilot to generate the initial version of `copilot_test.py`. Copilot produced the following code:

- It detects the operating system using the `platform` module.
- For Linux and macOS, it tries to read `/proc/uptime`. If unavailable (as on macOS), it falls back to the `uptime` command.
- For Windows, it executes `net stats srv` and extracts the uptime line.
- The script prints the system uptime in a human-readable format.

### Modifications

I made the following adjustments:

- Ensured the `subprocess.check_output(['uptime'])` call on macOS was only used if `/proc/uptime` does not exist.
- Added error handling for unsupported operating systems and subprocess exceptions.
- Reformatted the output for consistency across platforms.

### Testing

I tested the script on:
- **Linux**: Verified it reads from `/proc/uptime` and displays uptime correctly.
- **macOS**: Confirmed the fallback to `uptime` command works.
- **Windows**: Checked that running `net stats srv` extracts the correct uptime information.

No further modifications were needed after confirming cross-platform compatibility.

## How to Run the Script

1. **Clone the repository:**

    ```bash
    git clone https://github.com/teja46775/cop.git
    cd cop
    ```

2. **Run the script:**

    ```bash
    python copilot_test.py
    ```

    or, for Python 3 specifically:

    ```bash
    python3 copilot_test.py
    ```

**Note:**  
- On Windows, you may need to run the terminal as Administrator for `net stats srv` to work.
- No third-party dependencies are required; only Python's standard library is used.

---
```
