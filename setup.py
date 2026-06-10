from setuptools import setup

setup(
    name="butterfly-garden",
    version="1.0.0",
    description="Animated butterfly garden in your terminal",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Ravi Sharma",
    py_modules=["butterfly"],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "butterfly=butterfly:main_cli",
        ],
    },
    classifiers=[
        "Environment :: Console :: Curses",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS",
    ],
)
