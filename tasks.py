from celery import Celery
import docker
#app = Celery('tasks', backend='rpc://', broker='pyamqp://')
app = Celery('tasks')
app.config_from_object('celeryconfig')
# EXAMPLE CALL celery -A tasks worker --loglevel=info

client = docker.from_env()

@app.task
def add(x, y):
    return x + y

@app.task
def run_bt2():
    return client.containers.run('bowtie2-dock', 'bowtie2')
