# SchedulingAPIDjango

## Table of contents
* [General info](#general-info)
* [Setup](#setup)

## General info
This project includes scheduling Django Rest APIs, it uses AdvancedPythonScheduler module fro scheduling tasks.
This contains 2 endpoints - 
one for scheduling and other one is ping endpoint to check whether the server is alive or not .

### 1. Scheduling Endpoint :
This requires two arguements - first arguement will be datetime string in the format '%d/%m/%y %H:%M:%S' . For eg. 09/01/21 13:39:30 .
and second arguement will be the url which is to be called at scheduled time . For eg. https://google.com .

Response will JSON data with a message "Task Scheduled Successfully!" , if scheduling is successfull.
For eg. - 
```
${
$    "message": "Task Scheduled Successfully!"
$}
```


### 2. Ping Endpoint -
This endpoint checks whether server is alive or not , and returns JSON message 'OK' is server is alive , otherwise returns 'Network Error'.
For eg. - 
```
${
$    "status": "OK"
$}
```

## Setup
To install all the dependencies run: 

```
$ pip install -r requirements.txt
```

## Run :
```
$ python manage.py makemigrations
$ python manage.py migrate
```

## To start the server:
```
$ python manage.py runserver
```
### Now , you can start deploying at your local host.

