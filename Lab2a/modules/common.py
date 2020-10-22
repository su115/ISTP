import datetime
import sys


def get_current_date():
    """
    :return: DateTime object
    """
    return datetime.datetime


def get_current_platform():
    """
    :return: current platform
    """
    return sys.platform

def myfoo1(value):
    if value%2==1:value=False
    else:value=True
    for i in range(100):
        if value and i%2 == 0:
            print(i,end=' ')
        elif not value and i%2 == 1:

            print(i,end=' ')
            
def myfoo2(log,value):

    if value==0:
        log.error('value==0 error')
    else:
        log.info('you dont get error')

