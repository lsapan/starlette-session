import setuptools

setuptools.setup(
    name="starlette-session",
    version="0.4.1",
    author="auredentan",
    description="",
    long_description="",
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[],
    python_requires='>=3.6',
    py_modules=["quicksample"],
    package_dir={'':'quicksample/src'},
    install_requires=['starlette'],
)
