# djproj3
в папке
C:\Users\sunchara\Documents\djproj\djproj
выполняем
celery worker --app=cel --pool=solo --loglevel=INFO
celery worker --app=cel --pool=solo --loglevel=INFO

-запускаем 2 воркеров, по одному в терминале

python C:\Users\sunchara\Documents\djproj\manage.py runserver 

-запускаем джанго

-запускаем mongodb

curl -X POST --data https://upload.wikimedia.org/wikipedia/commons/thumb/0/0b/Cat_poster_1.jpg/275px-Cat_poster_1.jpg localhost:8000

- получаем guid котиков

curl -X GET --data f676ae37-1b0d-447b-bd35-b5f3fd5392c2 localhost:8000


- получаем хеш котиков
