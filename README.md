#  BackendAssignment Django Project

## Project Description
A Django project for create a post.

## Setup
Follow these steps to set up the project on your local machine.
### Prerequisites need
- Python
- Django
- Virtual environment (optional but recommended)
### Installation
git clone https://github.com/lomus123456789/html-project.git
cd BackendAssignment

4.Create a virtual environment and activate it:
python -m venv venv
source venv/Script/activate #for window
source venv/bin/activate  #for ubuntu

5.Install project dependencies
pip install -r requirements.txt

6:Run migrations:
python manage.py makemigrations
python manage.py migrate

7.Start the development server:
python manage.py runserver

8.Explain how to use your Django project, including how to access the application, any key features, and how to interact with it.
Access the web application at http://localhost:8000/

9.API Endpoints
[api/register/ (post api)
api/login/ (post api)
api/create_post/ (post api)
api/posts/ (get api)
]


