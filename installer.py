import os
import shutil
import subprocess
import sys

def install_dependencies():
    """
    Instalacja zależności z pliku dependencies.txt.
    """
    dependencies_file = os.path.join("install", "dependencies.txt")
    if os.path.exists(dependencies_file):
        print("Installing dependencies...")
        with open(dependencies_file, "r") as file:
            for line in file:
                dependency = line.strip()
                if dependency:
                    print(f"Installing {dependency}...")
                    subprocess.check_call([sys.executable, "-m", "pip", "install", dependency])
    else:
        print("No dependencies.txt file found. Skipping dependency installation.")

def create_folder(destination):
    """
    Tworzenie folderu AzeOS w wybranej lokalizacji.
    """
    final_path = os.path.join(destination, "AzeOS")
    os.makedirs(final_path, exist_ok=True)  # Tworzy folder AzeOS, jeśli nie istnieje
    return final_path

def copy_files(destination):
    """
    Kopiowanie plików z folderu install do wybranego folderu AzeOS.
    """
    files_to_copy = ["sysboot.py", "system.py", "config.txt"]
    for file_name in files_to_copy:
        source = os.path.join("install", file_name)
        if os.path.exists(source):
            print(f"Copying {file_name} to {destination}...")
            shutil.copy(source, destination)
        else:
            print(f"{file_name} not found in install directory. Skipping.")

def finalize_installation(destination):
    """
    Finalne kroki instalacji.
    """
    print("\nFinalizing installation...")
    print(f"All files and dependencies have been installed successfully in {destination}!")
    print("\n========================================")
    print("To run AzeOS:")
    print(f"1. Navigate to the installation directory: cd {destination}")
    print("2. Execute the following command: python sysboot.py")
    print("========================================\n")

def main():
    """
    Główna funkcja instalatora z możliwością wyboru lokalizacji.
    """
    print("\n========================================")
    print("          AzeOS Installer")
    print("========================================\n")

    install_dependencies()
    
    # Pytanie użytkownika o lokalizację instalacji
    default_path = os.path.expanduser("~/AzeOS")
    print(f"Default installation path: {default_path}")
    destination = input("Enter installation directory (press Enter to use default): ").strip() or default_path
    
    # Tworzenie folderu AzeOS
    final_path = create_folder(destination)
    print(f"Installing AzeOS in: {final_path}\n")

    copy_files(final_path)
    finalize_installation(final_path)

if __name__ == "__main__":
    main()
