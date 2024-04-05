
Flask Todo App
This is a simple Todo application built using Flask and SQLAlchemy.

Installation
Clone the repository: git clone https://github.com/your-username/flask-todo-app.git
Navigate to the project directory: cd flask-todo-app
Create a virtual environment (optional but recommended): python -m venv venv
Activate the virtual environment:

On Windows: venv\Scripts\activate
Install the required packages:
pip install -r requirements.txt
Set up the database: Open a Python shell:

python
Inside the Python shell, run the following commands to create the database tables:
from app import db
db.create_all()
exit()
Start the Flask development server:

flask run
Usage
Open your web browser and navigate to http://localhost:5000.
You can add new tasks, mark tasks as completed, and delete tasks.
Contributing
Fork the repository.
Create a new branch (git checkout -b feature/my-feature).
Make your changes.
Commit your changes (git commit -am 'Add new feature').
Push to the branch (git push origin feature/my-feature).
Create a new Pull Request.
