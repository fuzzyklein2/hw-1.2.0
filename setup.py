# setup.py
from setuptools import setup, find_packages

setup(
    name="hw",
    version="1.2.0",
    packages=find_packages(),
    include_package_data=True,  # include non-Python files listed in MANIFEST.in
    install_requires=[
        # "beautifulsoup4",
        # "pycairo",
        # "PyGObject",
        # "markdown",
        # "regex"
        'pygnition'
    ],
    python_requires=">=3.12",
    entry_points={
        # Optional: if you have a CLI script
        "console_scripts": [
            "hw.cli = hw.main:main"
        ]
    },
)
