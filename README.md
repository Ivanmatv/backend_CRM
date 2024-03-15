# Ambassadors CRM-system

### Description
CRM-system for Yandex Practice Ambassadors.

General description of the task: We want to create a community management infrastructure that brings a predictable flow of marketing engagements per month.

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
- for MacOS
```bash
python3 -m venv venv
source venv/bin/activate
```
- for Windows
```bash
python -m venv venv
source venv/Scripts/activate
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

## API Documentation
http://127.0.0.1:8000/api/swagger/  
http://127.0.0.1:8000/api/redoc/

## Technology
[Python](https://www.python.org), [Django REST framework](https://www.django-rest-framework.org), [PostgreSQL](https://www.postgresql.org/), [Docker](https://www.docker.com/), GitHub Actions

## Authors
Designers:
 - [Zhurbenko Valeriya](https://www.behance.net/vastrin)
 - [Serafima Gross](https://www.behance.net/serafi_me)
 - [Svetlana Belozerova](https://www.behance.net/svetlanbelozer)

Frontend-developers:
 - [Evgeny Zaryanov](https://github.com/EvgenyZaryanov)
 - [Stanislav Uglanov]()
 - [Dmitri]()

Backend-developers:

 - [Anastasia Antipina](https://github.com/an-nastasiia)  
 - [Evgeniy Golodnykh](https://github.com/Evgeniy-Golodnykh)  
 - [Ivan Matveev](https://github.com/Ivanmatv)  
 - [Sergey Chukin](https://github.com/ChukSerg)

System-analysts:
  - [Evgeniy Dunaevskiy]()
  - [Darya Klimova]()
  - [Kovalenko Andrey]()

Business-analytics:
 - [Evgenia Blagochevskaya](https://github.com/Evjhonia)
 - [Likunova Valeriya ](https://github.com/Batofyourdreams )

Project-manager:
 - [Anna Gaidash](https://www.linkedin.com/in/anna-gaidash/)

### CI/CD pipeline status
[![Ambassadors CRM workflow](https://github.com/Ivanmatv/backend_CRM/actions/workflows/crm_workflow.yml/badge.svg)](https://github.com/Ivanmatv/backend_CRM/actions/workflows/crm_workflow.yml)