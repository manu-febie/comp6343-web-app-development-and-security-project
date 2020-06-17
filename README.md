# COMP 6343 Web Application Development and Security

#### Final Project
This project is build using Flask, Docker and VueJS. Data is stored in a PostgreSQL database. All the python dependencies can be installed using `pip`. Just run `pip install -r requirements.txt` *(using a virtualenvironment is recommended)*. 

#### Local setup guide
Make sure you have `python 3.8.*` setup as your default python interpreter or create a virtual environment with `python 3.8.*`. Clone this project into whatever directory you want on your system `git clone https://github.com/imanuelfebie/comp6343-web-app-development-and-security-project.git`. Then run the following commands:

Change into project directory:
```bash
cd comp6343-web-app-development-and-security-project
```

Change into flask directory:
```bash
cd flask
```

Inside the flask directory, create a virtual environment using `venv`. (since this project is using python 3.8, make sure you have it installed on your system. You don't need to set it as your default python interpreter, but you can specify you want to use it as the default interpreter inside your virtual environment):
```bash
python3.8 -m venv <ENVIRONMENT_NAME>
```

Activate your virtual environment:
```bash
source <ENVIRONMENT_NAME>/bin/activate
```

Upgrade pip and install the requirements from `requirements.txt` after you have activated the virtual environment:
```
pip install --upgrade pip
pip install -r requirements.txt
```

#### Local PostgreSQL database setup
This project is using PostgreSQL to store data. How to install it will depend on your OS. 

