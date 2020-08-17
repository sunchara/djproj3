from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.decorators import api_view
from celery import Celery
from celery.result import AsyncResult
from djproj.cel import app


@api_view(['GET', 'POST'])
def foo(req):
    if req.method == 'POST':
        tsk =app.send_task('get_md5', args=[req.body.decode()], kwargs={})
        return Response(tsk.id, status=status.HTTP_202_ACCEPTED)
    elif req.method == 'GET':
        async_res = AsyncResult(req.body.decode())
        try:
            if async_res.ready():
                data = async_res.get()
                print(str(data),type(data),'\n\n')
                if data[0] == status.HTTP_200_OK:
                    return Response(data[1], status=status.HTTP_200_OK)
                else:
                    return Response(
                        "Error, response by url with status " +
                        f"{data[0]}, error msg: {str(data[1])}",
                        status=status.HTTP_400_BAD_REQUEST
                        )
            else:
                return Response(
                    async_res.status.decode(),
                    status=status.HTTP_409_CONFLICT
                    )
        except Exception as e:
            print(f"Exception raised: {str(e)}")
            return Response(
                f"Exception raised: {str(e)}" ,
                status=status.HTTP_400_BAD_REQUEST
                )
