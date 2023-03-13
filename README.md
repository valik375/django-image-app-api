# CSF API

## Setup

1) Create a virtual environment to install dependencies:

```sh
pip install virtualenv
virtualenv -p /usr/bin/python3.5 venv
source venv/bin/activate
cd django-image-app-api
```

2) Then install the dependencies:

```sh
cd ../
(env)$ pip install -r requirements.txt
(env)$ python ./manage.py migrate
(env)$ echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin@example.com', 'admin@example.com', 'adminadmin')" | python manage.py shell
```

3) Once `pip` has finished downloading the dependencies and env was started:
```sh
(env)$ python manage.py runserver
```
4) And navigate to `http://127.0.0.1:8000/`.
