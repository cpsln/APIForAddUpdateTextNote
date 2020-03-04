### Setup Step:
This is a Guide for create API's for a note-taking web application.

1. Installing Git

        
        $ sudo apt install git

2. Install and Setup virtualenv (Also includes setup for workon)

        First we need to install python-pip in order to be able to use pip
       
        $ sudo apt install python3-pip
        
        Once done, we can now install virtualenv
        
        $ sudo pip3 install virtualenv
        $ sudo pip3 install virtualenvwrapper
        

        
        $ vi ~/.bashrc
        
        Add these lines end of file:
        
            export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
            export VIRTUALENVWRAPPER_VIRTUALENV=/usr/local/bin/virtualenv
            export WORKON_HOME=/home/cpsln/Desktop/urbanstop/venv
            export PROJECT_HOME=/home/cpsln/projects
            source /usr/local/bin/virtualenvwrapper.sh

        
        > Restart the terminal to get the changes

3. Mysql installation and user creation:

       
        $ sudo apt-get install mysql-server
        $ sudo apt-get install python-dev default-libmysqlclient-dev
        $ sudo mysql
        

        Create user for ALL GRANT
        ============================

        
        mysql> CREATE USER 'root'@'%' IDENTIFIED BY 'root';
        mysql> GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' WITH GRANT OPTION;
        mysql> FLUSH PRIVILEGES;

        Create Database, name is "urbanstop":
        =================

        mysql> create database urbanstop;

4. Clone this Repository:

         
        git clone https://gitlab.com/cpsln/DataAnalyzer.git 


6. Create a new virtualenv for text note api

       
        $ mkvirtualenv textnote

5. Go to the cloned directory ,Location of this is supposed to be "/home/cpsln/Desktop/backend"

       
        $ cd backend
        $ pip install requirments.txt

        $ python manage.py runserver

