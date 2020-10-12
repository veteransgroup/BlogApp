# Django Blog website

"Django Blog" prototype website written in Django by <a href="mailto:liubing009@gmail.com">Jeff</a>


## Overview

This web application creates an online blog.

## Quick Start

To get this project up and running locally on your computer:
1. Set up the [Python development environment]
   I recommend using a Python virtual environment.
1. Assuming you have Python setup, run the following commands:
   ```
   pip3 install -r requirements.txt
   python3 manage.py migrate
   python3 manage.py createsuperuser # Create a superuser
   python3 manage.py runserver
   ```
1. Open a browser to `http://127.0.0.1:8000/admin/` to open the admin site
1. Now you have a blank blog website
1. You can generate batch test data by run command:
   python -m scripts.fake

1. Because search function rely on Elasticsearch service, if you don't want to launch a Elasticsearch service. 
   Please set env `export ENABLE_HAYSTACK_REALTIME_SIGNAL_PROCESSOR=no` to close real-time indexing.





## Have fun