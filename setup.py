import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='smithwaterman',
    version='1.1',
    author='Ian Neidel',
    author_email='ian.neidel@yale.edu',
    description='An implementation of the Smith-Waterman algorithm, supporting an affine gap penalty',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/ianneidel/affine-smith-waterman',
    project_urls = {
        "Bug Tracker": "https://github.com/ianneidel/affine-smith-waterman/issues"
    },
    license='GPL',
    packages=['smithwaterman'],
    install_requires=['numpy','pandas','argparse'],
)