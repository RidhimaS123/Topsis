from setuptools import setup, find_packages

# Read the contents of the README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="topsis",  
    version="1.0.0",
    author="RidhimaSharma_102203709",  
    author_email="rsharma1_be22@thapar.edu", 
    description="A Python implementation of the TOPSIS multi-criteria decision-making method.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/RidhimaS123/Topsis",  # Replace with your repository URL
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "numpy",
        "pandas",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'topsis=topsis.__main__:main',  
        ],
    },
)
