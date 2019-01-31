from setuptools import setup, find_packages, find_namespace_packages

VERSION = "v0.2.4"
DESCRIPTION = "Contains classes to represent a workflow, and provide options to convert to CWL / WDL"

######## SHOULDN'T NEED EDITS BELOW THIS LINE ########

with open("./janis/README.md") as readme:
    long_description = readme.read()

setup(
    name="janis pipelines",
    version=VERSION,
    description=DESCRIPTION,
    url="https://github.com/PMCC-BioinformaticsCore/janis",
    author="Michael Franklin, Evan Thomas, Mohammad Bhuyan",
    author_email="michael.franklin@petermac.org",
    license="GNU",
    packages=["janis"] + sorted(find_packages('./janis')),
    install_requires=["ruamel.yaml==0.15.77", "networkx==2.1", "six"],
    zip_safe=False,
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Bio-Informatics'
    ],
    extras_require={
        'bioinformatics': ['bioinformatics']
    }
)
