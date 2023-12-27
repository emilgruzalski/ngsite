# NgSite - Nginx Sites Management

## Description
This tool provides an interactive way to manage Nginx server configurations. It allows users to list, enable, or disable configurations based on user-defined regular expressions, streamlining the management of Nginx configurations.

## Features
- **List Configurations**: Users can input a regular expression to filter and list Nginx server configurations, displaying whether they are enabled or disabled.
- **Enable Configurations**: Input a regular expression to identify and enable specific Nginx server configurations.
- **Disable Configurations**: Input a regular expression to identify and disable specific Nginx server configurations.

## Requirements
- Python 3.x
- `colorama`
- Nginx installed on your system
- Access to /etc/nginx/sites-available and /etc/nginx/sites-enabled directories

## Installation
Ensure Python and Nginx are installed on your system. Additionally, the `colorama` library is required for colored terminal output. Install it using the following command:
```bash
pip install colorama
```

## Usage
To use the tool, run the script and choose an option from the menu:
```bash
python ngsite.py
```
- `1`: List configurations (using a regular expression).
- `2`: Enable configurations (using a regular expression).
- `3`: Disable configurations (using a regular expression).
- `4`: Exit the script.

## License
This project is licensed under the MIT License.
