## Build Instructions

### Python
Download python 3.6 on the machine using the following link https://www.python.org/ftp/python/3.6.8/python-3.6.8-macosx10.9.pkg which will download python 3.6.8 for macOS.

### Version Control
Clone repo from repository-url by running :-
* `git clone -b development https://github.com/13AbhishekJha/YoutubeApi.git`
* `cd YoutubeApi`

### Setup Virtual Environment
Install virtualenv using command : `pip3 install virtualenv`
Execute command : `virtualenv -p python3 venv`
Execute command : `source venv/bin/activate`
Verify python version by running `python --version`

### Docker-Compose
Install docker-compose using brew `brew install docker-compose`
To validate docker-compose installation run `docker-compose -v`
Output must be something like `Docker Compose version v2.13.0`

### After performing above operations, run below command, which build the complete application using docker-compose
* docker-compose up

### Build applictions individually
To trigger the periodic Youtube API ping
* cd app
* docker-compose up

To start the web-server running on Flask to connect to the mysql db
* cd youtube
* docker-compose up

### DB Configuration
###### Mysql config
docker run -e MYSQL_ROOT_PASSWORD=my-secret-pw -p 3306:3306 mysql

###### redis config
docker run -it --rm --name redis --net redis -p 6379:6379 redis:6.0-alpine


### Initiate the Celery workers and Beat.
celery -A worker.celery_worker worker -l info
celery -A worker.celery_worker beat -l info


### Run the web server.
cd ../youtube
python main.py
