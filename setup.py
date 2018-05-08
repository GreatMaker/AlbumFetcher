from setuptools import setup

config = {
        'description': 'Album fetcher',
        'author': 'Andrea Visinoni',
        'url': 'URL',
        'download_url': 'WHERE TO DOWNLOAD IT',
        'author_email': 'andrea.visinoni@gmail.com',
        'version': '0.0.1',
        'install_requires': [],
        'packages': ['album_fetcher'],
        'scripts': [],
        'name': 'album_fetcher'
}

# Add in any extra build steps for cython, etc.

setup(**config)