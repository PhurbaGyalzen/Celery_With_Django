
## Setup (linux)

To try the project, set up a virtual environment and install the listed dependencies:

```sh
$ python -m venv venv
$ source venv/bin/activate
(venv) $ python -m pip install -r requirements.txt
```

You'll also need to install Redis on your system:

```sh
$ sudo apt install redis
```

Once you've installed all the dependencies, you need to start four processes that need to run at the same time:

1. Django
2. Redis
3. Celery
4. Flower

To get all of them running, open four different terminal windows and start them one-by-one:

**Django app:**

```sh
(venv) $ python manage.py migrate
(venv) $ python manage.py runserver
```

**Redis server:**

```sh
$ redis-server
```

**Celery:**

```sh
(venv) $ python -m celery -A django_celery worker -l info
```


**Flower:**

```sh
(venv) $ celery -A django_celery flower --address=127.0.0.6 --port=5566
```

When all four processes are running, you can go to `localhost:8000/` and submit a feedback response. Celery will simulate a work-intensive process and send an email at the end of it. You'll see the email message show up in the log stream on the terminal window where the Celery worker is running. After that you can go to `127.0.0.6:5566/` and track the celery task status. 
