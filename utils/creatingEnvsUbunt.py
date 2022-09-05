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

2. create #filename#.service
  `
  [Unit]
  Description=#your description here#
  After = network.target

  [Service]
  User=#youruser#
  Group=#youruser#
  WorkingDirectory=#yourworkingdirectory#
  Environment="PATH=#yourenvpath#"
  ExecStart=^Environment/<terminal command to start>

  [Install]
  WantedBy=multi-user.target
'''

