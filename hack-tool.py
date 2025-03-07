import random
import time

# Failure rate configuration: 
# 100 = 1% failure chance, 200 = 0.5% failure chance, etc.
FAILRATE: int = 100  
# Character used for progress bar representation
PREFIX1: str = "█"
# Character used for empty space in the progress bar
PREFIX2: str = "-"
# Delay between progress updates, in seconds (0.1 sec here)
DELAY: float = 0.1  
# Size of the progress bar (how many characters it contains)
PROGRESSBAR_SIZE: int = 40

# Function to check if the provided IP is valid
def checkIp(ip: str) -> bool:
    """
    This function checks whether the given IP address is valid.
    It splits the IP into 4 parts and ensures each part is a digit between 0 and 255.
    """
    # Split IP address by periods to separate into parts
    parts = ip.split('.')
    # Check if there are exactly 4 parts in the IP
    if len(parts) != 4:
        return False  # If not, return False indicating invalid IP
    
    # Check each part of the IP
    for part in parts:
        if not part.isdigit():  # If the part is not a digit, return False
            return False
        # If the part is not between 0 and 255, return False
        if not 0 <= int(part) <= 255:
            return False
    
    # If all checks pass, the IP is valid
    return True

# Function to simulate failure with a specific chance
def failed() -> int:
    """
    Simulates a failure with a 1 in `FAILRATE` chance.
    A value of 1 represents failure, while any other value represents success.
    """
    return random.randint(1, FAILRATE)

# Function to display a progress bar
def ProgressBar() -> None:
    """
    This function simulates a progress bar that fills up over time.
    It also checks for failure (based on `failed()` function), and stops the progress if failure occurs.
    """
    # Loop to update progress bar
    for i in range(1, PROGRESSBAR_SIZE + 1):
        # Calculate the percentage of completion
        percent = (i * 100) / PROGRESSBAR_SIZE
        
        # Print progress bar with alternating / and \ characters for a dynamic look
        print(f"| {i * PREFIX1}{'' if i == PROGRESSBAR_SIZE else '/' if i % 2 == 0 else '\\'}{(PROGRESSBAR_SIZE-i) * PREFIX2} | {percent:.2f}%", end="\r")
        
        # Check if the process has failed
        if failed() == 1:
            # If failure occurs, display a message and stop the progress
            print("\nHack Failed!!")
            break
        
        # Wait for the specified delay before updating the progress again
        time.sleep(DELAY)
    
    # Print a newline after the progress bar is finished (or interrupted)
    print("\n")  

# Main loop to ask the user for an IP address and simulate progress bar
while True:
    # Ask the user to input an IP address
    ip: str = input("Please enter IP: ")
    
    # Check if the entered IP address is valid
    if not checkIp(ip):
        # If the IP is invalid, inform the user and ask again
        print("Invalid IP address. Please try again.")
        continue  # Skip to the next iteration of the loop
    
    # If the IP is valid, show the progress bar simulation
    ProgressBar()
