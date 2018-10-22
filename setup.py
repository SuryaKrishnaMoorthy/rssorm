from rssorm import __version__
from setuptools import setup, find_packages


APP_NAME = 'rssorm'
VERSION = __version__
AUTHOR = 'James Hibbard'

setup(
    name=APP_NAME,
    version=VERSION,
    author=AUTHOR,
    description="RSS controller",
    license="MIT",
    install_requires=[
        'Click==7.0',
        'appdirs==1.4.3',
        'ldap3==2.5.1',
        'requests==2.19.1',
        'SQLAlchemy==1.2.12',
    ],
    extras_require={
        'tests': ['pytest==3.8.1'],
    },
    packages=find_packages(),
    entry_points='''
        [console_scripts]
        orm=rssorm.runner:cli
    ''',
)
