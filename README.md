# Installation

You need to install virtualenv and then activate it:

```pip install virtualenv --no-site-packages```

```virtualenv env```

```source env/bin/activate```

Note: PIL and Pillow require that image libraries are installed on your system. On e.g. Debian or Ubuntu, you’d need these packages to compile and install Pillow:

```sudo apt-get -y install libz-dev libjpeg-dev libfreetype6-dev python-dev```

After it you need to install requirements for project:

```pip install -r requirements.txt```

Then, you need to install bower, which requires node, npm and git.

Installing git (if not already installed):

```sudo apt-get install git```

The steps to install Node.js/npm inside on your virtualenv:

```$ curl http://nodejs.org/dist/node-latest.tar.gz | tar xvz```

```$ cd node-v*```

```$ ./configure --prefix=$VIRTUAL_ENV```

```$ make install```

To install bower:

```npm install -g bower```

Finally, you have to install static dependencies with bower:

```bower install```

To make send_email function properly, you must copy  email_config_sample.py from project directory (sendmail) to root directory and configure it for your SMTP server and account.
# Quickstart

To start the project you need to create tables in DB and then run Django development server:

```python manage.py migrate```

```python manage.py runserver```
