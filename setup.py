import setuptools

with open("README.md", "r", encoding="utf-8") as file:
    long_description = file.read()

setuptools.setup(
    name="jg",
    version="0.0.1",
    author="Alison Y. Kim and Naomi Bleiker",
    description="A package that processes, filters and generates jokes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=["jg"],
    package_data={
        "jg": ["data/reddit_dadjokes.csv", "data/profanities.txt"],
    },
    python_requires=">=3.8",
    entry_points={
                        'console_scripts': ["jg=jg.CLI:main"]
    }
)