# cis245-testbank

This is the group project for CIS 245.

## Authors

- Tobi W.
- Daniel T.
- Crenguta I. (GitHub username: crengutaibrian) - Database



## Poetry

Poetry is a python packaging and dependency management.

**Set up**:

- First clone repo in your preferred directory
- Next make sure you are in your repo directory
- Then in your terminal you type `poetry install`
- After the installation is complete to activate the poetry environment, in your terminal type `poetry shell`
- Now in your terminal you can type `code .` if you are using VSCode

**Commands to help you get started**:

* To add a library/module to poetry:
  * poetry add library/module
* To remove a library/module from poetry:
  * poetry remove library/module
* To view a list of commands available:
  * poetry list
* To view what libraries/modules are installed:
  * poetry show
  * poetry show --tree
* To run file, make sure you are either in the directory or that you point to it in terminal:
  * poetry run app/registration.py
  * poetry run registration.py
* To format py file using Black:
  * poetry run black app/registration.py
* To see your files performance based on pylints coding guidelines:
  * poetry run pylint app/registration.py

For more help with **[Poetry](https://python-poetry.org/docs/)**
