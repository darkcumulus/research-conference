# URO-Conference App
A responsive web application that lists upcoming conferences, in a more direct-to-the-point way . created for PSU University Research Office. 

# Features
The usual, commenting system, Image uploads, search/group by category, search/group by keywords (hashtags), time for humans ( a min ago, 12 days ago, 3 weeks from now etc), pagination, and using bulma (meaning its a responsive app).


# Interface
Made with bulma CSS library (not a designer sorry) thanks to the author!

# Installation

1. Install python 3, git, virtualenv, pip3 
2. create virtual environment & activate it
	```batch
	>python.exe -m venv env3
	>env3\scripts\activate.bat
	```
3. Clone this repository
	```batch
	>git clone https://github.com/rcdosado/Kumperensya.git
	>cd Kumperensya
	```
4.  Install dependencies
	```batch
	pip3 install -r requirements.txt
	```
5.  Assuming all dependencies succeeded, Renew the database 
	```batch
	>python manage.py makemigrations
	>python manage.py migrate
	>python manage.py createsuperuser
	>..
	```
6.  Create superuser account (fill the necessary details)
	```batch	
	>python manage.py createsuperuser	
	```
7.  Run the WSGI server
	```batch
	>python manage.py runserver	
	```
8.  Go to localhost:8000/admin, login, then fill the system with information

# Screen Shots

### This is the index page

![id](https://drive.google.com/uc?id=0B-HPOmKexAcsSi1WM1NaQmJmSVU "Index page")

### This is the main page for searching 
-----------------------------------
![id](https://drive.google.com/uc?id=0B-HPOmKexAcsaGJnSzZ4ODdFaEk "Main Listing of Conferences")

### This is the page if you click a conference item
----------------------------------------------
![id](https://drive.google.com/uc?id=0B-HPOmKexAcsRUNCbG1DTHhZYUU "Detailed view of a conference")

### This is one of the admin page.
------------------------------
![id](https://drive.google.com/uc?id=0B-HPOmKexAcsYlh6TF9sTHEweEk "Admin Page listing of conferences")

# Todo
 * related conferences
 * refactor
 * some statistics section
 * static photos (currently photos are random)
 * tests
 
 
