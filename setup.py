from setuptools import setup, find_packages

setup(
    name='dryader',
    version='0.1.0',
    author='dobereiner',
    author_email='takulagin@gmail.com',
    description='A Python library for downloading datasets from DRYAD',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/dobereiner/dryader',
    packages=find_packages(),
    install_requires=[
        'requests',
        'tqdm'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
    entry_points={
        'console_scripts': [
            'dryader-cli=dryader.cli:main',
        ]
    },
)
