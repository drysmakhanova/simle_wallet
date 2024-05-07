from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Описание из README.md
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="simple_wallet", 
    version="1.0.0",  # Required
    description="Простой кошелек с балансом и транзакциями",  
    long_description=long_description,  
    url="https://github.com/drysmakhanova/simle_wallet", 
    # You can just specify package directories manually here if your project is
    # simple. Or you can use find_packages().
    #
    # Alternatively, if you just want to distribute a single Python file, use
    # the `py_modules` argument instead as follows, which will expect a file
    # called `my_module.py` to exist:
    #
    #   py_modules=["my_module"],
    #
    packages=find_packages(where="src"),  # Required
    python_requires=">=3.7, <4",
    # This field lists other packages that your project depends on to run.
    # Any package you put here will be installed by pip when your project is
    # installed, so they must be valid existing projects.
    #
    # For an analysis of "install_requires" vs pip's requirements files see:
    # https://packaging.python.org/discussions/install-requires-vs-requirements/
    install_requires=["peppercorn"],  # Optional
)