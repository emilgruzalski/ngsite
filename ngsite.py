import os
import re
from colorama import Fore, Style

# Directories for Nginx server configurations
nginx_available_dir = "/etc/nginx/sites-available"
nginx_enabled_dir = "/etc/nginx/sites-enabled"

def find_matching_configs(directory, pattern):
    matches = []
    active_configs = set(os.listdir(nginx_enabled_dir))
    regex_pattern = re.compile(pattern)
    for root, dirs, files in os.walk(directory):
        for file in files:
            if regex_pattern.match(file):
                match_status = "ENABLED" if file in active_configs else "DISABLED"
                matches.append((file, match_status))
    return matches

def list_configs(regex):
    print(f"{Fore.YELLOW}Listing matching Nginx configurations:{Style.RESET_ALL}")
    matches = find_matching_configs(nginx_available_dir, regex)
    for match, status in matches:
        print(f"{match} - {status}")

def enable_configs(regex):
    matches = find_matching_configs(nginx_available_dir, regex)
    for match, status in matches:
        if status == "DISABLED":
            os.symlink(os.path.join(nginx_available_dir, match), os.path.join(nginx_enabled_dir, match))
            print(f"{Fore.GREEN}Enabled {match}{Style.RESET_ALL}")

def disable_configs(regex):
    matches = find_matching_configs(nginx_enabled_dir, regex)
    for match, status in matches:
        if status == "ENABLED":
            os.remove(os.path.join(nginx_enabled_dir, match))
            print(f"{Fore.RED}Disabled {match}{Style.RESET_ALL}")

def main_menu():
    while True:
        print("\nMenu:")
        print("1. List configurations")
        print("2. Enable configurations")
        print("3. Disable configurations")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            regex = input("Enter a regular expression to LIST configurations: ")
            list_configs(regex)
        elif choice == "2":
            regex = input("Enter a regular expression to ENABLE configurations: ")
            enable_configs(regex)
        elif choice == "3":
            regex = input("Enter a regular expression to DISABLE configurations: ")
            disable_configs(regex)
        elif choice == "4":
            break
        else:
            print(f"{Fore.RED}Invalid choice, please try again.{Style.RESET_ALL}")

if __name__ == "__main__":
    main_menu()
