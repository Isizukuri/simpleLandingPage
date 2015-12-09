# Installation

You need to install virtualenv and then activate it:

```pip install virtualenv --no-site-packages```

```virtualenv env```

```source env/bin/activate```

After it you need to install requirements for project:

```pip install -r requirements```

To make send_email function properly, you must ask for SMTP server configuration and make changes to settings.py

# Quickstart

To start the project you need to run Django development server:

```python manage.py runserver```
