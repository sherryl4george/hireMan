Install WAMP. Set up your DB and set MySQL root password as root (If you set anything different make changes in config.py file)
Install all dependencies to (venv) from the requirements.txt file
set FLASK_APP = app.py in the PyCharm terminal (replace set with export if in Linux)
Execute the below commands:
1. flask db init
2. flask db migrate
3. flask db upgrade
Steps 2 & 3 need to be executed when ever you update the model
> flask run to run the project
You can use localhost:5000/admin to create initial roles and login credentials