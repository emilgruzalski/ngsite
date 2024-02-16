from setuptools import setup

setup(
    name='ngsite',
    version='0.1.0',
    description='Aplikacja CLI do zarządzania sites-enabled i sites-available w Nginx',
    author='Emil Grużalski',
    author_email='emilgruzalski@gmail.com',
    url='https://github.com/emilgruzalski/ngsite',
    packages=['ngsite'],
    install_requires=[
        'PyInquirer',
    ],
    entry_points={
        'console_scripts': [
            'ngsite = ngsite.main:main',
        ],
    },
)
