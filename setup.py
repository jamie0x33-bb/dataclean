from distutils.core import setup

setup(
    name="dataclean",
    version="0.2.1",
    description="Lightweight CSV data cleaning utility",
    author="jm",
    packages=["dataclean"],
    entry_points={
        "console_scripts": [
            "dataclean=dataclean.cli:main",
        ],
    },
    python_requires=">=3.8",
)
