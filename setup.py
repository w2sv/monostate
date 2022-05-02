from setuptools import setup, find_packages

from monostate import __version__


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setup(
    name='monostate',
    packages=find_packages(exclude=(["tests"])),
    version=__version__,
    license='MIT',
    description='Dependency-free monostate owner base class',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords=['singleton', 'borg', 'design-patterns'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    url='https://github.com/w2sv/monostate',
    python_requires='>=3.6',
    author='w2sv',
    author_email='zangenbergjanek@googlemail.com',
    platforms=['Linux', 'Windows', 'MacOS']
)