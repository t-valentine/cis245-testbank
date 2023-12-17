# cis245-testbank

This is the group project for CIS 245.

## Authors

- Tobi W. (Github username: t-valentine)
- Daniel T. (Github username: NiteToad)
- Crenguta I. (GitHub username: crengutaibrian) - Database
- Bertha I. (Github username:Bertelib)
- Lakhdar D. (username: ldehbi)
- John S .(username:Wozoht07) - Database Contributor

## Poetry

Poetry is a python packaging and dependency management.

**Set up**:

- First you need to install poetry:
  - if you have windows just paste the following into your powershell terminal:
    - `(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -`
  - if you have linux, macOS, WSL:
    - `curl -sSL https://install.python-poetry.org | python3 -`
  - after installing please add poetry to your PATH via edit environment variables on windows, for example this is mine:
    - `C:\Users\Dtorr\AppData\Roaming\Python\Scripts`
- Now you clone repo in your preferred directory, for example:
  - `git clone https://github.com/t-valentine/cis245-testbank.git $HOME\dev\school\cis245\project\cis245-testbank\` `
- Then change into your repo directory, for example:
  - `cd $HOME\dev\school\cis245\project\cis245-testbank\`
- Once inside your repository directory, in the terminal you can type:
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

## MySQL Database for development

The scripts (reset_schema.ps1 & reset_schema.sh) are designed to reset the database schema and insert our mock data for the project.
The scripts run SQL scripts to drop existing tables, create new ones, and then populate them with our mock data.

### Running the script

1. **Open Terminal:** This should be either Bash, zsh, Git Bash, or Powershell.
2. **Navigate to your Directory:** `cd cis245-testbank`
3. **Edit Script:** Enter your own Username, Database name (testbank is expected), and hostname (localhost is expected).
4. **Execute the Script:** 
    - If you are on Linux/MacOS or using Git Bash, your command will be `db/reset_schema.sh` 
    - If you are using Windows Powershell your command will be `db/reset_schema.ps1`
5. **Enter your MySQL Password:** After running the script you will be prompted to enter your password 


