'''
<commandline>
#variable#
`code`
'''

'''
1. Go home directory
2. touch .env
  3. export ENVNAME=ENVVAR
  4. source .env

5. On Reboot, these are erased
  6. vim .profile
    7. at bottom of above file, type 'source .env'


###### Setting up Server ########


1. Install gunicorn
  a. Install Httptools
  b. Install uvloop
2. <gunicorn -w 4 -k uvicorn.workers.UvicornWorker app.main:app --bind 0.0.0.0:8000>


### Creating service ######

1. /etc/systemd/system/
  a. All services installed on machine

2. create #servicename#.service
  `
  [Unit]
  Description=#your description here#
  After = network.target

  [Service]
  User=#youruser#
  Group=#youruser#
  WorkingDirectory=#yourworkingdirectory#
  Environment="PATH=#yourenvpath#" In conda it's in bin after path
  EnvironmentFile=#pathtoenvfile# !Make sure to remove from profile and remove export name!
  ExecStart=^Environment/<terminal command to start> In conda it's in bin

  [Install]
  WantedBy=multi-user.target

3. start it systemctl start #servicename#
4. Start on reboot
  a. sudo systemctl enable #servicename#

######## NGINX #########

1. conda install nginx
2. sudo apt install nginx -y
3. systemctl start nginx


4. configure
  a. open /etc/nginx/sites-available default
  b. change location
    C. proxy_pass http://localhost:8000;
    d. Delete other line


#### HTTPS #####

1. Purchase domain name
  a. namescheap.com

2. How to point digital ocean nameservers from common domain registrars - Digital ocean

3. Manage dns on digital ocean
  a. enter domain name
  b. create a record
    @
    droplet
    create record
  c. Create cname record
    www
    @
    create record


4. Certbot
5. Firewall
  sudo ufw allow
    http
    https
    ssh
  sudo ufw enable

##### making changes ######

1. pull from git
2. systemctl restart api







'''

