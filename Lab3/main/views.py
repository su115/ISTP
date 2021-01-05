from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
import os 
from datetime import datetime


def MyView(request):
    return render(request, 'main.html',{'selector':'value'})
def MyJson(request):
    resault={
            'date':datetime.now().isoformat(),
            'servername': 'testing server',
            'server_url': request.build_absolute_uri(),
            'server_iinfo': {
                'system': os.name,
                # Docker in Lab4 dont want work with them
#                'user': os.getlogin(),
#                'srv_pid': os.getpid(),
            },
            'client_info': {
                'user agent': request.META['HTTP_USER_AGENT'],
                'remote addr': request.META['REMOTE_ADDR'],
                'remote host': request.META['REMOTE_HOST'],
            }
        }
    return JsonResponse(resault)
