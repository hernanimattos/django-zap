
This app it for comunicate with zapsign api and make a crud of signatures in documents


Stack

- Python 3.11
- Django 3.1
- Django Rest Framework 3.11
- Postgres 12
- Docker
- Docker Compose


- Create a Virtual Env `python3 -m venv {nome_do_ambiente}`

- Active virtuaEvn `source env_zap_dev/bin/activate`

- Install dependencies `python3 -m pip install -r requirements.txt`

- To init django project `django-admin startproject zap`

- To create an app access the folder of project cd [zap] `python3 manage.py startapp api`

- To create a migration `python3 manage.py makemigrations`

- To create db `python3 manage.py migrate`

- Run server `python3 manage.py runserver`


