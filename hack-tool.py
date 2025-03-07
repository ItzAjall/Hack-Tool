import random
import time

# Failure rate configuration: 
# 100 = 1% failure chance, 200 = 0.5% failure chance, etc.
FAILRATE: int = 100  
PREFIX1: str = "█"
PREFIX2: str = "-"
DELAY: float = 0.1  
PROGRESSBAR_SIZE: int = 40

def checkIp(ip: str) -> bool:
    """
    This function checks whether the given IP address is valid.
    It splits the IP into 4 parts and ensures each part is a digit between 0 and 255.
    """
    parts = ip.split('.')
    if len(parts) != 4:
        return False 
    
    for part in parts:
        if not part.isdigit():
            return False
        if not 0 <= int(part) <= 255:
            return False
    
    return True

def failed() -> int:
    """
    Simulates a failure with a 1 in `FAILRATE` chance.
    A value of 1 represents failure, while any other value represents success.
    """
    return random.randint(1, FAILRATE)

def ProgressBar() -> None:
    """
    This function simulates a progress bar that fills up over time.
    It also checks for failure (based on `failed()` function), and stops the progress if failure occurs.
    """
    flag: bool = False
    for i in range(1, PROGRESSBAR_SIZE + 1):
        percent = (i * 100) / PROGRESSBAR_SIZE
        
        print(f"| {i * PREFIX1}{'' if i == PROGRESSBAR_SIZE else '/' if i % 2 == 0 else '\\'}{(PROGRESSBAR_SIZE-i) * PREFIX2} | {percent:.2f}%", end="\r")
        
        if failed() == 1:
            flag = True
            break
        
        # Wait for the specified delay before updating the progress again
        time.sleep(DELAY)
    
    print("\nHack Sucssesful!!\n") if not flag else print("\nHack Failed!!\n")

while True:
    ip: str = input("Please enter IP: ")
    
    if not checkIp(ip):
        print("Invalid IP address. Please try again.")
        continue
        
    ProgressBar()
