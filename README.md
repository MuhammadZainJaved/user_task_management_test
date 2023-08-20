# UserRoleManagement Project

This is a Django-based project for user role management and task management. It provides APIs for user authentication, task creation, and viewing tasks.

## Table of Contents

- [setup]
## SETUP

1. Set up repository and start project:

   1 -git clone https://github.com/MuhammadZainJaved/user_task_management_test.git

   2 - cd user_task_management
   
   3 - python -m venv venv

   4 - source venv/scripts/activate

   5 - pip install - requirements.txt
   
   6 - python manage.py makemigrations

   7 - python manage.py migrate

   8 - python manage.py runserver

   
## Project IDEA
- This is a simple user management system in which a super user can act as a manager and create and assign task and individuals can skim through the list of their tasks.
- The project aims to have a backend system for a user management system with authentication and authorization system in place.
-  This project is a baseline module which can be scaled to have different auth mechanisms integrated
-  For now a simple token based mechanism is created and implemented for the API authentication. JWT is configured and can be implemented in the near future.


