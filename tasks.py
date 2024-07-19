import time
from celery import Celery

app = Celery('tasks', 
             broker='pyamqp://guest@rabbitmq//',
             backend='redis://redis:6379/0')

@app.task
def ola_mundo():
    print("Olá, Mundo!")
    time.sleep(10)
    print("Task completada!")
    return "Olá, Mundo!"
