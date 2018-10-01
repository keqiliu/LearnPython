try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'my project ex48',
    'author': 'peppa keqi',
    'url': 'to be test',
    'download_url': 'Where to download',
    'author_email': 'keqi@smile.net',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex47'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)
