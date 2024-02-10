import os


def get_sites_available():
    """Pobiera listę dostępnych plików konfiguracyjnych."""
    sites_available_dir = '/etc/nginx/sites-available'
    return os.listdir(sites_available_dir)


def get_sites_enabled():
    """Pobiera listę włączonych plików konfiguracyjnych."""
    sites_enabled_dir = '/etc/nginx/sites-enabled'
    return os.listdir(sites_enabled_dir)


def enable_site(site_name):
    """Włącza witrynę."""
    sites_available_dir = '/etc/nginx/sites-available'
    sites_enabled_dir = '/etc/nginx/sites-enabled'

    # Sprawdź, czy plik konfiguracyjny istnieje
    if site_name not in get_sites_available():
        raise ValueError('Plik konfiguracyjny {} nie istnieje.'.format(site_name))

    # Utwórz link symboliczny do pliku konfiguracyjnego w katalogu sites-enabled
    os.symlink(os.path.join(sites_available_dir, site_name), os.path.join(sites_enabled_dir, site_name))

    # Uruchom ponownie serwer Nginx
    os.system('sudo service nginx restart')


def disable_site(site_name):
    """Wyłącza witrynę."""
    sites_enabled_dir = '/etc/nginx/sites-enabled'

    # Sprawdź, czy plik konfiguracyjny istnieje
    if site_name not in get_sites_enabled():
        raise ValueError('Plik konfiguracyjny {} nie jest włączony.'.format(site_name))

    # Usuń link symboliczny do pliku konfiguracyjnego z katalogu sites-enabled
    os.remove(os.path.join(sites_enabled_dir, site_name))

    # Uruchom ponownie serwer Nginx
    os.system('sudo service nginx restart')


def edit_site(site_name):
    """Edytuje konfigurację witryny."""
    # TODO: Zaimplementuj funkcję edytującą konfigurację witryny


def add_site(site_name):
    """Dodaje nową witrynę."""
    # TODO: Zaimplementuj funkcję dodającą nową witrynę


def delete_site(site_name):
    """Usuwa witrynę."""
    # TODO: Zaimplementuj funkcję usuwającą witrynę
