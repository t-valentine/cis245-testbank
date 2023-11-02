# cis245-testbank

This is the group project for CIS 245.

## Authors

- Tobi W. (Github username: t-valentine)
- Daniel T. (Github username: NiteToad)
- Crenguta I. (GitHub username: crengutaibrian) - Database
- Bertha I.

## Poetry

Poetry is a python packaging and dependency management.

**Set up**:

- First clone repo in your preferred directory, for example:
  - `git clone https://github.com/t-valentine/cis245-testbank.git $HOME\dev\school\cis245\project\cis245-testbank\` `
- Next make sure you are in your repo directory, for example:
  - `cd $HOME\dev\school\cis245\project\cis245-testbank\`
- One inside your repository, in the terminal you type:
  - `poetry install`
  - This will install all the libraries/modules that are in the pyproject.toml file
- After the installation is complete to activate the poetry environment, in your terminal type:
  - `poetry shell`
- Now you are ready to start coding and if you are using VS Code, in your terminal type:
  - `code .`

**Commands to help you get started**:

- To run your script:
  - `poetry run python app/registration.py`
- To add a library/module to poetry:
  - `poetry add tkinter`
- To remove a library/module from poetry:
  - `poetry remove tkinter`
- To view a list of commands available:
  - `poetry list`
- To view what libraries/modules are installed:
  - `poetry show`
  - `poetry show --tree`
- To run file, make sure you are either in the directory or that you point to it in terminal:
  - `poetry run app/registration.py`
  - `poetry run registration.py`
- To format py file using Black:
  - `poetry run black app/registration.py`
- To see your files performance based on pylints coding guidelines:
  - `poetry run pylint app/registration.py`

For more help with **[Poetry](https://python-poetry.org/docs/)**