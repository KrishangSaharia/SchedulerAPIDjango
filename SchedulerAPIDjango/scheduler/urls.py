from django.urls import path

from views import schedule_url

app_name = 'scheduler'

urlpatterns = [
    path('', schedule_url, name='schedule_url')
]