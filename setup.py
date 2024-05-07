from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Описание из README.md
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="simple_wallet", 
    version="0.1.0", 
    description="Простой кошелек с балансом и транзакциями",  
    long_description=long_description,  
    url="https://github.com/drysmakhanova/simle_wallet", 

    packages=find_packages(include=['wallet', 'wallet.*']), 
    scripts=['wallet\main.py','wallet\helper_classes.py','wallet\helper_functions.py'], 
    entry_points={
        'console_scripts': [
            'simple_wallet=wallet.wallet:main'
        ]
    },
)