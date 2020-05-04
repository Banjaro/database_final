# CS 2200 - Databases -  Final project
# Written By: Patrick Cobb, Ryan Copeland


## This application has only been tested on Windows 10 and Ubuntu 16.04


This application is a sample database program that can be used to track the assets (employees/projects/etc.) of companies

Before attempting to run the program please follow the steps below:

0. This project assumes that you have a MYSQL database setup already and that you have root permissions

1. This project requires access to an MYSQL database in order to function. In order to give the program access to your mysql database, go to **config.py** and input your mysql credentials and the name of the database where you would like to store your company information

2. (Windows) Insure scripting permissions are enabled. (Run cmd as admin, and type the command "Set-ExecutionPolicy Unrestricted")

3. Go to the filepath of this project and install prerequisites (bash: "chmod u+x LinuxInstall.sh" - Powershell: "./WindowsInstall.ps1")

4. Initialize database by running "startup.sql" in mysql.

5. Go to the filepath of this project and type ./run.py

6. Navigate to your browser of choice and paste **localhost:5000** into the address bar

You should see the login page for "The Business Machine --- Created my Team Corporate Sellout"