import os
import re
import sys
from termcolor import colored

def list_sites(directory, pattern):
    try:
        files = os.listdir(directory)
    except OSError as e:
        print(colored(f"Error accessing directory: {e}", 'red'))
        return []

    regex = re.compile(pattern)
    return [f for f in files if regex.search(f)]

def enable_site(site):
    source = f"/etc/nginx/sites-available/{site}"
    destination = f"/etc/nginx/sites-enabled/{site}"
    try:
        os.symlink(source, destination)
        print(colored(f"Site {site} enabled successfully.", 'green'))
    except OSError as e:
        print(colored(f"Error enabling site {site}: {e}", 'red'))

def disable_site(site):
    path = f"/etc/nginx/sites-enabled/{site}"
    try:
        os.remove(path)
        print(colored(f"Site {site} disabled successfully.", 'green'))
    except OSError as e:
        print(colored(f"Error disabling site {site}: {e}", 'red'))

def interactive_menu():
    while True:
        print(colored("\nNGINX Sites Manager", 'cyan', attrs=['bold']))
        print("1. Enable a site")
        print("2. Disable a site")
        print("3. List enabled sites")
        print("4. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            pattern = input("Enter regex pattern for site to enable: ")
            sites = list_sites("/etc/nginx/sites-available", pattern)
            if sites:
                print("Matching sites:")
                for i, site in enumerate(sites, start=1):
                    print(f"{i}. {site}")
                site_index = int(input("Enter site number to enable: ")) - 1
                if 0 <= site_index < len(sites):
                    enable_site(sites[site_index])
                else:
                    print(colored("Invalid selection.", 'red'))
            else:
                print(colored("No matching sites found.", 'yellow'))

        elif choice == '2':
            pattern = input("Enter regex pattern for site to disable: ")
            sites = list_sites("/etc/nginx/sites-enabled", pattern)
            if sites:
                print("Matching sites:")
                for i, site in enumerate(sites, start=1):
                    print(f"{i}. {site}")
                site_index = int(input("Enter site number to disable: ")) - 1
                if 0 <= site_index < len(sites):
                    disable_site(sites[site_index])
                else:
                    print(colored("Invalid selection.", 'red'))
            else:
                print(colored("No matching sites found.", 'yellow'))

        elif choice == '3':
            sites = os.listdir("/etc/nginx/sites-enabled")
            if sites:
                print("Enabled sites:")
                for site in sites:
                    print(site)
            else:
                print(colored("No sites are currently enabled.", 'yellow'))

        elif choice == '4':
            print("Exiting...")
            break
        else:
            print(colored("Invalid choice. Please select a valid option.", 'red'))

if __name__ == "__main__":
    interactive_menu()
