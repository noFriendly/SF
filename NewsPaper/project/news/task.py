from celery import app

@app.task
def add(x, y):
    z = x + y
    print(z)