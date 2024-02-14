from __future__ import print_function

import inquirer
from utils import (
    get_sites_available,
    get_sites_enabled,
    enable_site,
    disable_site,
    edit_site,
    add_site,
    delete_site,
)


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
    """Wyświetla listę dostępnych witryn."""
    sites_available = get_sites_available()
    sites_enabled = get_sites_enabled()

    print('Dostępne witryny:')
    for site in sites_available:
        print('  - {}'.format(site))

    print('Włączone witryny:')
    for site in sites_enabled:
        print('  - {}'.format(site))


def enable_site():
    """Włącza witrynę."""
    sites_available = get_sites_available()

    # Wybór witryny do włączenia
    site_name = inquirer.prompt([
        inquirer.List('site_name', 'Wybierz witrynę do włączenia:', sites_available),
    ])['site_name']

    enable_site(site_name)


def disable_site():
    """Wyłącza witrynę."""
    sites_enabled = get_sites_enabled()

    # Wybór witryny do wyłączenia
    site_name = inquirer.prompt([
        inquirer.List('site_name', 'Wybierz witrynę do wyłączenia:', sites_enabled),
    ])['site_name']

    disable_site(site_name)


def edit_site():
    """Edytuje konfigurację witryny."""
    sites_available = get_sites_available()

    # Wybór witryny do edycji
    site_name = inquirer.prompt([
        inquirer.List('site_name', 'Wybierz witrynę do edycji:', sites_available),
    ])['site_name']

    # TODO: Zaimplementuj edycję konfiguracji witryny


def add_site():
    """Dodaje nową witrynę."""
    # TODO: Zaimplementuj dodanie nowej witryny


def delete_site():
    """Usuwa witrynę."""
    sites_enabled = get_sites_enabled()

    # Wybór witryny do usunięcia
    site_name = inquirer.prompt([
        inquirer.List('site_name', 'Wybierz witrynę do usunięcia:', sites_enabled),
    ])['site_name']

    delete_site(site_name)


if __name__ == '__main__':
    main()
