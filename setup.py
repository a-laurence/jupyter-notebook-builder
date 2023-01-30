from setuptools import setup, find_packages
from python_scripts.__version__ import __version__


if __name__ == "__main__":
    setup(
        name="jupyter-notebook-builder",
        version=__version__,
        author="Laurence P. Abanes",
        packages=find_packages(),
        include_package_data=True,
        install_requires=[
            "requests",
            "black",
            "install",
            "ipython",
            "jupyterlab"
        ],
        url="",
    )
