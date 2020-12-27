# Login-Signup_System
Login and Signup System using Python tkinter module. Alternatively referred to as a sign in, a login or logon is a set of credentials used to gain access to an area that requires proper authorization. Logins are used to gain access to and control of computers, networks, and bulletin boards, as well as other services and devices. The login page serves several purposes. It allows new applicants to register for a logon ID and password. Facilitates a login point for those who already have a ID and password. Allows users with an ID and password to simply search and view context which have been set up in local database.

## Modules Used
### tkinter module
- Tkinter is the inbuilt python module that is used to create GUI applications. It is one of the most commonly used modules for creating GUI applications in Python as it is simple   and easy to work with. You don’t need to worry about the installation of the Tkinter module separately as it comes with Python already. It gives an object-oriented interface to   the Tk GUI toolkit.
### SQLite3 module
- sqlite3 module provides a lightweight disk-based database that doesn’t require a separate server process and allows accessing the database using a python program. We can perform   various actions such as connecting to a database, execute sql queries, update the database and return the database results.
## Dependencies
- pip install sqlite3

## Features
- Sign up
  - Creates a new account
  - Accepts user name, user email and new password
  - On successful signup, pops up message saying "Account created"
- Logging in
  - Accepts user email and password
  - Checks if account is present in the database
  - If account present, executes message - "User found with the user name"
  - If account not present, executes - "User not found"
  
## Installation
- To run the application locally, you can issue the following commands:
  - $ git clone https://github.com/rutuja1302/Login-Signup_System
  - $ cd Login-Signup_System
  
## Screenshots
- ### Main Front end of the application with two options- login & signup
  ![](https://github.com/rutuja1302/Login-Signup_System/blob/main/Main/op_1.jpg)
- ### Signup Page upon successful signing into the application
  ![](https://github.com/rutuja1302/Login-Signup_System/blob/main/Main/op_2.jpg)
- ### Login Page
  ![](https://github.com/rutuja1302/Login-Signup_System/blob/main/Main/op_3.jpg)
