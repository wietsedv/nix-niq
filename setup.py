from setuptools import setup

setup(
    name='niq',
    description='Fast Nixpkgs Quering',
    author='Wietse de Vries',
    author_email='wietse.de.vries@rug.nl',
    packages=['niq'],
    entry_points={
        'console_scripts': ['niq=niq.cli:main'],
    },
    python_requires='>=3.6',
)
