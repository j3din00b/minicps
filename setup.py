#!/usr/bin/env python2
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# NOTE: https://docs.python.org/2/distutils/setupscript.html
setup(
    name='minicps',
    version='1.1.0',
    description='MiniCPS: a framework for Cyber-Physical Systems \
    real-time simulation, built on top of mininet.',
    # NOTE: long_description displayed on PyPi
    long_description='MiniCPS is a framework for Cyber-Physical Systems \
    real-time simulation. It includes support for physical process and \
    control devices simulation, and network emulation. It is build \
    on top of mininet.',
    url='https://github.com/scy-phy/minicps',
    author='Daniele Antonioli',
    author_email='antonioli.daniele@gmail.com',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='simulation cyber-physical systems security real-time mininet',
    packages=['minicps'],
    # packages=find_packages(exclude=['docs', 'tests*', 'examples', 'temp',
    # 'bin']),
    # NOTE: for the uses, see requirements for the developer
    install_requires=[
        'cryptography',
        'pyasn1',
        'pymodbus',
        'cpppo',
    ],
    # NOTE: specify files relative to the module path
    package_data={},
    # NOTE: specify files with absolute paths
    data_files=None,
    scripts=[],
)

