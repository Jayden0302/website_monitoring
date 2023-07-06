# Website Monitoring Tool
A simple tool to monitor the accessibility and responsibility of a list of websites configured in the config file

# Setting up Local Environment
It is always better to setup a Python virtual environment for a better dependency management
## Python Virtual Environment (Venv)
### Install Venv
```
  pip install virtualenv
```
### Create Venv
```
  python -m venv <venv_name>
```
### Activate Venv
```
  cd .\venv\Scripts
  activate.bat
```
**Note:** You can see (<venv_name>) if the Venv is activated successfully.

## Install dependencies
```
  pip install -r requirements.txt
```

## To run the tool
```
  python main.py <time_interval>
```
The tool accept an integer arguement from command-line, ommit it to get the default_time_interval from the config.json.
