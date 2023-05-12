# A Membership-System (prototype)
The prototype of a membership system designed to keep records on SQLLite3 database (which comes by default with Django). 

To begin begin writing: 
Step 1 : 
Clone the repository 


Step 2 . Install python :
Kindly make sure you have python installed . 
Download python here [https://www.python.org/downloads/release/python-31011/]

Step 3 :
Create a virtual environment with the command :  
`python -m venv venv`  (On Windows) 

Step 4 
Activate the virtual Environment : 
Type in :  
cd venv\Scripts\activate  (hit enter)

 

Step 5 : 
After activating your virtual environment ;  Run the command below to install django and default pacakges automatically: 
`pip install -r requirements.txt` 
(This will installs all the packages required to run the code) 

Step 6 :
======== CREATE A SUPER USER (to have administrative access) =====
In your terminal type in the command below and hit enter: 
`python manage.py createsuperuser`

Follow the prompts and enter your preferred username , email and password to create an admin account. 


Lastly, Run the command below to start the built in server : 
`python manage.py runserver`

By default the django server runs on your localhost server (http://127.0.0.1:8000/)
So you can simply copy and paste http://127.0.0.1:8000/ to see the live website . 

