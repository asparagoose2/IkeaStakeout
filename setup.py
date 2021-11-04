from setuptools import setup, find_packages

setup(
    name='IkeaStakeout',
    version='1.0.0',
    packages=find_packages(),
    description='Telepytgram Ikea updater bot',
    install_requires=['emoji', 'aiogram', 'aiohttp', 'click'],
    python_requires=">=3.7",
    license='GPLv3',
    author='Ofir Duchovne',
    entry_points={
        'console_scripts': [
            'run_IkeaStakeout = IkeaStakeout.main:main'
        ]
    }
)
