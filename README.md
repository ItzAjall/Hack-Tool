# IP Progress Bar Simulation

This project simulates a progress bar that fills up over time while checking the validity of an IP address. The progress bar has a chance to "fail" randomly based on a set failure rate. It is designed to simulate a network operation (like a "hack" attempt) with a visual progress bar.

---

## Features

- **IP Validation**: Checks if a provided IP address is in the correct format (IPv4).
- **Progress Bar**: Displays a progress bar with a dynamic filling effect.
- **Random Failure Simulation**: At each step of the progress bar, there’s a chance that the operation might fail.
- **Customizable Settings**:
  - Failure rate (`FAILRATE`): Set the probability of failure (e.g., 1% or 0.5%).
  - Progress bar size (`PROGRESSBAR_SIZE`): Adjust the length of the progress bar.
  - Delay (`DELAY`): Control the speed of the progress bar's filling.

---

## Installation

To run this project, you can simply clone the repository to your local machine and execute it.

### Clone the Repository:

```bash
git clone https://github.com/ItzAjall/Hack-Tool.git
```
Navigate to the Project Directory:
```bash
cd Hack-Tool
```
Run the Script:
```bash
python3 hack-tool.py
```
## Configuration
You can adjust the following parameters in the code:

- FAILRATE: Defines the chance of failure during the process. A higher value means a lower failure rate.

  - Example: FAILRATE = 100 means a 1% failure rate.
- PREFIX1 and PREFIX2: Characters used for the progress bar.

  - PREFIX1 = "█" (filled part)
  - PREFIX2 = "-" (empty part)
- DELAY: The time (in seconds) to wait before updating the progress bar.

  - Example: DELAY = 0.1 means 100 milliseconds between progress updates.
- PROGRESSBAR_SIZE: The number of characters in the progress bar.

  - Example: PROGRESSBAR_SIZE = 40 means the progress bar will have 40 segments.

## How It Works
1. IP Validation: The program will prompt you to enter an IP address. It validates if the address is a valid IPv4 address with 4 parts (e.g., 192.168.1.1).
2. Progress Bar: After entering a valid IP, a progress bar will start filling. The bar will display alternating / and \ characters to simulate a dynamic effect.
3. Random Failure: At each update of the progress bar, there’s a small chance that the operation might fail. If it does, the progress bar stops, and "Hack Failed!!" is displayed.
4. Customizable Simulation: You can modify the failure rate, delay, and progress bar size to suit your needs.
