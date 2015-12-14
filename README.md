# Installation

You need to install virtualenv and then activate it:

```pip install virtualenv```

```virtualenv env --no-site-packages```

```source env/bin/activate```

After it you need to install requirements for project:

```pip install -r requirements.txt```

# Quickstart

To start the project you need to create tables in DB and then run Django development server:

```cd sendmail```

```python manage.py migrate```

```python manage.py runserver```
