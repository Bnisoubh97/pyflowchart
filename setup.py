import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='pyflow',
    version='0.0.0',
    url='https://github.com/cdfmlr/pyflow',
    license='MIT',
    author='CDFMLR',
    author_email='cdfmlr@outlook.com',
    description='Python codes to Flowcharts.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",
    ],
    python_requires='>=3.6',
    install_requires=['astunparse'],
)
