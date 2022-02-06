# how-to :: Deploy Le App de Flask
---
## Overview
Just a quick rundown how to deploy a Flask app using Apache2.

### Estimated Time Cost: 30 minutes and change

### Prerequisites:

- Python3 & Flask installed
- Apache2 & mod_wsgi installed

### Let's Get Cracking

1. Install those prerequisities
2. Setup the flask file structure (located in ```/var/www```)
It should look something like this:
```
my-foist-app/
├─ logs/
├─ app/
│  ├─ static/
│  ├─ templates/
│  ├─ __init__.py
│  ├─ app.py
├─ app.wsgi
```
3. Configure ```__init__.py``` to import flask & other files (ie. ```app.py```).
```python
from flask import Flask
import app
```
4. Configure ```app.py```
```python
from flask import Flask
app = Flask(__name__)

app.route("/")
def hello_world():
    return "Hello World!"

...

if __name__ == '__main__': 
    app.run(host='0.0.0.0')
```
4. Configure ```app.wsgi``` (this is outside the ```app``` folder)
```python
import sys
sys.path.insert(0, '/var/www/myfoistapp/app')

from app import app as application
```

5. Configure the Apache2 config files.<br>
```bash
cd /etc/apache2
sudo nano sites-available/myfoistapp.conf
```
```
<VirtualHost *:PORT_NUM>
    ServerName IP_ADDRESS

    WSGIDaemonProcess flaskapp user=www-data group=www-data threads=5
    WSGIScriptAlias / /var/www/myfoistapp/app.wsgi

    <Directory /var/www/myfoistapp>
        WSGIProcessGroup flaskapp
        WSGIApplicationGroup %{GLOBAL}
        Order deny,allow
        Allow from all
    </Directory>

    ErrorLog /var/www/myfoistapp/logs/error.log
    CustomLog /var/www/myfoistapp/logs/access.log combined
</VirtualHost>
```
6. Enable the site & restart apache2 service
```bash
sudo a2ensite myfoistapp.conf
suod service apache2 restart
```
7. (OPTIONAL... kind of) If your ```ports.conf``` in ```/etc/apache2``` doesn't contain your desired port, add the following to the file to enable said port.
```
Listen PORT_NUM
```
8. Go to the site!
### Resources
* https://flask.palletsprojects.com/en/2.0.x/deploying/mod_wsgi/
---

Accurate as of (last update): 2021-01-19

#### Contributors:  
Daniel Sooknanan, pd2  
