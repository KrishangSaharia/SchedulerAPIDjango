from django.shortcuts import render
from datetime import datetime
import requests

import os

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger


def print_function():
    print('y')

def call_url(url):
    print(datetime.now())
    r = requests.get('{0}'.format(url))
    print('status code', r.status_code)


@api_view(['GET'])
def schedule_url(request):
    url = request.GET['url']
    stamp = request.GET['datetime']
    stamp = datetime.strptime(stamp, '%d/%m/%y %H:%M:%S')
    print(stamp.day)
    print(stamp.second)
    # print(stamp)
    # datetime = request.GET['datetime']
    # timestamp = datetime.strptime(request.GET['datetime'], '%d/%m/%y %H:%M:%S')
    # print(datetime.day())
    # if datetime.now() == 
    scheduler = BackgroundScheduler()
    scheduler.add_job(call_url,'cron', args=[url] , second = stamp.second, minute = stamp.minute, hour = stamp.hour, day =stamp.day, month = stamp.month, year = stamp.year)
    scheduler.start()

    # print(request.GET['datetime'])
   
    # print(parse_date("23.11.2009 12:34:56"))
    return Response(status = status.HTTP_200_OK)


@api_view(['GET'])
def ping_status(request):
    response = os.system("ping -n 1 " + request.GET['url'])

    if response == 0:
        pingstatus = "OK"
    else:
        pingstatus = "Network Error"

    data = {
        'status': pingstatus
    }

    return Response(data, status = status.HTTP_200_OK)
