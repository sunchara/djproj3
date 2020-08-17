from __future__ import absolute_import, unicode_literals

from celery import Celery

app = Celery('cel',
             broker='mongodb://localhost:27017/jobs',
             backend='mongodb://localhost:27017/res',
             include=['task'])
if __name__ == '__main__':
    app.start()
#celery worker --app=cel --pool=solo --loglevel=INFO
