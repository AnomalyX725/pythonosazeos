import time
import os
from system import system_startup  # Import właściwej funkcji

# ASCII art do wyświetlenia
ascii_art = r"""
 .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |      __      | || |   ________   | || |  _________   | || |     ____     | || |    _______   | |
| |     /  \     | || |  |  __   _|  | || | |_   ___  |  | || |   .'    `.   | || |   /  ___  |  | |
| |    / /\ \    | || |  |_/  / /    | || |   | |_  \_|  | || |  /  .--.  \  | || |  |  (__ \_|  | |
| |   / ____ \   | || |     .'.' _   | || |   |  _|  _   | || |  | |    | |  | || |   '.___`-.   | |
| | _/ /    \ \_ | || |   _/ /__/ |  | || |  _| |___/ |  | || |  \  `--'  /  | || |  |`\____) |  | |
| ||____|  |____|| || |  |________|  | || | |_________|  | || |   `.____.'   | || |  |_______.'  | |
| |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 
"""

def clear_console():
    """Czyści konsolę."""
    os.system('cls' if os.name == 'nt' else 'clear')

def loading_animation(duration=5):
    """Wyświetla animację ładowania."""
    spinner = ['|', '/', '-', '\\']
    for _ in range(duration * 4):
        for frame in spinner:
            print(f"\rLoading {frame}", end='', flush=True)
            time.sleep(0.25)

def boot_sequence():
    """Uruchamia proces bootowania."""
    clear_console()
    print(ascii_art)
    print("\nBooting AzeLinux... Please wait.")
    loading_animation(3)
    print("\nAzeLinux boot completed.")
    system_startup()  # Uruchamia system.py

if __name__ == "__main__":
    boot_sequence()