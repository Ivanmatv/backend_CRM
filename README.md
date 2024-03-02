# Backend_CRM

### Description
CRM-system for Yandex Practice Ambassadors.

### Quick Start
1. Clone repo
```bash
git clone git@github.com:Ivanmatv/backend_CRM.git
```
2. Creates the virtual environment
```bash
python3 -m venv venv
```
3. Activates the virtual environment
```bash
source venv/bin/activate
```
4. Upgrade PIP and install the requirements packages into the virtual environment
```bash
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
```
5. To create the database use command
```bash
python3 manage.py migrate
```
6. To create the superuser use command
```bash
python3 manage.py createsuperuser
```
7. To run the application use command
```bash
python3 manage.py runserver
```

### API Documentation
http://127.0.0.1:8000/api/swagger/  
http://127.0.0.1:8000/api/redoc/

### Technology
[Python](https://www.python.org), [Django REST framework](https://www.django-rest-framework.org), [PostgreSQL](https://www.postgresql.org/), [Docker](https://www.docker.com/), GitHub Actions

### Authors
[Anastasia Antipina](https://github.com/an-nastasiia)  
[Evgeniy Golodnykh](https://github.com/Evgeniy-Golodnykh)  
[Ivan Matveev](https://github.com/Ivanmatv)  
[Sergey Chukin](https://github.com/ChukSerg)

### CI/CD pipeline status
[![Ambassadors CRM workflow](https://github.com/Ivanmatv/backend_CRM/actions/workflows/crm_workflow.yml/badge.svg)](https://github.com/Ivanmatv/backend_CRM/actions/workflows/crm_workflow.yml)