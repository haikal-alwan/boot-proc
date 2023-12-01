import time
import datetime

def steps(process_name, start, end, message):
    for progress in range(start, end + 1, 10):
        time.sleep(0.1)  # Delay 0.1 seconds
        print(f"\r{process_name} Progress: {progress}%", end='', flush=True)
    time.sleep(1)
    print("\r", end='', flush=True)  # Clear the line after completion
    print(f"{process_name}: {message}")

class BIOS:
    def __init__(self):
        self.boot_order = ["BootLoader"]

    def start(self):
        print("\033c", end="")
        time.sleep(1)
        print("BIOS: Starting boot process...")
        steps("BIOS", 0, 100, "Loading POST...")
        kernel = Kernel()
        kernel.start()

class Kernel:
    def __init__(self):
        self.computer_specs = {
            "RAM_FIRST": "Kingston Fury Beast 3200MHz 8GB",
            "RAM_SEC": "Kingston Fury Beast 3200MHz 8GB",
            "Storage": "Samsung 980 PRO M.2 SSD 1TB",
            "Graphics Card": "NVidia Geforce GTX 1660 6GB",
            "Keyboard": "Logitech K100",
            "Mouse": "Logitech M100",
            "Monitor": "Samsung 24 Inch Monitor",
            "Speaker": "Logitech Z120"
        }

    def start(self):
        time.sleep(1)
        print("\nKernel: Load Success...")
        self.check_components()
        bootloader = BootLoader()
        bootloader.start()

    def check_components(self):
        print("Checking components:")
        self.check_ram_first()
        self.check_ram_sec()
        self.check_ssd()
        self.check_graphics_card()
        self.check_input()
        self.check_output()

    def check_ram_first(self):
        steps("RAM Check", 0, 100, f"Checking RAM SLOT 1: {self.computer_specs['RAM_FIRST']}...")
        # Add your RAM checking logic here
        time.sleep(1)
        print("RAM: Check complete. No issues found.")

    def check_ram_sec(self):
        steps("RAM Check", 0, 100, f"Checking RAM SLOT 2: {self.computer_specs['RAM_SEC']}...")
        # Add your RAM checking logic here
        time.sleep(1)
        print("RAM: Check complete. No issues found.")

    def check_ssd(self):
        steps("SSD Check", 0, 100, f"Checking SSD: {self.computer_specs['Storage']}...")
        # Add your SSD checking logic here
        time.sleep(1)
        print("SSD: Check complete. No issues found.")

    def check_graphics_card(self):
        steps("Graphics Card Check", 0, 100, f"Checking Graphics Card: {self.computer_specs['Graphics Card']}...")
        # Add your graphics card checking logic here
        time.sleep(1)
        print("Graphics Card: Check complete. No issues found.")

    def check_input(self):
        steps("Keyboard Check", 0, 100, f"Checking Keyboard: {self.computer_specs['Keyboard']}...")
        # Add your graphics card checking logic here
        time.sleep(1)
        print("Keyboard: Check complete. No issues found.")
        #================================================================
        steps("Mouse Check", 0, 100, f"Checking Mouse: {self.computer_specs['Mouse']}...")
        # Add your graphics card checking logic here
        time.sleep(1)
        print("Mouse: Check complete. No issues found.")

    def check_output(self):
        steps("Monitor Check", 0, 100, f"Checking Monitor: {self.computer_specs['Monitor']}...")
        # Add your graphics card checking logic here
        time.sleep(1)
        print("Monitor: Check complete. No issues found.")
        #================================================================
        steps("Speaker Check", 0, 100, f"Checking Speaker: {self.computer_specs['Speaker']}...")
        # Add your graphics card checking logic here
        time.sleep(1)
        print("Speaker: Check complete. No issues found.")
        print("\n")

class BootLoader:
    def start(self):
        time.sleep(1)
        print("\nBootLoader: Load Success...")
        steps("BootLoader", 0, 100, "Loading Operating System...")
        osloader = OS()
        osloader.start()

class OS:
    def start(self):
        print("\033c", end="")
        time.sleep(1)
        print("\nWelcome: Starting the operating system...")
        steps("BlueberryOS", 0, 100, "Hello, User!")
        prompt = SimpleCommandPrompt()
        prompt.run()        

class SimpleCommandPrompt:
    def __init__(self):
        self.current_directory = "/"
        self.file_system = {
            "/": ["file1.txt", "file2.txt", "folder1"],
            "/folder1": ["file3.txt", "file4.txt"]
        }
        self.logged_in = False
        self.current_user = None
        self.users = {"user": "pass", "alwan": "123"}

    def run(self):
        while True:
            if self.logged_in:
                prompt = f"{self.current_directory} ({self.current_user})> "
            else:
                prompt = f"{self.current_directory}> "
            command = input(prompt)
            self.execute_command(command)

    def execute_command(self, command):
        command = command.lower()

        if command == "shutdown":
            print("Exiting Operating System.")
            exit()

        if not self.logged_in:
            if command == "login":
                self.login()
            else:
                print("Login required. Please enter 'login' to log in.")
            return

        if command == "dir":
            self.list_directory()
        elif command.startswith("cd "):
            path = command[3:]
            self.change_directory(path)
        elif command.startswith("mkdir "):
            new_folder_name = command[6:]
            self.create_directory(new_folder_name)
        elif command.startswith("rmdir "):
            folder_to_remove = command[6:]
            self.remove_directory(folder_to_remove)
        elif command == "date":
            self.show_date()
        elif command == "time":
            self.show_time()
        elif command == "help":
            self.show_help()
        else:
            print(f"Command not recognized: {command}")

    def login(self):
        if self.logged_in:
            print("You are already logged in.")
            return

        username = input("Enter username: ")
        password = input("Enter password: ")

        if self.users.get(username) == password:
            print("Login successful.")
            self.logged_in = True
            self.current_user = username
        else:
            print("Login failed. Check your username and password.")

    def list_directory(self):
        files = self.file_system.get(self.current_directory, [])
        for file in files:
            print(file)

    def change_directory(self, path):
        if path.startswith("/"):
            new_directory = path
        else:
            new_directory = f"{self.current_directory}/{path}"

        if new_directory in self.file_system:
            self.current_directory = new_directory
        else:
            print(f"Directory not found: {new_directory}")

    def create_directory(self, folder_name):
        new_folder_path = f"{self.current_directory}/{folder_name}"
        if new_folder_path not in self.file_system:
            self.file_system[new_folder_path] = []
            print(f"Directory '{folder_name}' created.")
        else:
            print(f"Directory '{folder_name}' already exists.")

    def remove_directory(self, folder_name):
        folder_path = f"{self.current_directory}/{folder_name}"
        if folder_path in self.file_system:
            del self.file_system[folder_path]
            print(f"Directory '{folder_name}' removed.")
        else:
            print(f"Directory '{folder_name}' not found.")

    def show_date(self):
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        print(f"Current date: {current_date}")

    def show_time(self):
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"Current time: {current_time}")

    def show_help(self):
        print("Available commands:")
        print("  dir               - List files and directories")
        print("  cd <path>         - Change current directory")
        print("  mkdir <name>      - Create a new directory")
        print("  rmdir <name>      - Remove a directory")
        print("  date              - Show current date")
        print("  time              - Show current time")
        print("  help              - Display this help message")
        print("  login             - Log in")
        print("  shutdown          - Exit")

#================================================================
bios = BIOS()
bios.start()