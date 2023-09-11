import setuptools

with open("README.md", "r", encoding="utf-8") as file:
    long_description = file.read()

setuptools.setup(
    name                            = "PyTrivialOpenGL",
    version                         = "0.1.2",
    author                          = "underwatergrasshopper",
    description                     = "Simple python package which provides tools to create OpneGL window.",
    long_description                = long_description,
    long_description_content_type   = "text/markdown",
    url                             = "https://github.com/underwatergrasshopper/PyTrivialOpenGL",
    project_urls                    = {
        "Bug Tracker": "https://github.com/underwatergrasshopper/PyTrivialOpenGL/issues",
    },
    classifiers                     = [
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
    ],
    package_dir                     = {"": "src"},
    packages                        = setuptools.find_packages(where = "src"),
    install_requires                = [],
    license                         = "MIT",
    python_requires                 = "~=3.9",
)