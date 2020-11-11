import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django-durationwidget2",
    version="1.0.6",
    author="Simone Pozzoli",
    author_email="simonepozzoli1@gmail.com",
    description="Django Duration field widget to handle duration field in the form",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pozzolana93/django-durationwidget",
    packages=setuptools.find_packages(),
    install_requires=[
        'Django>=1.11',
    ],
    classifiers=[
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
)
