from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from scheduler import views

def print_function():
    print()

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(print_function, 'interval', hours=1)
    scheduler.start()