# snappy-scripts
Python program, that takes a json file (which contains the information
of a directory in nested structure) and prints out its content in the console in
the style of ls (linux utility).

# Dependencies
Python 3
pip modules described in requirements.txt

# Build
Best practice is to use a virtual environment:

python3 -m venv .venv
source .venv/bin/activate
Go to the directory in which the setup.py file for the vm_snapshot exists.
To install the package directly using the setup.py file run:

pip install .
You can add the -e flag if you want to test locally and the code changes should be reflected when executing the script.

To create a build package run:

python3 setup.py build sdist

After create a main.py file and import module

from pys import main

## Install
Installation instructions are provided on the corresponding agent README file.

## Configuration
Configuration instructions are provided on the corresponding agent README file.

## Usage
Usage instructions are provided on the corresponding agent README file.

## Adding new Agents
When implementing new agents, place each agent in a folder under the corresponding structure mentioned below:


Additionally to this, make sure to include a README.me file on the agent's root folder with the following information:
- Agent Description
- Installation instructions
- Usage details (how to run it, expected arguments, samples)
