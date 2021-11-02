from setuptools import setup, find_packages

from monostate import __version__

setup(
    name='monostate',
    packages=find_packages(exclude=(["*.tests", "*.tests.*", "tests.*", "tests"])),
    version=__version__,
    license='MIT',
    keywords=['singleton', 'borg'],
    url='https://github.com/w2sv/monostate',
    python_requires='>=3.6',
    author='w2sv',
    author_email='zangenbergjanek@googlemail.com',
    platforms=['Linux', 'Windows', 'MacOS'],
    description='Monostate class interface'
)
