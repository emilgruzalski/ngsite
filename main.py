from __future__ import print_function
import inquirer

def main():
    # Lista dostępnych opcji
    options = [
        'Wyświetl listę dostępnych witryn',
        'Włącz witrynę',
        'Wyłącz witrynę',
        'Edytuj konfigurację witryny',
        'Dodaj nową witrynę',
        'Usuń witrynę',
        'Wyjdź',
    ]

    # Wyświetl menu i pobierz wybór użytkownika
    choice = inquirer.prompt([
        inquirer.List('choice', 'Wybierz opcję:', options),
    ])['choice']

    # Wykonaj wybraną opcję
    if choice == 'Wyświetl listę dostępnych witryn':
        list_sites()
    elif choice == 'Włącz witrynę':
        enable_site()
    elif choice == 'Wyłącz witrynę':
        disable_site()
    elif choice == 'Edytuj konfigurację witryny':
        edit_site()
    elif choice == 'Dodaj nową witrynę':
        add_site()
    elif choice == 'Usuń witrynę':
        delete_site()
    elif choice == 'Wyjdź':
        exit()

def list_sites():
    # TODO: Zaimplementuj funkcję wyświetlającą listę dostępnych witryn

def enable_site():
    # TODO: Zaimplementuj funkcję włączającą witrynę

def disable_site():
    # TODO: Zaimplementuj funkcję wyłączającą witrynę

def edit_site():
    # TODO: Zaimplementuj funkcję edytującą konfigurację witryny

def add_site():
    # TODO: Zaimplementuj funkcję dodającą nową witrynę

def delete_site():
    # TODO: Zaimplementuj funkcję usuwającą witrynę

if __name__ == '__main__':
    main()
