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
        2: "\nStep 2: Creating installation directory...",
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

def create_directory():
    """
    Tworzy folder `AzeOS` w wybranej lokalizacji instalacyjnej.
    """
    print_instructions(2)
    default_path = os.path.expanduser("~/AzeOS")  # Domyślna lokalizacja instalacji
    print(f"Default installation path: {default_path}")
    user_path = input("Enter installation directory (press Enter to use default): ").strip()
    # Użycie domyślnego folderu lub własnej ścieżki
    final_path = user_path or default_path
    azeos_path = os.path.join(final_path, "AzeOS")  # Tworzenie folderu "AzeOS"
    os.makedirs(azeos_path, exist_ok=True)  # Upewnienie się, że folder istnieje
    print(f"Created directory: {azeos_path}")
    return azeos_path

def copy_files(destination):
    """
    Kopiuje pliki systemowe do folderu instalacyjnego.
    """
    print_instructions(3)
    files_to_copy = ["sysboot.py", "system.py", "config.txt"]
    for file_name in files_to_copy:
        if os.path.exists(file_name):
            print(f"Copying {file_name} to {destination}...")
            shutil.copy(file_name, destination)
        else:
            print(f"File {file_name} not found in main directory. Skipping.")

def finalize_installation(destination):
    """
    Finalizuje instalację i wyświetla instrukcje użytkownikowi.
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
    Główna funkcja prowadząca proces instalacji krok po kroku.
    """
    print("\n========================================")
    print("          Welcome to AzeOS Installer")
    print("Follow the instructions below to complete the installation.")
    print("========================================\n")

    install_dependencies()
    destination = create_directory()
    copy_files(destination)
    finalize_installation(destination)

if __name__ == "__main__":
    main()
