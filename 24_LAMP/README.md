# how-to :: CREATE A DIGITAL OCEAN DROPLET WITH UBUNTU AND APACHE
---
## Overview

Just a quick rundown on what to do for provisioning
a Droplet from Digital Ocean.

### Estimated Time Cost: 1-2 hours

#### Prerequisites:

- [Github Student Developer Pack](https://education.github.com/pack) (Sign up using your Stuy ID)

#### Acquiring the Droplet
1. Sign into DigitalOcean with Github.
2. Link a debit/credit card or PayPal account.
3. Select a Ubuntu 20.04 Droplet.

Switch to root user before starting this

Run the following commands
```
sudo apt install apache2
sudo apt install libapache2-mod-wsgi python-dev
sudo a2enmod wsgi 
```

#### Creating a Flask App
Run
```
cd /var/www
mkdir FlaskApp
cd FlaskApp/
mkdir app/
cd app/
mkdir static/ templates/

```
Verify you directory struct looks like this:
```
/var/www/ :
├── FlaskApp
│   └── app
│       ├── static
│       └── templates
└── html
    └── index.html
```

Run
```
cd /var/www/FlaskApp/app/
nano __init__.py
```
Nano should open and you should type some basic python flask code 
A suggestion:
```Python
from flask import Flask
app = Flask(__name__)
@app.route("/")
def main():
    return "Hello, World"
    
if __name__ == "__main__":
    app.run()
```

#### Installing Flask
Run:
```
apt install python3-pip
pip install virtualenv
cd /var/www/FlaskApp/app/
virtualenv venv/
source venv/bin/activate
```
The virtual env should appear, then continue on and run:
```
pip install flask
python __init__.py
```
If the normal flask stuff shows up, Ctrl-C and deactivate the virtual env

#### Configure a Virtual Host
Run:
```
cd /etc/apache2/sites-available/
wget grixisutils.site/lamp_tools/FlaskApp.conf
```
See where wget stores the file to, and mv it to `FlaskApp.conf`

`cat FlaskApp.conf` to make sure the conf file is good, if it is run
`sudo a2ensite FlaskApp`.

Run:
```
cd /var/www/FlaskApp/
wget grixisutils.site/lamp_tools/flaskapp.wsgi
```
Make sure you rename the file it saves to `flaskapp.wsgi`

service apache2 restart



### Resources
* [Github Student Developer Pack](https://education.github.com/pack)
* [Digital Ocean](https://www.digitalocean.com/)
* [Droplet How-Tos](https://www.digitalocean.com/docs/droplets/how-to/)
* [Installing LAMP stack on Ubuntu 20.04](https://www.digitalocean.com/community/tutorials/how-to-install-linux-apache-mysql-php-lamp-stack-on-ubuntu-20-04)
* [Error Permission denied (publickey) when I try to ssh](https://www.digitalocean.com/community/questions/error-permission-denied-publickey-when-i-try-to-ssh)
* [Secure Ubuntu server for non-root user using only SSH keys](https://www.digitalocean.com/community/questions/secure-ubuntu-server-for-non-root-user-using-only-ssh-keys?answer=22286)
* [How To Create a New Sudo-enabled User on Ubuntu 20.04 [Quickstart]](https://www.digitalocean.com/community/tutorials/how-to-create-a-new-sudo-enabled-user-on-ubuntu-20-04-quickstart)
* [Error Permission denied (publickey) when I try to ssh](https://www.digitalocean.com/community/questions/error-permission-denied-publickey-when-i-try-to-ssh?answer=44730)
* [How to Connect to your Droplet with PuTTY on Windows](https://www.digitalocean.com/docs/droplets/how-to/connect-with-ssh/putty/)
* [How to Create SSH Keys with OpenSSH on MacOS or Linux](https://www.digitalocean.com/docs/droplets/how-to/add-ssh-keys/create-with-openssh/)
* [How to Connect to your Droplet with OpenSSH](https://www.digitalocean.com/docs/droplets/how-to/connect-with-ssh/openssh/)

---

Accurate as of (last update): 2022-01-17

#### Contributors:  
Cameron Nelson, pd 2  
Daniel Sooknanan, pd 2  