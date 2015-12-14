# Installation

You need to install virtualenv and then activate it:

```pip install virtualenv```

```virtualenv env --no-site-packages```

```source env/bin/activate```

After it you need to install requirements for project:

```pip install -r requirements.txt```

To make send_email function properly, you must copy  email_config_sample.py from project directory (sendmail) to root directory and configure it for your SMTP server and account.
# Quickstart

To start the project you need to create tables in DB and then run Django development server:

```cd sendmail```

```python manage.py migrate```

```python manage.py runserver```
