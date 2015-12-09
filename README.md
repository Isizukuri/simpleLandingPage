# Installation

You need to install virtualenv and then activate it:

```pip install virtualenv --no-site-packages```

```virtualenv env```

```source env/bin/activate```

After it you need to install requirements for project:

```pip install -r requirements```

Note: PIL and Pillow require that image libraries are installed on your system. On e.g. Debian or Ubuntu, you’d need these packages to compile and install Pillow:

```apt-get -y install libz-dev libjpeg-dev libfreetype6-dev python-dev```

To make send_email function properly, you must ask for SMTP server configuration and make changes to email_config.py

# Quickstart

To start the project you need to run Django development server:

```python manage.py runserver```
