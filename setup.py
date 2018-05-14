#!/usr/bin/env python3

from setuptools import setup, find_packages
import histogram

setup(
    name = 'histogram',
    description = histogram.__doc__.strip(),
    url = 'https://github.com/nul-one/histogram',
    download_url = 'https://github.com/nul-one/histogram/archive/'+histogram.__version__+'.tar.gz',
    version = histogram.__version__,
    author = histogram.__author__,
    author_email = histogram.__author_email__,
    license = histogram.__licence__,
    packages = [ 'histogram' ],
    entry_points={ 
        'console_scripts': [
            'histogram=histogram.__main__:main',
        ],
    },
    install_requires = [
    ],
    python_requires=">=3.4.6",
)

