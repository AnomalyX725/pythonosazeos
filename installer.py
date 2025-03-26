import os
import shutil
import subprocess
import sys

def print_instructions(step):
    """
    Wyświetla instrukcję dla konkretnego kroku instalacji.
    """
    instructions = {
        1: "\nStep 1: Checking and installing dependencies...",
        2: "\nStep 2: Selecting installation directory...",
        3: "\nStep 3: Copying necessary files...",
        4: "\nStep 4: Finalizing installation...",
    }
    print(instructions.get(step, "\nUnknown Step"))

def install_dependencies():
    """
    Instalacja zależności z pliku dependencies.txt.
    """
    print_instructions(1)
    dependencies_file = "dependencies.txt"
    if os.path.exists(dependencies_file):
        with open(dependencies_file, "r") as file:
            for line in file:
                dependency = line.strip()
                if dependency:
                    print(f"Installing {dependency}...")
                    subprocess.check_call([sys.executable, "-m", "pip", "install", dependency])
    else:
        print("No dependencies.txt file found. Skipping dependency installation.")

def select_directory():
    """
    Prowadzi użytkownika przez wybór lokalizacji instalacji.
    """
    print_instructions(2)
    default_path = os.path.expanduser("~/AzeOS")
    print(f"Default installation path: {default_path}")
    user_path = input("Enter installation directory (press Enter to use default): ").strip()
    return user_path or default_path

def copy_files(destination):
    """
    Kopiowanie plików do wybranego folderu instalacji.
    """
    print_instructions(3)
    os.makedirs(destination, exist_ok=True)  # Tworzy folder, jeśli nie istnieje
    files_to_copy = ["sysboot.py", "system.py", "config.txt"]
    for file_name in files_to_copy:
        if os.path.exists(file_name):
            print(f"Copying {file_name} to {destination}...")
            shutil.copy(file_name, destination)
        else:
            print(f"File {file_name} not found in main directory. Skipping.")

def finalize_installation(destination):
    """
    Finalizuje proces instalacji i wyświetla instrukcje dalszego postępowania.
    """
    print_instructions(4)
    print(f"\nInstallation completed successfully in {destination}!")
    print("\n========================================")
    print("To run AzeOS:")
    print(f"1. Navigate to the installation directory: cd {destination}")
    print("2. Execute the following command: python sysboot.py")
    print("========================================\n")

def main():
    """
    Główna funkcja prowadząca użytkownika przez proces instalacji.
    """
    print("\n========================================")
    print("          Welcome to AzeOS Installer")
    print("Follow the instructions below to complete the installation.")
    print("========================================\n")

    install_dependencies()
    destination = select_directory()
    copy_files(destination)
    finalize_installation(destination)

if __name__ == "__main__":
    main()
