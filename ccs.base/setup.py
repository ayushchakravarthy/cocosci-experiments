#!/usr/bin/env python

import os
import sys

from setuptools import setup, find_packages


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

try:
    import pypandoc
    readme = pypandoc.convert('README.md', 'rst')
    history = pypandoc.convert('CHANGELOG.md', 'rst')
except (IOError, ImportError):
    readme = open('README.md').read()
    history = open('CHANGELOG.md').read()

# Get rid of Sphinx markup
history = history.replace('.. :changelog:', '')

setup_args = dict(
    name='ccs.base',
    version='0.1.0',
    description='A simple Intergenerational Goods Game with no social comparison',
    long_description=readme + '\n\n' + history,
    author='Ayush Chakravarthy',
    author_email='akchakravarthy@ucdavis.edu',
    url='https://github.com/ayushchakravarthy/ccs.base',
    packages=find_packages('.'),
    package_dir={'': '.'},
    namespace_packages=['ccs'],
    include_package_data=True,
    install_requires=[
        'setuptools',
    ],
    license='MIT',
    zip_safe=False,
    keywords='Dallinger base',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
    ],
    entry_points={
        'dallinger.experiments': [
            'IGG = ccs.base.experiment:IGG',
        ],
    },
    extras_require={
        'test': [
            'pytest',
            'selenium',
            'pexpect',
        ]
    }
)

setup(**setup_args)
